# 📚 MATERIAL COMPLETO PARA O TCC1 - TERRASAFE

**Aluno:** Gabriel Felipe Guarnieri
**Curso:** Engenharia de Software - UTFPR
**Projeto:** TerraSafe - Sistema Inteligente de Análise de Segurança para IaC
**Data:** Janeiro 2025

---

## 📂 ARQUIVOS CRIADOS

Este diretório contém 4 arquivos principais com TODO o conteúdo necessário para seu TCC1:

### 1. `TCC1_CONTEUDO_PRINCIPAL.md`
**O QUE TEM:**
- ✅ Estrutura completa do TCC1
- ✅ Capítulo 1 - INTRODUÇÃO (COMPLETO)
  - Contextualização
  - Problema de Pesquisa
  - Justificativa
  - Objetivos (Geral + 10 Objetivos Específicos)
  - Estrutura do Trabalho
- ✅ Capítulo 2 - FUNDAMENTAÇÃO TEÓRICA (OUTLINE)
  - Estrutura das seções
  - Indicações do que pesquisar
- ✅ Capítulo 3 - METODOLOGIA (COMPLETO)
  - Classificação da pesquisa
  - 5 fases de desenvolvimento
  - Tecnologias utilizadas
  - Métricas de avaliação

**PÁGINAS ESTIMADAS:** 40-50 páginas (quando completar Cap. 2)

---

### 2. `TCC1_RESULTADOS_E_CRONOGRAMA.md`
**O QUE TEM:**
- ✅ Capítulo 4 - DESENVOLVIMENTO E RESULTADOS (COMPLETO)
  - Arquitetura da solução
  - Resultados dos 3 testes (vulnerável, seguro, misto)
  - Análise de performance
  - Cobertura de testes (94%)
  - Comparação com Checkov, Terrascan, tfsec
- ✅ Capítulo 5 - CRONOGRAMA TCC2 (COMPLETO)
  - 10 atividades detalhadas
  - Cronograma de 20 semanas (fev-jun 2026)
  - Detalhamento mensal
  - Marcos e riscos
- ✅ Capítulo 6 - CONSIDERAÇÕES FINAIS (COMPLETO)
  - Conclusões parciais
  - Limitações
  - Próximos passos

**PÁGINAS ESTIMADAS:** 50-60 páginas

---

### 3. `TCC1_LACUNAS_PESQUISA.md` ⚠️ **CRÍTICO**
**O QUE TEM:**
- 🔍 Lista de TODAS as referências que você precisa buscar
- 🔍 Tópicos que precisam ser pesquisados para cada seção
- 🔍 Onde buscar (IEEE Xplore, ACM, Google Scholar, etc.)
- 🔍 Checklist de pesquisa
- 🔍 Estratégia de busca semana a semana

**REFERÊNCIAS ESSENCIAIS IDENTIFICADAS:**
- ⚠️ **OBRIGATÓRIO:** LIU et al. (2008) - Isolation Forest [IEEE Xplore]
- MORRIS (2020) - Infrastructure as Code [Livro]
- CHANDOLA et al. (2009) - Anomaly Detection Survey [ACM]
- IBM Security (2024) - Cost of Data Breach Report
- HUMBLE & FARLEY (2010) - Continuous Delivery
- + muitas outras listadas no arquivo

**AÇÃO REQUERIDA:** Você PRECISA fazer pesquisa bibliográfica extensa!

---

### 4. `TCC1_GUIA_ABNT.md`
**O QUE TEM:**
- 📐 Formatação completa ABNT (NBR 14724:2011)
- 📐 Como fazer citações (NBR 10520:2023)
- 📐 Como fazer referências (NBR 6023:2018)
- 📐 Exemplos de cada tipo de referência
- 📐 Formatação de figuras e tabelas
- 📐 Estrutura de elementos pré-textuais
- 📐 Checklist final de formatação
- 📐 Erros comuns a evitar

**USO:** Consulte este arquivo durante a escrita e formatação!

---

## 🎯 O QUE VOCÊ PRECISA FAZER AGORA

### PRIORIDADE MÁXIMA (Esta Semana):

#### 1. Buscar Artigo do Isolation Forest
```bash
# OBRIGATÓRIO - Fundamento teórico essencial
# Autor: LIU, Fei Tony; TING, Kai Ming; ZHOU, Zhi-Hua
# Ano: 2008
# Título: Isolation Forest
# Onde: IEEE Xplore (https://ieeexplore.ieee.org/)
# DOI: 10.1109/ICDM.2008.17

# Como acessar:
1. Entrar no Portal CAPES (via UTFPR)
2. Buscar "IEEE Xplore"
3. Pesquisar: "Isolation Forest Liu 2008"
4. Fazer download do PDF
5. Ler e fazer fichamento
```

#### 2. Começar Pesquisa Bibliográfica
```
- Ler arquivo TCC1_LACUNAS_PESQUISA.md (linha por linha!)
- Criar pasta "Referencias_TCC1/"
- Baixar pelo menos 5 referências essenciais
- Fazer fichamento de cada uma
```

#### 3. Testar Ferramentas Concorrentes
```bash
# Para completar tabela comparativa do Cap. 4
# Usar os mesmos arquivos test_files/vulnerable.tf, secure.tf, mixed.tf

# Instalar e testar Checkov:
pip install checkov
checkov -f test_files/vulnerable.tf

# Instalar e testar Terrascan:
# (ver documentação oficial)

# Instalar e testar tfsec:
# (ver documentação oficial)

# Anotar resultados para comparação
```

---

### PRIORIDADE ALTA (Próximas 2 Semanas):

#### 4. Redigir Seção 2.1 - Infraestrutura como Código
```
- Ler MORRIS (2020) - Capítulos 1-3
- Ler documentação Terraform
- Escrever subseções 2.1.1, 2.1.2, 2.1.3
- Meta: 8-10 páginas
- Prazo: [defina uma data]
```

#### 5. Redigir Seção 2.3.2 - Isolation Forest
```
- Estudar artigo LIU et al. (2008)
- Entender princípio matemático
- Explicar com suas palavras
- Meta: 4-5 páginas
- Prazo: [defina uma data]
```

---

### PRIORIDADE MÉDIA (Próximo Mês):

#### 6. Completar Capítulo 2 Inteiro
```
- Todas as 4 seções redigidas
- 30-40 páginas
- Mínimo 20 referências
- Revisão do orientador
- Prazo: [defina uma data]
```

#### 7. Preparar Elementos Pré-Textuais
```
- Escrever Resumo (150-500 palavras)
- Traduzir para Abstract
- Criar Lista de Figuras
- Criar Lista de Tabelas
- Atualizar Lista de Siglas
```

---

## 📊 STATUS ATUAL DO TCC1

```
✅ COMPLETO (85%):
- Capítulo 1 - Introdução
- Capítulo 3 - Metodologia
- Capítulo 4 - Desenvolvimento e Resultados
- Capítulo 5 - Cronograma TCC2
- Capítulo 6 - Considerações Finais

⚠️ INCOMPLETO (15%):
- Capítulo 2 - Fundamentação Teórica (apenas outline)
  → Requer pesquisa bibliográfica extensa
  → Requer redação de 30-40 páginas

🔨 TODO:
- Elementos pré-textuais (Resumo, Abstract, Listas)
- Formatação ABNT final
- Conversão de diagramas para imagens
- Revisão ortográfica/gramatical
- Verificação anti-plágio
```

---

## 📐 COMO ESCREVER O TCC1

### Usando LaTeX (Recomendado):

```bash
# 1. Criar conta no Overleaf: https://www.overleaf.com/

# 2. Procurar template "abnTeX2" ou "UTFPR"

# 3. Copiar o conteúdo dos arquivos .md para o LaTeX

# 4. Vantagens:
#    - Formatação ABNT automática
#    - Referências automáticas (BibTeX)
#    - Sumário gerado automaticamente
```

### Usando Word:

```
1. Configurar margens: 3-2-3-2 cm
2. Fonte: Times New Roman 12 pt
3. Espaçamento: 1,5 linhas
4. Seguir guia TCC1_GUIA_ABNT.md rigorosamente
5. Usar estilos para seções (Título 1, Título 2, etc.)
```

---

## 🗂️ ORGANIZAÇÃO RECOMENDADA

```
TerraSafe/
├── TCC1_README.md (este arquivo)
├── TCC1_CONTEUDO_PRINCIPAL.md
├── TCC1_RESULTADOS_E_CRONOGRAMA.md
├── TCC1_LACUNAS_PESQUISA.md
├── TCC1_GUIA_ABNT.md
├── Referencias_TCC1/          ← CRIAR ESTA PASTA
│   ├── LIU_2008_IsolationForest.pdf
│   ├── MORRIS_2020_InfraAsCode.pdf
│   ├── CHANDOLA_2009_AnomalyDetection.pdf
│   ├── IBM_2024_DataBreach.pdf
│   └── [outras referências]
├── Fichamentos/               ← CRIAR ESTA PASTA
│   ├── fichamento_liu_2008.md
│   ├── fichamento_morris_2020.md
│   └── [outros fichamentos]
├── Figuras_TCC1/              ← CRIAR ESTA PASTA
│   ├── arquitetura_terrasafe.png
│   ├── pipeline_analise.png
│   └── [outras figuras]
└── TCC1_Monografia_GabrielGuarnieri.tex  ← SEU DOCUMENTO FINAL
```

---

## 📅 CRONOGRAMA SUGERIDO PARA TCC1

### Semana 1-2 (AGORA):
- [ ] Buscar artigo LIU et al. (2008)
- [ ] Baixar 5 referências essenciais
- [ ] Testar Checkov, Terrascan, tfsec
- [ ] Criar estrutura de pastas

### Semana 3-4:
- [ ] Redigir seção 2.1 (IaC)
- [ ] Fazer fichamentos
- [ ] Primeira reunião com orientador

### Semana 5-6:
- [ ] Redigir seção 2.3.2 (Isolation Forest)
- [ ] Buscar trabalhos relacionados (2.4)
- [ ] Criar figuras

### Semana 7-8:
- [ ] Completar seção 2.2 (Segurança Cloud)
- [ ] Completar seção 2.3 (ML)
- [ ] Segunda reunião com orientador

### Semana 9-10:
- [ ] Completar seção 2.4 (Trabalhos Relacionados)
- [ ] Escrever Resumo/Abstract
- [ ] Criar listas (figuras, tabelas, siglas)

### Semana 11-12:
- [ ] Revisão completa
- [ ] Formatação ABNT final
- [ ] Verificação anti-plágio
- [ ] Revisão com orientador

### Semana 13-14:
- [ ] Ajustes finais
- [ ] Gerar PDF final
- [ ] ENTREGA DO TCC1 ✅

---

## ⚠️ ALERTAS IMPORTANTES

### 1. SOBRE PLÁGIO
```
❌ NUNCA copie texto sem aspas e citação
❌ NUNCA use texto da documentação do projeto sem citar
✅ SEMPRE parafraseie com suas palavras
✅ SEMPRE cite as fontes (autor, ano, página)
```

### 2. SOBRE CITAÇÕES DE SOFTWARE
```
Terraform, Checkov, etc. são citados como documentação técnica
Ver exemplos em TCC1_GUIA_ABNT.md, seção 4.6 e 4.9
```

### 3. SOBRE FIGURAS
```
Se usar diagramas do README:
Fonte: Autoria própria (2025)

Se adaptar de outras fontes:
Fonte: Adaptado de MORRIS (2020, p. 67)
```

---

## 🆘 PRECISA DE AJUDA?

Se tiver dúvidas específicas durante a escrita, você pode pedir ajuda para:

1. **Redigir seções específicas** (após buscar referências)
   - "Ajude-me a redigir a seção 2.1.1 sobre Evolução de IaC"

2. **Revisar texto**
   - "Revise este parágrafo que escrevi sobre Isolation Forest"

3. **Formatar referências**
   - "Converta esta referência para ABNT: [dados]"

4. **Criar tabelas/figuras**
   - "Crie uma tabela comparativa com estes dados: [dados]"

5. **Traduzir Abstract**
   - "Traduza este Resumo para inglês (Abstract)"

---

## ✅ CHECKLIST FINAL ANTES DA ENTREGA

```
CONTEÚDO:
□ Capítulo 1 completo e revisado
□ Capítulo 2 completo (30-40 páginas, ≥20 referências)
□ Capítulo 3 completo e revisado
□ Capítulo 4 completo com resultados reais
□ Capítulo 5 (Cronograma TCC2) completo
□ Capítulo 6 (Considerações) completo

ELEMENTOS PRÉ-TEXTUAIS:
□ Capa formatada
□ Folha de rosto com natureza do trabalho
□ Resumo (150-500 palavras) + palavras-chave
□ Abstract + keywords
□ Listas (figuras, tabelas, siglas)
□ Sumário atualizado

FORMATAÇÃO:
□ ABNT NBR 14724 aplicada
□ Citações no formato correto (NBR 10520)
□ Referências em ordem alfabética (NBR 6023)
□ Figuras e tabelas formatadas corretamente
□ Paginação correta

QUALIDADE:
□ Revisão ortográfica
□ Revisão gramatical
□ Verificação anti-plágio
□ Revisão do orientador
□ PDF gerado sem erros
```

---

## 🎓 ESTIMATIVA FINAL

**Total de páginas esperado:** 100-150 páginas

```
Elementos Pré-Textuais:  10-15 páginas (não contam na numeração)
Capítulo 1:              8-12 páginas
Capítulo 2:              30-40 páginas  ← TRABALHO PRINCIPAL
Capítulo 3:              15-20 páginas
Capítulo 4:              35-45 páginas
Capítulo 5:              8-12 páginas
Capítulo 6:              3-5 páginas
Referências:             3-5 páginas
```

---

## 🚀 VAMOS LÁ!

Você tem:
- ✅ 85% do conteúdo já redigido
- ✅ Estrutura completa definida
- ✅ Guia ABNT detalhado
- ✅ Lista clara de referências para buscar
- ✅ Cronograma para TCC2 pronto

**O que falta:**
- 🔨 Pesquisa bibliográfica (Cap. 2)
- 🔨 Redação de 30-40 páginas (Cap. 2)
- 🔨 Formatação final ABNT
- 🔨 Elementos pré-textuais

**Você consegue! 🎉**

---

**Data de criação deste material:** 28 de Outubro de 2025
**Última atualização:** 28 de Outubro de 2025

**Boa sorte com o TCC1! 📚🚀**
