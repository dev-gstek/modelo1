from django.core.management.base import BaseCommand
from unittest.mock import patch
from catalog.models import Product, Marketplace, ProductMapping
from orders.tasks import sync_mercadolivre_orders
from orders.models import Order
from decimal import Decimal
import datetime

class Command(BaseCommand):
    help = 'Roda o fluxo de integração do ML em modo Sandbox (Dados Falsos) para testar a Matemática.'

    @patch('orders.tasks.MercadoLivreClient.fetch_recent_orders')
    def handle(self, mock_fetch, *args, **options):
        self.stdout.write(self.style.WARNING("=== Iniciando Homologação Sandbox ==="))

        # 1. Prepara Banco de Dados Fake
        ml, _ = Marketplace.objects.get_or_create(name="Mercado Livre", is_active=True)
        produto, _ = Product.objects.get_or_create(
            sku="CAN-MAG-01",
            defaults={
                'name': "Caneca Mágica Homologação",
                'base_cost': Decimal('10.00'),
                'packaging_cost': Decimal('2.00'),
                'tax_percentage': Decimal('6.00'), # 6% Simples Nacional
                'stock_quantity': 100
            }
        )
        ProductMapping.objects.get_or_create(
            product=produto,
            marketplace=ml,
            external_sku="MLB-CAN-999"
        )

        # 2. Mock do Payload da API do Mercado Livre
        fake_payload = [
            {
                "id": f"SANDBOX-{int(datetime.datetime.now().timestamp())}",
                "date_created": datetime.datetime.now().isoformat(),
                "total_amount": 100.00,
                "shipping_cost": 15.00, # Frete pago pelo vendedor
                "buyer": {"first_name": "Cliente Sandbox da Silva"},
                "order_items": [
                    {
                        "item": {"seller_sku": "MLB-CAN-999"},
                        "quantity": 2, # Comprou 2 canecas
                        "unit_price": 50.00,
                        "sale_fee": 16.00 # 16% de comissão do ML
                    }
                ]
            }
        ]

        # Injeta o payload falso no client
        mock_fetch.return_value = fake_payload

        self.stdout.write(self.style.SUCCESS("[1/3] Banco de dados preparado e Payload Mockado."))
        
        # 3. Roda a Task do Celery como se fosse real
        self.stdout.write(self.style.WARNING("[2/3] Rodando Motor de Sincronização..."))
        resultado = sync_mercadolivre_orders()
        self.stdout.write(self.style.SUCCESS(f"Resultado da Task: {resultado}"))

        # 4. Verifica a Matemática
        order = Order.objects.order_by('-created_at').first()
        self.stdout.write(self.style.WARNING("\n=== DRE CALCULADA PELO MOTOR ==="))
        self.stdout.write(f"Venda Bruta: R$ {order.total_amount}")
        self.stdout.write(f"Comissão ML: R$ {order.marketplace_fee}")
        self.stdout.write(f"Frete Seller: R$ {order.shipping_cost}")
        self.stdout.write(f"Custo Prod (2x12): R$ {order.total_product_cost}")
        self.stdout.write(f"Imposto (6%): R$ {order.calculated_tax}")
        self.stdout.write(self.style.SUCCESS(f"--> LUCRO LÍQUIDO: R$ {order.net_profit}"))
        self.stdout.write(self.style.SUCCESS(f"--> MARGEM: {order.profit_margin}%"))
        
        # Verifica Estoque
        produto.refresh_from_db()
        self.stdout.write(self.style.SUCCESS(f"--> ESTOQUE RESTANTE: {produto.stock_quantity} unidades"))
