from django.db import models
from django.utils.translation import gettext_lazy as _

class CostCenter(models.Model):
    name = models.CharField(_('Nome do Centro de Custo'), max_length=100)
    description = models.TextField(_('Descrição'), blank=True, null=True)

    class Meta:
        verbose_name = _('Centro de Custo')
        verbose_name_plural = _('Centros de Custo')

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(_('Razão Social / Nome'), max_length=150)
    cnpj_cpf = models.CharField(_('CNPJ / CPF'), max_length=20, blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)
    phone = models.CharField(_('Telefone'), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _('Fornecedor')
        verbose_name_plural = _('Fornecedores')

    def __str__(self):
        return self.name

class Expense(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pendente')
        PAID = 'PAID', _('Pago')
        OVERDUE = 'OVERDUE', _('Atrasado')
        CANCELLED = 'CANCELLED', _('Cancelado')

    description = models.CharField(_('Descrição da Despesa'), max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Fornecedor'))
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Centro de Custo'))
    
    amount = models.DecimalField(_('Valor Total'), max_digits=10, decimal_places=2)
    due_date = models.DateField(_('Data de Vencimento'))
    payment_date = models.DateField(_('Data de Pagamento'), null=True, blank=True)
    
    status = models.CharField(_('Status'), max_length=15, choices=Status.choices, default=Status.PENDING)
    attachment = models.FileField(_('Comprovante/Boleto'), upload_to='expenses/attachments/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Conta a Pagar (Despesa)')
        verbose_name_plural = _('Contas a Pagar')

    def __str__(self):
        return f"{self.description} - R$ {self.amount}"

class Receivable(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pendente')
        RECEIVED = 'RECEIVED', _('Recebido')
        OVERDUE = 'OVERDUE', _('Atrasado')

    description = models.CharField(_('Descrição do Recebimento'), max_length=200)
    amount = models.DecimalField(_('Valor Total'), max_digits=10, decimal_places=2)
    expected_date = models.DateField(_('Data Prevista'))
    received_date = models.DateField(_('Data de Recebimento'), null=True, blank=True)
    
    status = models.CharField(_('Status'), max_length=15, choices=Status.choices, default=Status.PENDING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Conta a Receber')
        verbose_name_plural = _('Contas a Receber')

    def __str__(self):
        return f"{self.description} - R$ {self.amount}"

class BankTransaction(models.Model):
    """
    Transactions imported from OFX files for bank reconciliation.
    """
    transaction_id = models.CharField(_('ID da Transação (OFX)'), max_length=100, unique=True)
    date = models.DateField(_('Data da Transação'))
    amount = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2)
    memo = models.CharField(_('Descrição (Extrato)'), max_length=255)
    
    is_reconciled = models.BooleanField(_('Conciliado'), default=False)
    expense_linked = models.ForeignKey(Expense, on_delete=models.SET_NULL, null=True, blank=True, related_name='bank_transactions')
    receivable_linked = models.ForeignKey(Receivable, on_delete=models.SET_NULL, null=True, blank=True, related_name='bank_transactions')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Transação Bancária (OFX)')
        verbose_name_plural = _('Transações Bancárias (OFX)')

    def __str__(self):
        return f"{self.date} | {self.memo} | R$ {self.amount}"
