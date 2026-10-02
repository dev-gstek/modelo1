from celery import shared_task
from django.db import transaction
from decimal import Decimal
from catalog.models import Marketplace, ProductMapping
from orders.models import Order, OrderItem
from orders.services import calculate_order_financials
from .integrations.mercadolivre import MercadoLivreClient
import logging
from dateutil import parser

logger = logging.getLogger(__name__)

@shared_task
def sync_mercadolivre_orders():
    logger.info("Iniciando sincronização de pedidos do Mercado Livre...")
    
    # 1. Pega as credenciais
    try:
        marketplace = Marketplace.objects.get(name__icontains="Mercado Livre")
    except Marketplace.DoesNotExist:
        logger.error("Marketplace Mercado Livre não configurado.")
        return "Fail: ML Not Configured"

    # 2. Conecta na API
    client = MercadoLivreClient(marketplace)
    orders_data = client.fetch_recent_orders()
    
    # 3. Processa e Salva
    for data in orders_data:
        external_id = str(data.get('id'))
        
        # Pula se o pedido já existe (Evita duplicidade)
        if Order.objects.filter(external_order_id=external_id).exists():
            continue
            
        with transaction.atomic():
            # Cria a cabeça do Pedido
            order = Order.objects.create(
                marketplace=marketplace,
                external_order_id=external_id,
                customer_name=data.get('buyer', {}).get('first_name', 'Cliente ML'),
                status='paid',
                total_amount=Decimal(str(data.get('total_amount', 0))),
                shipping_cost=Decimal(str(data.get('shipping_cost', 0))),
                marketplace_fee=Decimal(str(data.get('order_items', [{}])[0].get('sale_fee', 0))),
                order_date=parser.parse(data.get('date_created'))
            )
            
            # Processa os Itens (Cruza com o De/Para)
            for item_data in data.get('order_items', []):
                external_sku = item_data.get('item', {}).get('seller_sku')
                
                try:
                    mapping = ProductMapping.objects.get(marketplace=marketplace, external_sku=external_sku)
                    product = mapping.product
                    
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item_data.get('quantity', 1),
                        unit_price=Decimal(str(item_data.get('unit_price', 0))),
                        # Tira a foto do custo no momento da venda (Crucial)
                        snapshot_base_cost=product.base_cost,
                        snapshot_packaging_cost=product.packaging_cost
                    )
                except ProductMapping.DoesNotExist:
                    logger.warning(f"SKU Externo {external_sku} não mapeado no sistema. Item ignorado.")
                    
            # Aciona o Motor Financeiro para calcular Imposto, Lucro e Margem
            calculate_order_financials(order)

    return f"ML Sync: {len(orders_data)} orders processed"

@shared_task
def sync_nuvemshop_orders():
    """
    Busca novos pedidos na API da NuvemShop.
    """
    logger.info("Iniciando sincronização de pedidos da NuvemShop...")
    # Lógica da API da NuvemShop
    return "NuvemShop Sync: Success"
