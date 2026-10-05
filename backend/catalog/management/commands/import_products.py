import csv
import os
from decimal import Decimal
from django.core.management.base import BaseCommand
from catalog.models import Product, Marketplace, ProductMapping
from django.conf import settings

class Command(BaseCommand):
    help = 'Importa produtos e SKUs do De/Para a partir de uma planilha CSV para carga inicial.'

    def handle(self, *args, **options):
        csv_path = os.path.join(settings.BASE_DIR, 'produtos_homologacao.csv')
        
        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR(f"Arquivo {csv_path} não encontrado."))
            return

        self.stdout.write(self.style.WARNING("=== Iniciando Importação em Massa de Produtos ==="))
        
        # Garante que o Marketplace do ML existe para o mapeamento
        ml, _ = Marketplace.objects.get_or_create(name="Mercado Livre", is_active=True)
        
        importados = 0
        mapeados = 0

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                sku = row['sku'].strip()
                
                # Cria ou Atualiza o Produto
                product, created = Product.objects.update_or_create(
                    sku=sku,
                    defaults={
                        'name': row['nome'].strip(),
                        'base_cost': Decimal(row['custo_base']),
                        'packaging_cost': Decimal(row['custo_embalagem']),
                        'tax_percentage': Decimal(row['imposto']),
                        'stock_quantity': int(row['estoque'])
                    }
                )
                importados += 1
                
                # Verifica Mapeamento De/Para
                sku_ml = row.get('sku_mercado_livre', '').strip()
                if sku_ml:
                    ProductMapping.objects.update_or_create(
                        product=product,
                        marketplace=ml,
                        defaults={
                            'external_sku': sku_ml
                        }
                    )
                    mapeados += 1

        self.stdout.write(self.style.SUCCESS(f"[SUCESSO] Carga Inicial Finalizada!"))
        self.stdout.write(self.style.SUCCESS(f"-> {importados} produtos importados/atualizados."))
        self.stdout.write(self.style.SUCCESS(f"-> {mapeados} mapeamentos De/Para vinculados com sucesso ao Mercado Livre."))
