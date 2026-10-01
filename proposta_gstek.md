# PROPOSTA DE DESENVOLVIMENTO
## Plataforma de Gestão Unificada e Motor Financeiro

**GSTek - ENGENHARIA DE SOFTWARE CORPORATIVO**

| | |
|---|---|
| **Cliente** | Dom Lux Brindes |
| **Consultoria** | GSTek - Engenharia de Software Corporativo |
| **Stack Tecnológico** | Python, Django, PostgreSQL, Celery e Docker |

---

### Proposta Comercial • Desenvolvimento sob medida

## 1. O Problema Atual
Hoje, a Dom Lux Brindes precisa consolidar informações de diferentes canais de venda para obter uma visão financeira única do negócio. A utilização de relatórios separados e planilhas exige conferências manuais, aumenta o tempo operacional e dificulta a visualização do resultado real por produto, pedido e canal.

O cenário envolve aproximadamente 500 SKUs e a necessidade de cruzar informações de venda, custos, impostos, taxas, fretes, caixa, lucro e margem de contribuição.

## 2. A Solução Proposta
A GSTek propõe o desenvolvimento de uma Plataforma de Gestão Multicanal sob medida, centralizando a operação e automatizando a captura de pedidos e os cálculos financeiros.

A plataforma será estruturada para receber dados das principais plataformas de venda, manter uma base central de produtos e custos, controlar estoque e transformar os dados operacionais em indicadores financeiros unificados.

## 3. Escopo Funcional da Plataforma

**Módulo 1 — Motor de Captação de Pedidos e Automação**
* Integração por APIs oficiais com Mercado Livre, Shopee e NuvemShop.
* Rotinas de sincronização automáticas, com processamento em background utilizando Celery.
* Importação contínua dos pedidos e respectivas informações disponibilizadas pelas plataformas.
* Lançamento manual de vendas realizadas por canais sociais, como WhatsApp e Instagram.
* Centralização dos pedidos em uma única interface.

**Módulo 2 — Gestão Inteligente de Custos e SKUs**
* Cadastro unificado dos aproximadamente 500 SKUs.
* Cadastro de Custo Base e Custo de Embalagem por produto.
* Configuração de Imposto Individual (%).
* Cadastro e aplicação das taxas e comissões relevantes de cada plataforma.
* Tela de De/Para para vincular códigos externos das plataformas ao produto interno.
* Estrutura preparada para evolução futura da matriz de custos.

**Módulo 3 — Estoque Inteligente e Multicanal**
* Controle de estoque centralizado.
* Baixa automática após a confirmação de venda.
* Sincronização do saldo disponível com os canais conectados, conforme recursos permitidos por cada API.
* Redução do risco de venda de produtos sem disponibilidade.
* Visão unificada do estoque por produto e canal.

**Módulo 4 — Inteligência Financeira e Dashboard**
* Cálculo automatizado do resultado por pedido e produto.
* Visão financeira baseada em Venda, Taxas, Fretes, Impostos, Custos, Caixa, Lucro e Margem.
* Relatório com 12 indicadores/colunas: ID, Data, Cliente, Nº Pedido, Produto, Custo, Valor Venda, Imposto, Caixa, Lucro, % de Lucro e Margem de Contribuição.
* Dashboard consolidado por período e canal.
* Consolidação de Mercado Livre, Shopee, NuvemShop e vendas sociais.

**Módulo 5 — Controle de Acesso e Usuários**
* Sistema de autenticação e permissões.
* Até 4 usuários na configuração inicial.
* Separação de permissões por perfil.
* Possibilidade de restringir informações financeiras sensíveis conforme o perfil do usuário.

## 4. Matriz de Viabilidade de Integração das APIs

A análise técnica considera os recursos públicos e os modelos de autenticação das plataformas. A disponibilidade efetiva de determinados campos, taxas, dados financeiros e permissões depende da conta, aplicativo aprovado e regras vigentes de cada plataforma.

| Plataforma | Viabilidade | Autenticação / Integração | Dados e Observações |
|---|---|---|---|
| **Mercado Livre** | Muito alta | OAuth 2.0; APIs de pedidos e integração com Mercado Pago. | Pedidos via Orders API; informações de tarifas e fretes conforme dados disponibilizados; recebimentos integrados pelo MP. |
| **Shopee** | Alta | App Key / credenciais e aprovação do aplicativo. | Pedidos via endpoints da plataforma; dados de comissões, frete e vouchers conforme disponibilidade da API. |
| **NuvemShop** | Muito alta | OAuth 2.0. | Pedidos, itens e fretes. Taxas de cartão dependem do gateway/meio de pagamento utilizado. |

**Conclusão técnica**
A arquitetura proposta é tecnicamente viável para unificar os dados das plataformas, desde que as contas e aplicações tenham as permissões necessárias e que os campos utilizados estejam disponíveis nas APIs vigentes.
* O valor de venda é obtido da plataforma; os custos internos serão mantidos na base da Dom Lux.
* O sistema fará a composição do resultado a partir de venda, taxas, fretes, impostos e custos cadastrados.
* O mapeamento De/Para permitirá relacionar SKUs externos, como códigos de anúncios, aos produtos internos.
* Dados pessoais disponibilizados pelas plataformas serão tratados conforme as permissões e limitações de cada API.

## 5. Arquitetura e Tecnologia

| Componente | Tecnologia / Abordagem |
|---|---|
| Backend | Python + Django |
| Banco de Dados | PostgreSQL |
| Processamento assíncrono | Celery + rotinas em background |
| Infraestrutura | Docker + ambiente Cloud |
| Integrações | APIs oficiais das plataformas |
| Interface | Painel web responsivo |
| Segurança | Autenticação, permissões por usuário e proteção de rotas |

## 6. Escopo Opcional — Evoluções Futuras
* **Contas a Pagar, Receber e Conciliação Bancária:** Gestão de despesas, fornecedores, boletos e importação de extratos OFX para conciliação e fechamento de caixa.
* **Esteira de Produção:** Kanban para acompanhamento de produtos personalizados, etapas de produção e anexos de artes aprovadas.

---

## 7. Investimento em Desenvolvimento

O investimento abaixo contempla a arquitetura, desenvolvimento do backend em Python/Django, integrações, rotinas de sincronização, banco de dados, painel e infraestrutura base descritos neste escopo.

| Módulo / Etapa | Prazo (Est.) | Escopo resumido | Valor (R$) |
|---|---|---|---|
| **1. Motor de Integração de Pedidos** | 15 dias | Robôs sincronizadores e rotinas background (Celery) para ML, Shopee e NuvemShop. | R$ 5.800,00 |
| **2. Gestão de Custos e SKUs** | 10 dias | Produtos, custos, embalagem, imposto individual, taxas e ferramenta de De/Para. | R$ 3.500,00 |
| **3. Inteligência Financeira e Painel** | 15 dias | Núcleo financeiro, cálculo de resultado, 12 colunas e dashboard unificado. | R$ 4.200,00 |
| **4. Estoque Inteligente e Multicanal** | 07 dias | Baixa automática e sincronização de saldo nos canais conectados. | R$ 2.500,00 |
| **5. Segurança e Infraestrutura Base** | 05 dias | Docker/PostgreSQL, login, permissões de 4 usuários e proteção de rotas. | R$ 2.500,00 |

**INVESTIMENTO TOTAL DO PROJETO BASE:** R$ 18.500,00

## 8. Módulos Opcionais — Orçamento Futuro
Os módulos abaixo não fazem parte do investimento do projeto base e poderão ser contratados posteriormente.

| Módulo | Prazo (Est.) | Descrição | Valor (R$) |
|---|---|---|---|
| Contas a Pagar, Receber e Conciliação | 15 dias | Gestão de despesas, fornecedores, boletos e importação automática de OFX. | R$ 4.500,00 |

## 9. Condições de Pagamento
* **Entrada** — 30% no ato do contrato: R$ 5.550,00.
* **Homologação** — 30% na entrega da Fase 1: R$ 5.550,00.
* **Entrega Final** — 40% na entrega oficial e treinamento: R$ 7.400,00.

## 10. Manutenção, Hospedagem e Suporte Pós-Entrega
Hospedagem em Servidor Cloud e manutenção da infraestrutura/banco de dados, incluindo apoio técnico para eventuais atualizações de chaves, credenciais e configurações necessárias às integrações.
* **Valor mensal:** R$ 450,00
* A cobrança inicia após o 1º mês de operação livre.

## 11. Cronograma e Premissas
* **Prazo estimado total:** 52 dias úteis.
* O prazo inicia após a assinatura do contrato, aprovação do escopo e disponibilização das credenciais/chaves necessárias para as integrações.
* O cronograma poderá ser ajustado caso alguma plataforma exija aprovação, homologação, revisão de permissões ou alteração de requisitos de API.
* A volumetria média de pedidos/mês será utilizada para dimensionamento adequado do ambiente Cloud.
* A implantação contempla os recursos descritos no escopo desta proposta.

## 12. Próximos Passos
1. Aprovação da arquitetura e do escopo inicial.
2. Definição da volumetria média de pedidos por mês.
3. Liberação das contas, acessos e credenciais necessárias às integrações.
4. Assinatura do contrato e início do desenvolvimento.
5. Homologação progressiva dos módulos e entrega final com treinamento.

---

### Resumo Executivo

**INVESTIMENTO BASE:** R$ 18.500,00  
**PRAZO ESTIMADO:** 52 dias úteis  
**MANUTENÇÃO / SERVIDOR:** R$ 450,00/mês após o 1º mês de operação livre  

*Validade da proposta: 15 dias.*  
**GSTek - Engenharia de Software**
