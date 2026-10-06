from django.contrib import admin
from .models import CostCenter, Supplier, Expense, Receivable, BankTransaction

@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj_cpf', 'email', 'phone')
    search_fields = ('name', 'cnpj_cpf')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'supplier', 'cost_center', 'amount', 'due_date', 'status')
    list_filter = ('status', 'due_date', 'cost_center')
    search_fields = ('description', 'supplier__name')
    date_hierarchy = 'due_date'

@admin.register(Receivable)
class ReceivableAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'expected_date', 'status')
    list_filter = ('status', 'expected_date')
    search_fields = ('description',)
    date_hierarchy = 'expected_date'

@admin.register(BankTransaction)
class BankTransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'memo', 'amount', 'is_reconciled')
    list_filter = ('is_reconciled', 'date')
    search_fields = ('memo', 'transaction_id')
    date_hierarchy = 'date'
