# Plano de Ação Oficial (Revisado - Pós Estruturação)

## Status Atual: Arquitetura Core Concluída 🟢
Nós aceleramos a esteira de desenvolvimento e construímos toda a base arquitetural em tempo recorde. 
**O que já está pronto no repositório:**
* **Infra:** Docker Compose (Django, PostgreSQL, Redis, Celery).
* **Segurança:** Custom User Model com permissões de Admin/Operacional.
* **Catálogo:** Models de Produtos, Custos e a Ferramenta Relacional "De/Para" de SKUs.
* **Estoque (Inteligência):** Signals configurados para baixar estoque via Inbound e notificar via Outbound.
* **Inteligência Financeira:** Serviço matemático de DRE, geração das 12 Colunas via Serializer e endpoint de API REST (`/api/v1/dashboard/financials/`).

---

Como a "espinha dorsal" já existe, o nosso cronograma de **77 dias úteis** agora será totalmente dedicado a conectar fios reais, front-end e integrações diretas com os marketplaces.

## 🖥️ Fase 1: Interface do Usuário (Dias 1-15)
**Foco:** Ligar o visual incrível (mockups) aos dados reais do banco de dados.

* [ ] **Dashboard Dinâmico:** Conectar a tela `demo_dashboard.html` ao endpoint da API para que os gráficos do Chart.js sejam renderizados baseados nos pedidos gravados.
* [ ] **Tabela Financeira:** Conectar a tabela mágica de 12 colunas da tela `demo_sistema.html` com o backend.
* [ ] **Telas de Cadastro:** Desenvolver (ou adaptar no Django Admin) uma interface amigável para a cliente cadastrar o Custo Base, Embalagem e Mapeamento De/Para.

## 🔐 Fase 2: Conexões OAuth e Segurança de Chaves (Dias 16-30)
**Foco:** Estabelecer o elo de confiança entre o nosso sistema e os Marketplaces. *(Depende da assinatura do contrato).*

* [ ] **App Mercado Livre:** Criar o aplicativo no DevCenter, gerar `client_id`, `client_secret` e programar a rotina para atualizar o Token de 6 em 6 horas.
* [ ] **App NuvemShop:** Criar o fluxo de autenticação OAuth 2.0 e capturar o Access Token.
* [ ] **App Shopee:** Configurar Partner ID, Shop ID e rotinas de assinatura HMAC (exigência da API deles).
* [ ] **Criptografia:** Garantir que os tokens sejam salvos de forma segura no banco (JSONField encriptado).

## 🤖 Fase 3: Robôs Inbound (Puxando Pedidos Reais) (Dias 31-50)
**Foco:** Dar vida às funções vazias do Celery.

* [ ] **Mercado Livre:** Refatorar a task `sync_mercadolivre_orders` para disparar um GET na `/orders/search`, ler o JSON, aplicar a regra de "De/Para" do SKU e salvar no nosso banco.
* [ ] **Shopee & NuvemShop:** Criar o mesmo fluxo de varredura para os outros dois canais.
* [ ] **Homologação Matemática:** Validar se o nosso Motor Financeiro (`services.py`) está batendo centavo por centavo com a taxa de frete e comissão que a API mandou.

## 📦 Fase 4: Webhooks e Outbound de Estoque (Dias 51-65)
**Foco:** O sistema trabalhando passivamente.

* [ ] **Endpoint de Webhooks (ML):** Criar uma rota no Django (`/api/webhooks/mercadolivre/`) para receber alertas imediatos quando uma venda acontecer (sem precisar esperar o Celery).
* [ ] **Baixa de Estoque Real (Outbound):** Escrever os códigos `PUT` dentro das tasks `push_stock_mercadolivre` (e afins) para mandar o saldo atualizado de volta para os marketplaces.

## 🚀 Fase 5: Testes de Carga, Deploy e Treinamento (Dias 66-77)
**Foco:** Tirar da máquina local e colocar na nuvem (Produção).

* [ ] **Testes de Carga:** Simular a entrada de 5.000 pedidos/mês para garantir que o Celery e o Postgres aguentam sem enfileirar infinitamente.
* [ ] **Deploy Cloud:** Subir o `docker-compose.yml` para uma VPS (Ex: DigitalOcean Droplet, AWS EC2 ou Linode).
* [ ] **SSL (HTTPS):** Configurar Nginx + Certbot Let's Encrypt para segurança máxima.
* [ ] **Entrega Final:** Treinar os 4 usuários da Dom Lux Brindes a operarem o sistema.
