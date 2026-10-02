from decimal import Decimal
from .models import Order

def calculate_order_financials(order: Order):
    """
    Motor Financeiro: Recebe um pedido e recalcula toda a matemática da DRE.
    """
    total_product_cost = Decimal('0.00')
    total_tax = Decimal('0.00')

    # Soma os custos capturando as "fotos" (snapshots) tiradas no momento da venda
    for item in order.items.all():
        item_base_cost = item.snapshot_base_cost or Decimal('0.00')
        item_pkg_cost = item.snapshot_packaging_cost or Decimal('0.00')
        
        # Custo do Produto = (Base + Embalagem) * Quantidade
        total_product_cost += (item_base_cost + item_pkg_cost) * item.quantity
        
        # Imposto = (Proporção da venda do item) * % Imposto do Produto
        # Simplificação: aplica a % sobre o valor bruto rateado ou unitário.
        tax_pct = item.product.tax_percentage / Decimal('100.00')
        item_gross_value = item.unit_price * item.quantity
        total_tax += item_gross_value * tax_pct

    # Cálculo do Caixa (Gross Profit)
    # Caixa = Venda - Taxas da Plataforma - Frete Pago pelo Seller
    caixa_gerado = order.total_amount - order.marketplace_fee - order.shipping_cost

    # Cálculo do Lucro Líquido
    net_profit = caixa_gerado - total_product_cost - total_tax

    # Cálculo da Margem (%)
    if order.total_amount > 0:
        profit_margin = (net_profit / order.total_amount) * Decimal('100.00')
    else:
        profit_margin = Decimal('0.00')

    # Salva no banco
    order.total_product_cost = total_product_cost
    order.calculated_tax = total_tax
    order.net_profit = net_profit
    order.profit_margin = profit_margin
    
    # Obs: Salvamos passando update_fields para evitar gatilhos infinitos caso existam signals no Order
    order.save(update_fields=['total_product_cost', 'calculated_tax', 'net_profit', 'profit_margin'])

    return order
