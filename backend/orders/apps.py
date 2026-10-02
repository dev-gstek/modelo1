from django.apps import AppConfig

class OrdersConfig(AppConfig):
    name = 'orders'
    verbose_name = 'Motor de Pedidos'

    def ready(self):
        import orders.signals
