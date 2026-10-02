from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .tasks import push_stock_mercadolivre, push_stock_shopee, push_stock_nuvemshop

@receiver(post_save, sender=Product)
def sync_stock_to_marketplaces(sender, instance, created, **kwargs):
    """
    Sempre que o saldo de um Produto mudar, este signal dispara
    tarefas em background para avisar todas as plataformas conectadas.
    """
    # Em produção, usaremos um tracker para verificar se o campo stock_quantity realmente mudou.
    # Dispara atualização para os canais
    push_stock_mercadolivre.delay(instance.id, instance.stock_quantity)
    push_stock_shopee.delay(instance.id, instance.stock_quantity)
    push_stock_nuvemshop.delay(instance.id, instance.stock_quantity)
