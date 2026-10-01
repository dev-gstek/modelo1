# Plano de Ação: Plataforma Dom Lux Brindes

Este plano de ação foi desenhado para guiar o desenvolvimento do projeto ao longo dos **52 dias úteis**, garantindo entregas organizadas e validáveis. A arquitetura segue o padrão MVC do **Django** aliado ao **Celery** para filas assíncronas e **PostgreSQL**.

---

## 🚀 Fase 1: Infraestrutura e Base do Sistema (Dias 1-5)
**Foco:** Preparar o terreno, subir o servidor local e garantir a segurança. (Refere-se ao Módulo 5)

* [ ] **Setup do Ambiente:** Configurar `docker-compose.yml` contendo `web` (Django), `db` (PostgreSQL), `redis` (Broker) e `celery` (Worker).
* [ ] **Criação do Projeto:** `django-admin startproject domlux_core`.
* [ ] **Modelagem de Usuários (Módulo 5):** Estender o `AbstractUser` do Django para criar os perfis de acesso (Admin vs Operacional).
* [ ] **Autenticação:** Configurar tela de Login padrão e proteção de rotas (LoginRequiredMixin).
* [ ] **Setup de Frontend:** Escolher um template admin limpo e moderno (ex: Tailwind CSS ou Bootstrap 5 com tema AdminLTE/Tabler) para focar no back-end.

---

## 📦 Fase 2: Gestão Inteligente de Custos e SKUs (Dias 6-15)
**Foco:** O "Cérebro" financeiro. O sistema precisa conhecer os produtos antes de vender. (Refere-se ao Módulo 2)

* [ ] **Modelagem de Produtos:** Criar app `catalog` e o model `Product` (Nome, SKU Interno, Custo Base, Custo Embalagem, % Imposto).
* [ ] **Telas de CRUD:** Construir telas para listar, criar, editar e excluir produtos.
* [ ] **Modelagem de Integrações:** Criar model `Marketplace` (Nome, Chaves de API).
* [ ] **Ferramenta de De/Para (Crucial):** Criar model `ProductMapping` que relaciona o `Product` interno com o `External_ID` e `External_SKU` de cada marketplace.
* [ ] **Interface do De/Para:** Tela onde a cliente informa "A Caneca Mágica na Shopee tem o código 12345 e equivale ao nosso SKU CAN-01".

---

## 🤖 Fase 3: Motor de Captação de Pedidos (Dias 16-30)
**Foco:** A automação que aposenta as planilhas. (Refere-se ao Módulo 1)

* [ ] **Autenticação de APIs:** Desenvolver fluxos OAuth 2.0 para salvar e renovar tokens do **Mercado Livre** e **NuvemShop**, e configuração de App Key da **Shopee**.
* [ ] **Modelagem de Pedidos:** Criar app `orders` com models `Order` (Status, Cliente, Data, Canal, Total, Taxas, Frete) e `OrderItem`.
* [ ] **Workers de Sincronização (Celery):** Escrever as *tasks* (ex: `fetch_ml_orders`, `fetch_shopee_orders`) rodando a cada X minutos.
* [ ] **Tratamento de Dados:** Normalizar a resposta em JSON das 3 APIs para o padrão do nosso banco de dados. (Ex: Pegar `transaction_amount` e `shipping_cost`).
* [ ] **Lançamento Manual:** Criar formulário rápido para cadastrar vendas de **WhatsApp/Instagram**.

---

## 🔄 Fase 4: Estoque Inteligente e Multicanal (Dias 31-37)
**Foco:** Evitar furos de estoque. (Refere-se ao Módulo 3)

* [ ] **Controle de Saldo:** Adicionar campo `stock_quantity` ao model `Product`.
* [ ] **Gatilho de Baixa (Inbound):** Configurar *Signals* no Django. Assim que um `Order` for salvo no banco, descontar o estoque dos produtos correspondentes.
* [ ] **Gatilho de Sincronização (Outbound):** Assim que o estoque interno mudar, disparar task no Celery para avisar as plataformas:
  * [ ] API ML (`PUT /items/{id}`)
  * [ ] API Shopee (`UpdateStock`)
  * [ ] API NuvemShop (`PUT /products/{id}/variants/{id}`)

---

## 💰 Fase 5: Inteligência Financeira e Dashboard (Dias 38-52)
**Foco:** Entregar o valor real do sistema para a cliente. (Refere-se ao Módulo 4)

* [ ] **Engine de Cálculo (DRE por pedido):** Desenvolver lógica no backend que, após receber o pedido, calcula:
  * `Lucro Bruto` = Venda - (Taxas Plataforma + Frete Seller)
  * `Custo Total` = (Custo Base do Produto + Embalagem) * Quantidade
  * `Imposto` = Venda * % Imposto do Produto
  * `Lucro Líquido` = Lucro Bruto - Custo Total - Imposto
  * `Margem %` = (Lucro Líquido / Venda) * 100
* [ ] **Tabela Mágica:** Criar a View que exibe a tabela com as 12 colunas exatas exigidas pela cliente.
* [ ] **Dashboard:** Consolidar os dados mensais e exibir em gráficos dinâmicos (Chart.js): Lucro por Canal, Produtos mais rentáveis, Faturamento Total.
* [ ] **Filtros de Permissão:** Garantir que o usuário "Operacional" veja a tabela sem as colunas de "Custo" e "Lucro".

---

## 🛡️ Fase 6: Homologação e Deploy (Dias Finais)
* [ ] **Ambiente Sandbox:** Testar geração de vendas fake e verificar o cálculo das taxas.
* [ ] **Deploy de Produção:** Subir a stack completa para uma VPS (DigitalOcean / AWS).
* [ ] **Configuração SSL/HTTPS:** Para garantir a segurança das integrações (APIs exigem HTTPS).
* [ ] **Treinamento e Entrega:** Validar com a Dom Lux e iniciar o monitoramento de logs.
