from django.db import models
from catalog.models import Marketplace, Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendente'),
        ('paid', 'Pago'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregue'),
        ('canceled', 'Cancelado'),
    )

    marketplace = models.ForeignKey(Marketplace, on_delete=models.SET_NULL, null=True, verbose_name="Canal de Venda")
    external_order_id = models.CharField(max_length=100, unique=True, verbose_name="ID do Pedido na Plataforma")
    customer_name = models.CharField(max_length=255, verbose_name="Nome do Cliente")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    
    # Valores Brutos (Puxados da API)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Valor Bruto da Venda")
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Custo de Frete (Seller)")
    marketplace_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Taxa da Plataforma")

    # Valores Calculados (Inteligência Financeira)
    calculated_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Imposto Calculado (R$)")
    total_product_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Custo Total dos Produtos")
    net_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Lucro Líquido")
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Margem (%)")

    order_date = models.DateTimeField(verbose_name="Data do Pedido")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-order_date']

    def __str__(self):
        return f"Pedido {self.external_order_id} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produto")
    quantity = models.IntegerField(default=1, verbose_name="Quantidade")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário")
    
    # Snapshots (Tira a foto do custo do produto no exato momento da venda)
    snapshot_base_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Custo Base (No momento da venda)")
    snapshot_packaging_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Custo Embalagem (No momento da venda)")

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"

    def __str__(self):
        return f"{self.quantity}x {self.product.name} (Pedido {self.order.external_order_id})"
