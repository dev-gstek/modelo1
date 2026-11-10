# Planejamento Técnico do MVP — Vaga Fácil GO

## 1. Modelagem de Dados Central (Django Models)

```python
# core/models.py (Esboço Arquitetural)

class PerfilCandidato(models.Model):
    telefone = models.CharField(max_length=20, unique=True, db_index=True) # chave no WhatsApp
    nome_completo = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100, default="Goiânia")
    bairro = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=50) # Fundamental, Médio, Superior, Técnico
    areas_interesse = models.JSONField(default=list) # Ex: ["Vendas", "Estoque", "Administrativo"]
    resumo_experiencias = models.TextField(blank=True)
    disponibilidade_horario = models.CharField(max_length=100) # Manhã/Tarde, Escala 12x36, etc.
    canal_origem = models.CharField(max_length=20, choices=[("WEB", "Web"), ("WHATSAPP", "WhatsApp")])
    ativo = models.BooleanField(default=True)
    consentimento_lgpd = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Empresa(models.Model):
    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    telefone_contato = models.CharField(max_length=20)
    email = models.EmailField()
    verificada = models.BooleanField(default=False) # Moderação da plataforma

class Vaga(models.Model):
    TIPO_ORIGEM = [
        ("DIRETA", "Publicada por Empresa Cadastrada"),
        ("PARCEIRO", "Órgão Público / SINE / Entidade"),
        ("EXTERNA_CURADA", "Curadoria com Link Original"),
    ]
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    area = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100, blank=True)
    salario_info = models.CharField(max_length=100, default="A combinar")
    tipo_contratacao = models.CharField(max_length=50) # CLT, Estágio, Jovem Aprendiz
    tipo_origem = models.CharField(max_length=20, choices=TIPO_ORIGEM, default="DIRETA")
    link_externo_origem = models.URLField(blank=True, null=True)
    ativa = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

class Candidatura(models.Model):
    STATUS = [
        ("ENVIADA", "Enviada"),
        ("VISUALIZADA", "Visualizada pelo Empregador"),
        ("SELECIONADO_ENTREVISTA", "Selecionado para Entrevista"),
        ("FINALIZADA", "Processo Concluído"),
    ]
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name="candidaturas")
    candidato = models.ForeignKey(PerfilCandidato, on_delete=models.CASCADE, related_name="candidaturas")
    data_candidatura = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS, default="ENVIADA")
    respostas_criterios = models.JSONField(default=dict, blank=True)
```

## 2. Fluxo da Candidatura em 1 Clique com Triagem Leve

1. **Acesso:** Candidato navega na lista de vagas filtrando por Cidade (ex: *Aparecida de Goiânia*) e Área (*Comércio / Vendas*).
2. **Ação:** Clica em **"Quero me candidatar"**.
3. **Validação:**
   - Se já logado no navegador: Perfil carregado instantaneamente.
   - Se via WhatsApp: Digita o número da vaga (ex: *"Quero a vaga 12"*).
4. **Perguntas de Corte (Máximo 2 a 3 perguntas Sim/Não):**
   - *"Você tem disponibilidade para início imediato?"* [Sim/Não]
   - *"Tem fácil acesso à região do Buriti Shopping?"* [Sim/Não]
5. **Efetivação:** Candidatura registrada no painel da empresa instantaneamente.

## 3. Estratégia de Desenvolvimento por Etapas (Sprints)

- **Sprint 1 (Fundação Web):** Django + SQLite/Postgres + Models de Candidato, Vaga e Empresa + Templates responsivos Bootstrap 5.
- **Sprint 2 (Painel do Empregador & Vagas):** Cadastro rápido de empresas e publicação de vagas com filtros de triagem.
- **Sprint 3 (Motor de Candidatura em 1 Clique):** Mecanismo de submissão rápida e painel de triagem da empresa.
- **Sprint 4 (Webhook WhatsApp):** Integração com API de WhatsApp para cadastro conversacional e alertas de vagas.
- **Sprint 5 (Dashboard Administrativo e Indicadores):** Painel de métricas para prestação de contas com órgãos goianos (FAPEG / SINE).

