from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def sync_mercadolivre_orders():
    """
    Task executada pelo Celery Beat a cada X minutos.
    Busca novos pedidos na API do Mercado Livre (Orders API).
    """
    logger.info("Iniciando sincronização de pedidos do Mercado Livre...")
    # Aqui entrará o script de OAuth e fetch na API do ML na Fase 3
    # 1. Puxar /orders/search?seller_id={id}
    # 2. Iterar sobre os resultados
    # 3. Converter SKU externo para interno
    # 4. Salvar model Order
    return "ML Sync: Success"

@shared_task
def sync_shopee_orders():
    """
    Busca novos pedidos na API da Shopee.
    """
    logger.info("Iniciando sincronização de pedidos da Shopee...")
    # Lógica da API da Shopee
    return "Shopee Sync: Success"

@shared_task
def sync_nuvemshop_orders():
    """
    Busca novos pedidos na API da NuvemShop.
    """
    logger.info("Iniciando sincronização de pedidos da NuvemShop...")
    # Lógica da API da NuvemShop
    return "NuvemShop Sync: Success"
