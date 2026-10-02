from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('snapshot_base_cost', 'snapshot_packaging_cost')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('external_order_id', 'marketplace', 'customer_name', 'status', 'total_amount', 'net_profit', 'profit_margin', 'order_date')
    list_filter = ('marketplace', 'status', 'order_date')
    search_fields = ('external_order_id', 'customer_name')
    readonly_fields = ('calculated_tax', 'total_product_cost', 'net_profit', 'profit_margin')
    inlines = [OrderItemInline]
    date_hierarchy = 'order_date'

    fieldsets = (
        ('Informações da Venda', {
            'fields': ('marketplace', 'external_order_id', 'customer_name', 'order_date', 'status')
        }),
        ('Valores da Plataforma', {
            'fields': ('total_amount', 'shipping_cost', 'marketplace_fee')
        }),
        ('Inteligência Financeira (Calculado)', {
            'fields': ('total_product_cost', 'calculated_tax', 'net_profit', 'profit_margin'),
            'classes': ('collapse',)
        }),
    )
