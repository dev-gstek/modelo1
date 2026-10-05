# Plano de Ação Oficial - Status de Homologação (Dom Lux Brindes)

## Panorama Executivo: Conclusão Antecipada 🏆
Através de engenharia agressiva, nós finalizamos a **arquitetura primária** e a **engenharia de integração** das Fases 1 a 5 do projeto antes mesmo da assinatura do contrato. 

A "Espinha Dorsal" SaaS está criada:
- **Backend (Django REST + Celery):** Modelagem financeira, sistema de permissões, "De/Para" de SKUs, OAuth 2.0 (ML), cálculo de DRE e Signals de estoque concluídos.
- **Frontend (React + Vite):** Interface SPA com o layout Vanilla aprovado, gráficos de BI e roteamento configurados.

Como a programação bruta do núcleo foi abstraída, os **77 dias úteis** previstos no orçamento serão utilizados de forma extremamente cirúrgica para testes de carga, ajustes refinados e entrega premium.

---

## 🔌 Etapa 1: "Data Binding" (Conexão Front e Back) (Dias 1-10)
**Foco:** Ligar as pontas soltas locais.

* [x] Configurar CORS no Django `settings.py` para aceitar conexões do React (`localhost:5173`).
* [x] Refatorar os componentes `Dashboard.jsx` e `FinanceTable.jsx` do React para remover os "dados mockados" e passar a usar `fetch()` para consumir a nossa rota `/api/v1/dashboard/financials/`.
* [x] Garantir que os gráficos do Chart.js processem corretamente as somatórias de Caixa e Lucro devolvidas pela API.

## 🔑 Etapa 2: Homologação de APIs (Sandbox e Keys) (Dias 11-30)
**Foco:** Testar as integrações com os sistemas terceiros em modo Sandbox. *(Depende do Cliente)*.

* [x] Pegar o App Key, Client Secret, Shop ID e Partner ID do cliente (Shopee, ML e NuvemShop) e imputar no Django Admin.
* [x] Rodar os `sync_tasks` manualmente usando um pedido falso para confirmar que a criptografia OAuth e HMAC-SHA256 da Shopee não está quebrando.
* [ ] Testar a renovação do Token do ML após 6 horas.

## 🕸️ Etapa 3: Webhooks e Concorrência (Dias 31-45)
**Foco:** Ajustes finos de tempo real.

* [x] Criar endpoint POST `/api/webhooks/mercadolivre/` para receber o "ping" do ML informando que uma venda aconteceu, tirando a necessidade do Celery consultar o ML de 5 em 5 minutos.
* [x] Escrever o código real de PUT na API da Shopee/ML dentro das tasks do Celery `push_stock_` para dar a baixa do estoque no outbound.

## 💣 Etapa 4: Carga de Dados Iniciais (Dias 46-60)
**Foco:** Preparar a base para o lançamento.

* [x] Usar um script Python para importar os 500 SKUs da planilha da cliente para dentro do model `Product` (Nome, Custo, Embalagem, Imposto).
* [x] Mapear o "De/Para" de pelo menos os 50 produtos mais vendidos para garantir a prova de conceito e a precisão do cálculo da DRE nos primeiros dias.

## 🌐 Etapa 5: Deploy Cloud e Treinamento (Dias 61-77)
**Foco:** Produção e Go-Live.

* [ ] Contratar VPS (DigitalOcean Droplet).
* [ ] Instalar Docker na VPS e configurar Nginx Reverso + Certbot SSL.
* [ ] Subir containers de produção (Postgres + Redis + Celery + Django + React/Vite estático).
* [ ] Entregar para a cliente e treinar os 4 usuários da base.
