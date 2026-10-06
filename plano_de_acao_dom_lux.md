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

## 🎁 Etapa 5: Módulo Bônus - Contas a Pagar, Receber e Conciliação Bancária (Dias 61-70)
**Foco:** Gestão avançada de despesas, fluxo de caixa e fechamento financeiro (Oferecido como cortesia comercial).

* [ ] **Gestão de Despesas e Fornecedores:** Criar models no Django para cadastro de fornecedores, contas de consumo (água, luz, internet), folha de pagamento e impostos (Centros de Custo).
* [ ] **Anexos e Comprovantes:** Upload de arquivos PDF/Imagens (boletos e recibos) linkados diretamente à despesa para auditoria rápida.
* [ ] **Painel de Contas a Pagar/Receber:** Criar interface no React com visão de calendário, alertas de contas vencidas e projeção de pagamentos futuros (Fluxo de Caixa).
* [ ] **Motor de Conciliação Bancária (OFX):** Desenvolver script Python para ler extratos bancários no formato padrão OFX e realizar o "match" automático entre a saída de dinheiro e as contas registradas.
* [ ] **DRE Real (Lucro Líquido):** Integrar os custos operacionais (fixos e variáveis) com as vendas brutas importadas da Shopee/Mercado Livre/NuvemShop para calcular o verdadeiro Lucro Líquido do mês.

## 🌐 Etapa 6: Deploy Cloud e Treinamento (Dias 71-77)
**Foco:** Produção e Go-Live.

* [ ] Contratar VPS (DigitalOcean Droplet).
* [ ] Instalar Docker na VPS e configurar Nginx Reverso + Certbot SSL.
* [ ] Subir containers de produção (Postgres + Redis + Celery + Django + React/Vite estático).
* [ ] Entregar para a cliente e treinar os 4 usuários da base.
