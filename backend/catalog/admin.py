from django.contrib import admin
from .models import Product, Marketplace, ProductMapping

class ProductMappingInline(admin.TabularInline):
    model = ProductMapping
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'base_cost', 'packaging_cost', 'tax_percentage', 'stock_quantity')
    search_fields = ('sku', 'name')
    inlines = [ProductMappingInline]

@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)

@admin.register(ProductMapping)
class ProductMappingAdmin(admin.ModelAdmin):
    list_display = ('product', 'marketplace', 'external_sku', 'external_id')
    list_filter = ('marketplace',)
    search_fields = ('product__sku', 'external_sku', 'external_id')
