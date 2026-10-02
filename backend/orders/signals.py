from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def deduct_stock_on_order(sender, instance, created, **kwargs):
    """
    (Inbound) - Quando um pedido cai no sistema e o item é salvo,
    desconta automaticamente a quantidade comprada do estoque do Produto.
    Isso vai engatilhar o Signal do Catalog que avisará os outros canais.
    """
    if created:
        with transaction.atomic():
            product = instance.product
            product.stock_quantity -= instance.quantity
            product.save()
