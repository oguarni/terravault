# GUIA DE FORMATAÇÃO ABNT PARA O TCC1

## NORMAS ABNT APLICÁVEIS

**Normas principais:**
- **NBR 14724:2011** - Trabalhos acadêmicos (estrutura)
- **NBR 6023:2018** - Referências bibliográficas
- **NBR 6027:2012** - Sumário
- **NBR 6028:2021** - Resumo
- **NBR 10520:2023** - Citações
- **NBR 6024:2012** - Numeração de seções

---

## 1. FORMATAÇÃO GERAL DO DOCUMENTO

### 1.1 Configurações de Página

```
Papel: A4 (21,0 cm × 29,7 cm)

Margens:
  - Superior: 3 cm
  - Inferior: 2 cm
  - Esquerda: 3 cm
  - Direita: 2 cm

Fonte: Times New Roman ou Arial

Tamanho:
  - Corpo do texto: 12 pt
  - Citações longas: 10 pt
  - Notas de rodapé: 10 pt
  - Legendas de figuras/tabelas: 10 pt

Espaçamento entre linhas:
  - Texto principal: 1,5 linhas
  - Citações longas: simples (1,0)
  - Resumo: simples
  - Referências: simples (com espaço duplo entre entradas)
  - Legendas: simples

Alinhamento:
  - Texto: Justificado
  - Títulos de seções: Alinhado à esquerda
  - Títulos não numerados (RESUMO, ABSTRACT): Centralizados

Recuo de parágrafo: 1,25 cm (primeira linha)
Recuo de citação longa: 4 cm da margem esquerda
```

### 1.2 Paginação

```
Elementos pré-textuais: Contam, mas NÃO aparecem
  (capa, folha de rosto, resumo, abstract, listas, sumário)

Elementos textuais: Numeração arábica (1, 2, 3...)
  Inicia na INTRODUÇÃO como página 1
  Posição: Canto superior direito, a 2 cm da borda

Elementos pós-textuais: Continua numeração
```

---

## 2. ELEMENTOS PRÉ-TEXTUAIS

### 2.1 CAPA (obrigatório)

```
[Centralizado, fonte 12, espaçamento simples]

UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ
DEPARTAMENTO ACADÊMICO DE INFORMÁTICA
CURSO DE ENGENHARIA DE SOFTWARE

[4-5 espaços duplos]

GABRIEL FELIPE GUARNIERI

[4-5 espaços duplos]

TERRASAFE: SISTEMA INTELIGENTE DE ANÁLISE DE SEGURANÇA
PARA INFRAESTRUTURA COMO CÓDIGO UTILIZANDO
ISOLATION FOREST

[Espaços até o final da página]

PONTA GROSSA
2025
```

### 2.2 FOLHA DE ROSTO (obrigatório)

```
[Topo - centralizado]
GABRIEL FELIPE GUARNIERI

[Centro da página - centralizado]

TERRASAFE: SISTEMA INTELIGENTE DE ANÁLISE DE SEGURANÇA
PARA INFRAESTRUTURA COMO CÓDIGO UTILIZANDO
ISOLATION FOREST

[Recuo de 8 cm da margem esquerda, justificado, tamanho 10]
    Trabalho de Conclusão de Curso de
    Graduação apresentado como requisito
    para obtenção do título de Bacharel em
    Engenharia de Software do Departamento
    Acadêmico de Informática da Universidade
    Tecnológica Federal do Paraná.

    Orientador: Prof. Dr. [Nome do Orientador]

[Rodapé - centralizado]
PONTA GROSSA
2025
```

### 2.3 RESUMO (obrigatório)

```
RESUMO

GUARNIERI, Gabriel Felipe. TerraSafe: Sistema Inteligente de Análise de Segurança
para Infraestrutura como Código Utilizando Isolation Forest. 2025. 120 f. Trabalho
de Conclusão de Curso (Bacharelado em Engenharia de Software) - Universidade
Tecnológica Federal do Paraná. Ponta Grossa, 2025.

[Texto do resumo: parágrafo único, espaçamento simples, 150-500 palavras]

A Infraestrutura como Código (IaC) tornou-se prática fundamental em ambientes de
computação em nuvem, porém configurações inadequadas representam principal vetor
de vulnerabilidades. Este trabalho propõe o TerraSafe, sistema inteligente que
combina detecção baseada em regras com aprendizado de máquina para análise de
segurança em arquivos Terraform. [...]

Palavras-chave: Infraestrutura como Código. Segurança de Nuvem. Aprendizado de
Máquina. Detecção de Anomalias. Isolation Forest. DevSecOps.
```

**IMPORTANTE:**
- Resumo em parágrafo ÚNICO
- Espaçamento SIMPLES
- 150-500 palavras
- Palavras-chave separadas por ponto (não vírgula)

### 2.4 ABSTRACT (obrigatório)

```
ABSTRACT

GUARNIERI, Gabriel Felipe. TerraSafe: Intelligent Security Analysis System for
Infrastructure as Code Using Isolation Forest. 2025. 120 p. Final Project
(Bachelor in Software Engineering) - Federal University of Technology - Paraná.
Ponta Grossa, 2025.

[Tradução do resumo]

Keywords: Infrastructure as Code. Cloud Security. Machine Learning. Anomaly
Detection. Isolation Forest. DevSecOps.
```

### 2.5 LISTA DE ABREVIATURAS E SIGLAS

```
LISTA DE ABREVIATURAS E SIGLAS

ABNT    Associação Brasileira de Normas Técnicas
API     Application Programming Interface
AWS     Amazon Web Services
CI/CD   Continuous Integration / Continuous Deployment
HCL     HashiCorp Configuration Language
IaC     Infrastructure as Code
ML      Machine Learning
SAST    Static Application Security Testing
```

**Ordem:** Alfabética

### 2.6 SUMÁRIO (obrigatório)

```
SUMÁRIO

1 INTRODUÇÃO................................................................12
1.1 CONTEXTUALIZAÇÃO........................................................12
1.2 PROBLEMA DE PESQUISA....................................................14
1.3 JUSTIFICATIVA...........................................................15
1.4 OBJETIVOS...............................................................17
1.4.1 Objetivo Geral........................................................17
1.4.2 Objetivos Específicos.................................................17
1.5 ESTRUTURA DO TRABALHO...................................................18

2 FUNDAMENTAÇÃO TEÓRICA.....................................................20
[...]

REFERÊNCIAS................................................................110
```

**IMPORTANTE:**
- Não numerar: RESUMO, ABSTRACT, LISTAS, REFERÊNCIAS
- Pontilhado até o número da página
- Seções até nível 4 (evitar nível 5)

---

## 3. CITAÇÕES (NBR 10520:2023)

### 3.1 Citação Direta Curta (até 3 linhas)

```
Segundo Morris (2020, p. 45), "a infraestrutura como código permite versionamento
e auditoria completa de mudanças de configuração".

OU:

"A infraestrutura como código permite versionamento e auditoria completa de mudanças
de configuração" (MORRIS, 2020, p. 45).
```

**Regras:**
- Usar aspas duplas
- Incluir número da página (obrigatório)
- Manter pontuação original

### 3.2 Citação Direta Longa (mais de 3 linhas)

```
Liu, Ting e Zhou (2008, p. 415) descrevem o princípio fundamental do Isolation Forest:

    O algoritmo Isolation Forest baseia-se na observação de que anomalias são
    poucos e diferentes, e portanto podem ser isoladas mais facilmente do que
    pontos normais. O processo de isolamento é realizado através de partições
    aleatórias do espaço de features, criando árvores binárias onde anomalias
    tendem a ter caminho médio mais curto até a folha da árvore.

Este princípio permite complexidade computacional linear, adequada para aplicações
em tempo real.
```

**Formatação:**
- Recuo de 4 cm da margem esquerda
- Espaçamento simples (1,0)
- Fonte tamanho 10 pt
- **SEM aspas**
- **SEM itálico**

### 3.3 Citação Indireta (paráfrase)

```
A computação em nuvem transformou a maneira como organizações gerenciam infraestrutura
(HUMBLE; FARLEY, 2010).

OU:

Humble e Farley (2010) argumentam que a computação em nuvem transformou o
gerenciamento de infraestrutura.
```

**Regras:**
- NÃO usar aspas
- NÃO precisa número de página
- Texto com suas próprias palavras

### 3.4 Múltiplos Autores

```
1 autor: (SILVA, 2020) ou Silva (2020)
2 autores: (SILVA; SANTOS, 2020) ou Silva e Santos (2020)
3 autores: (SILVA; SANTOS; OLIVEIRA, 2020) ou Silva, Santos e Oliveira (2020)
4+ autores: (SILVA et al., 2020) ou Silva et al. (2020)
```

**ATENÇÃO:**
- Na citação: ponto e vírgula (;) entre autores
- No texto corrido: "e" entre autores

### 3.5 Citação de Citação (apud) - EVITAR!

```
Segundo Silva (1995 apud SANTOS, 2020, p. 78), "a segurança deve ser considerada
desde o design".
```

**IMPORTANTE:**
- Usar APENAS quando impossível acessar fonte original
- Na lista de referências, incluir apenas SANTOS (2020)

### 3.6 Documento Sem Autor (Entidade)

```
(GARTNER, 2024)
(IBM SECURITY, 2024)
(HASHICORP, 2023)
```

**Regra:** Nome da entidade em MAIÚSCULAS

---

## 4. REFERÊNCIAS (NBR 6023:2018)

### 4.1 Formatação Geral

```
- Título da seção: REFERÊNCIAS (centralizado, negrito, maiúsculas)
- Alinhamento: Justificado à esquerda
- Espaçamento: Simples dentro de cada entrada, duplo entre entradas
- Ordem: Alfabética por sobrenome do autor
- Deslocamento: 0 cm (não recuar primeira linha)
```

### 4.2 Livro Completo

```
SOBRENOME, Nome. Título do livro: subtítulo. Edição. Cidade: Editora, ano.
```

**Exemplos:**

```
MORRIS, Kief. Infrastructure as Code: managing servers in the cloud. 2. ed.
Sebastopol: O'Reilly Media, 2020.

HUMBLE, Jez; FARLEY, David. Continuous Delivery: reliable software releases
through build, test, and deployment automation. Boston: Addison-Wesley, 2010.

BISHOP, Christopher M. Pattern Recognition and Machine Learning. New York:
Springer, 2006.
```

**Regras:**
- Título do livro em negrito OU itálico (escolher um padrão)
- Edição: 2. ed., 3. ed. (primeira edição não mencionar)
- Sobrenome em MAIÚSCULAS

### 4.3 Artigo de Periódico Científico

```
SOBRENOME, Nome. Título do artigo. Título do Periódico, Local, v. volume,
n. número, p. página inicial-final, mês abreviado. ano. DOI: [se disponível].
```

**Exemplo:**

```
LIU, Fei Tony; TING, Kai Ming; ZHOU, Zhi-Hua. Isolation Forest. In: IEEE
INTERNATIONAL CONFERENCE ON DATA MINING (ICDM), 8., 2008, Pisa. Proceedings [...].
Pisa: IEEE, 2008. p. 413-422. DOI: 10.1109/ICDM.2008.17.

CHANDOLA, Varun; BANERJEE, Arindam; KUMAR, Vipin. Anomaly Detection: a survey.
ACM Computing Surveys, New York, v. 41, n. 3, p. 1-58, July 2009.
```

**Regras:**
- Título do periódico em negrito OU itálico
- Incluir DOI quando disponível

### 4.4 Artigo de Conferência/Evento

```
SOBRENOME, Nome. Título do trabalho. In: NOME DO EVENTO, número, ano, Local.
Anais [...]. Local: Editora, ano. p. página inicial-final.
```

**Exemplo:**

```
HARIRI, Sahand; KIND, Matias Carrasco; BRUNNER, Robert J. Extended Isolation
Forest. In: IEEE INTERNATIONAL CONFERENCE ON DATA SCIENCE AND ADVANCED ANALYTICS
(DSAA), 7., 2019, Washington. Proceedings [...]. Washington: IEEE, 2019. p. 1-10.
```

### 4.5 Documento Online (Site, Relatório)

```
ENTIDADE. Título. Ano. Disponível em: URL. Acesso em: dia mês abreviado. ano.
```

**Exemplos:**

```
IBM SECURITY. Cost of a Data Breach Report 2024. Armonk: IBM Corporation, 2024.
Disponível em: https://www.ibm.com/security/data-breach. Acesso em: 20 jan. 2025.

GARTNER. Gartner Forecasts Worldwide Public Cloud End-User Spending to Reach
Nearly $600 Billion in 2023. 2022. Disponível em: https://www.gartner.com/en/
newsroom/press-releases/2022-10-31-gartner-forecasts. Acesso em: 15 jan. 2025.

HASHICORP. Terraform Documentation: Security Best Practices. 2023. Disponível em:
https://developer.hashicorp.com/terraform/tutorials/configuration-language/
sensitive-variables. Acesso em: 10 jan. 2025.
```

**ATENÇÃO:**
- URL longo: pode quebrar linha (sem hífen)
- Data de acesso: obrigatória
- Mês abreviado: jan., fev., mar., abr., maio, jun., jul., ago., set., out.,
  nov., dez.

### 4.6 Software/Repositório GitHub

```
AUTOR. Nome do Repositório. Versão. Ano. Disponível em: URL. Acesso em: data.
```

**Exemplo:**

```
BRIDGECREW. Checkov: static code analysis tool for infrastructure as code.
Version 2.5.2. 2024. Disponível em: https://github.com/bridgecrewio/checkov.
Acesso em: 18 jan. 2025.
```

---

## 5. FIGURAS E TABELAS

### 5.1 Figuras

**Formatação:**
- Título: acima da figura, centralizado, fonte 10 pt
- Fonte: abaixo da figura, centralizado, fonte 10 pt
- Figura centralizada na página

**Exemplo:**

```
[No texto:]
A arquitetura do sistema TerraSafe é organizada em quatro camadas principais,
conforme ilustrado na Figura 1.

Figura 1 – Arquitetura em Camadas do Sistema TerraSafe

[IMAGEM AQUI - centralizada]

Fonte: Autoria própria (2025).
```

**Se adaptado de outra fonte:**
```
Fonte: Adaptado de Morris (2020, p. 67).
```

### 5.2 Tabelas

**Formatação:**
- Título: acima da tabela
- Fonte: abaixo da tabela
- Abertas nas laterais (sem bordas verticais)
- Linhas horizontais apenas no topo e rodapé

**Exemplo:**

```
Tabela 1 – Comparação de Ferramentas de Análise IaC

Ferramenta    | Vulnerabilidades | Performance | ML Support
--------------|------------------|-------------|------------
TerraSafe     | 6/6 (100%)      | 0.82s       | Sim
Checkov       | 5/6 (83%)       | 1.45s       | Não
Terrascan     | 4/6 (67%)       | 2.10s       | Não

Fonte: Autoria própria (2025).
```

---

## 6. SEÇÕES E SUBSEÇÕES (NBR 6024:2012)

### 6.1 Numeração e Formatação

```
1 SEÇÃO PRIMÁRIA (CAIXA ALTA, NEGRITO, fonte 12)

1.1 SEÇÃO SECUNDÁRIA (CAIXA ALTA, SEM NEGRITO, fonte 12)

1.1.1 Seção Terciária (Somente primeira letra maiúscula, negrito, fonte 12)

1.1.1.1 Seção Quaternária (Somente primeira letra maiúscula, sem negrito, fonte 12)
```

**IMPORTANTE:**
- Evitar seção quinária (1.1.1.1.1)
- Limite recomendado: quaternária
- Alinhamento: à esquerda
- Não numerar: RESUMO, ABSTRACT, LISTAS, SUMÁRIO, REFERÊNCIAS

### 6.2 Exemplo Completo

```
2 FUNDAMENTAÇÃO TEÓRICA

2.1 INFRAESTRUTURA COMO CÓDIGO (IAC)

2.1.1 Conceitos e Evolução

[Texto da seção terciária...]

2.1.2 Terraform e HashiCorp Configuration Language

[Texto...]

2.2 SEGURANÇA EM COMPUTAÇÃO EM NUVEM

2.2.1 Vulnerabilidades e Misconfigurations

[Texto...]
```

---

## 7. FERRAMENTAS RECOMENDADAS

### 7.1 LaTeX com abnTeX2 (RECOMENDADO)

```
# Template UTFPR pronto
git clone https://github.com/utfpr-dv/abntex2-utfpr

# Ou usar Overleaf online:
https://www.overleaf.com/
# Procurar template "abntex2" ou "UTFPR"
```

**Vantagens:**
- Formatação ABNT automática
- Referências automáticas (BibTeX)
- Sumário gerado automaticamente
- Numeração de páginas correta

### 7.2 Microsoft Word

```
- Usar estilos personalizados
- Cuidado com formatação de referências (fazer manualmente ou usar Mendeley)
- Ferramentas: Fast Format, More
```

### 7.3 Gerenciadores de Referências

```
Zotero (RECOMENDADO - gratuito):
1. Instalar: https://www.zotero.org/
2. Adicionar connector do navegador
3. Coletar referências de IEEE/ACM automaticamente
4. Exportar em formato ABNT (BibTeX ou copiar formatado)

Mendeley (gratuito)
JabRef (para LaTeX)
```

---

## 8. CHECKLIST FINAL DE FORMATAÇÃO

```
ESTRUTURA:
□ Capa formatada corretamente
□ Folha de rosto com natureza do trabalho
□ Resumo entre 150-500 palavras + palavras-chave
□ Abstract (tradução do resumo) + keywords
□ Listas (figuras, tabelas, siglas) se aplicável
□ Sumário com paginação correta

FORMATAÇÃO GERAL:
□ Margens: 3-2-3-2 cm
□ Fonte Times ou Arial, tamanho 12
□ Espaçamento 1,5 no texto principal
□ Paginação: pré-textuais não numerados, textuais a partir de 1

CITAÇÕES E REFERÊNCIAS:
□ Citações formatadas conforme NBR 10520
□ Todas as citações têm referência correspondente
□ Referências em ordem alfabética, NBR 6023
□ Sem referências não citadas no texto

FIGURAS E TABELAS:
□ Figuras e tabelas numeradas sequencialmente
□ Títulos de figuras acima, fonte abaixo
□ Tabelas abertas nas laterais
□ Todas chamadas no texto

QUALIDADE:
□ Seções numeradas corretamente (NBR 6024)
□ Revisão ortográfica e gramatical
□ Verificação anti-plágio
□ Sem "lorem ipsum" ou placeholders
```

---

## 9. ERROS COMUNS A EVITAR

❌ **ERRADO:**
```
Morris, K. (2020). Infrastructure as Code. O'Reilly.
```
✅ **CORRETO:**
```
MORRIS, Kief. Infrastructure as Code: managing servers in the cloud. 2. ed.
Sebastopol: O'Reilly Media, 2020.
```

---

❌ **ERRADO:**
```
Segundo Morris, "IaC é importante".
```
✅ **CORRETO:**
```
Segundo Morris (2020, p. 45), "a infraestrutura como código permite versionamento
e auditoria completa de mudanças de configuração".
```

---

❌ **ERRADO:**
```
1 Introdução
1.1 Contextualização
```
✅ **CORRETO:**
```
1 INTRODUÇÃO
1.1 CONTEXTUALIZAÇÃO
```

---

**BOA FORMATAÇÃO! 📝**
