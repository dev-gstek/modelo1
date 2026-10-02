from django.db import models

class Product(models.fields.Field):
    pass # Wait, I shouldn't inherit from Field, let me fix this in the next replacement or just provide the right code directly.

# Re-writing the models.py correctly
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do Produto")
    sku = models.CharField(max_length=100, unique=True, verbose_name="SKU Interno")
    base_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Custo Base")
    packaging_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Custo de Embalagem")
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Imposto (%)")
    stock_quantity = models.IntegerField(default=0, verbose_name="Estoque Disponível")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.sku}] {self.name}"

    class Meta:
        verbose_name = "Produto Interno"
        verbose_name_plural = "Produtos Internos"


class Marketplace(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Plataforma")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    api_credentials = models.JSONField(blank=True, null=True, verbose_name="Credenciais de API")

    def __str__(self):
        return self.name


class ProductMapping(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="mappings", verbose_name="Produto Interno")
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE, verbose_name="Marketplace")
    external_sku = models.CharField(max_length=100, blank=True, null=True, verbose_name="SKU Externo (Ex: Código Anúncio ML)")
    external_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Externo (Platform Item ID)")

    class Meta:
        verbose_name = "De/Para de SKU"
        verbose_name_plural = "Mapeamentos De/Para"
        unique_together = ('marketplace', 'external_id')

    def __str__(self):
        return f"{self.marketplace.name} -> {self.product.sku} ({self.external_sku or self.external_id})"
