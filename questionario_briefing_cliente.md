# Documento de Briefing: Plataforma de Gestão Multicanal
**Cliente:** [Nome da Empresa / Cliente]
**Data da Reunião:** ___/___/20__
**Objetivo:** Levantar o escopo técnico e de negócios para unificar a gestão de vendas (Shopee, Mercado Livre, Nuvemshop, WhatsApp/Insta), financeiro, estoque e produção.

---

## 📦 1. Volume e Operação Básica

**1.1. Qual é a média de pedidos mensais somando todos os canais de venda?**
> *Anotações:* 


**1.2. Quantos SKUs (produtos únicos) vocês têm cadastrados hoje, considerando as variações (tamanho, cor, etc.)?**
> *Anotações:* 


**1.3. Vocês já utilizam algum sistema de gestão (ERP como Bling, Tiny) ou controlam tudo em planilhas?**
> *Anotações:* 


**1.4. Como é feita a emissão de notas fiscais (NF-e / NFC-e) hoje?** 
*(O novo sistema precisará emitir as notas diretamente ou vai integrar com um ERP existente?)*
> *Anotações:* 


---

## 🔄 2. Integrações e Canais de Venda

**2.1. Mercado Livre, Shopee e Nuvemshop: Vocês possuem apenas uma conta em cada, ou gerenciam múltiplas contas/CNPJs nas plataformas?**
> *Anotações:* 


**2.2. WhatsApp e Instagram: A ideia é apenas registrar essas vendas manualmente no sistema, ou vocês esperam alguma automação (ex: bot no WhatsApp que já cria o pedido)?**
> *Anotações:* 


**2.3. Quais empresas/métodos de frete e logística vocês utilizam? (Correios, Melhor Envio, transportadoras próprias, Kangu, etc.)**
> *Anotações:* 


---

## 🎨 3. Produtos Personalizados (O ponto crítico)

**3.1. Qual a proporção das vendas entre produtos personalizados vs. prateleira (não personalizados)?**
> *Anotações:* 


**3.2. Como funciona o fluxo do personalizado (ex: Pedido > Envio da Arte > Aprovação > Produção > Despacho)?** 
*(O sistema precisará gerenciar os status dessa esteira de produção?)*
> *Anotações:* 


**3.3. O cliente faz a personalização no ato da compra (via site) ou vocês combinam os detalhes pelo WhatsApp após o pagamento?**
> *Anotações:* 


**3.4. O sistema precisará armazenar e gerenciar os arquivos de arte/design vinculados a cada pedido?**
> *Anotações:* 


---

## 💰 4. Financeiro e Precificação

**4.1. Como vocês calculam o custo do produto hoje? O sistema precisará de uma ficha técnica (composição de insumos) para os personalizados?**
> *Anotações:* 


**4.2. Vocês precisam que o sistema concilie automaticamente os repasses dos marketplaces?**
*(Descontando taxas de comissão da plataforma e frete)*
> *Anotações:* 


**4.3. O controle de Contas a Pagar e Receber envolverá conciliação bancária (importar arquivo OFX do banco)?**
> *Anotações:* 


**4.4. Sobre a Margem de Contribuição: quais custos variáveis (além da taxa do marketplace e impostos) vocês querem ratear por pedido (ex: embalagem, custo de aquisição/tráfego)?**
> *Anotações:* 


---

## 🏗️ 5. Estoque e Logística

**5.1. Como é feita a baixa de estoque dos personalizados?**
*(O estoque é da matéria-prima - ex: caneca branca em branco - ou do produto final?)*
> *Anotações:* 


**5.2. Vocês trabalham com múltiplos locais de estoque (estoque físico local vs. Full do Mercado Livre)?**
> *Anotações:* 


---

## 📌 Próximos Passos (Uso Interno)
- [ ] Validar nível de esforço das APIs necessárias (Mercado Livre, Shopee, Nuvemshop).
- [ ] Definir arquitetura da esteira de produção para os itens personalizados.
- [ ] Montar proposta dividida em módulos (MVP, Intermediário, Completo) ou proposta de mensalidade de desenvolvimento.
