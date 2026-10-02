from rest_framework import serializers
from .models import Order

class FinancialDashboardSerializer(serializers.ModelSerializer):
    canal = serializers.CharField(source='marketplace.name', read_only=True)
    produto_str = serializers.SerializerMethodField()
    caixa = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 
            'order_date', 
            'customer_name', 
            'external_order_id', 
            'produto_str', 
            'total_product_cost', 
            'total_amount', 
            'calculated_tax', 
            'caixa', 
            'net_profit', 
            'profit_margin'
        ]

    def get_produto_str(self, obj):
        # Retorna os itens do pedido concatenados
        items = obj.items.all()
        return ", ".join([f"{item.quantity}x {item.product.sku}" for item in items])

    def get_caixa(self, obj):
        # Caixa Gerado = Total - Taxas - Frete
        return obj.total_amount - obj.marketplace_fee - obj.shipping_cost
