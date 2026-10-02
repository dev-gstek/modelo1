from django.apps import AppConfig

class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Catálogo e Estoque'

    def ready(self):
        import catalog.signals
