# TCC1 - TerraSafe: Sistema Inteligente de Análise de Segurança para IaC

## ESTRUTURA COMPLETA DO DOCUMENTO

```
ELEMENTOS PRÉ-TEXTUAIS
├── Capa (obrigatório)
├── Folha de Rosto (obrigatório)
├── Resumo em Português (obrigatório)
├── Abstract em Inglês (obrigatório)
├── Lista de Figuras (se aplicável)
├── Lista de Tabelas (se aplicável)
├── Lista de Abreviaturas e Siglas (recomendado)
└── Sumário (obrigatório)

ELEMENTOS TEXTUAIS
1. INTRODUÇÃO
2. FUNDAMENTAÇÃO TEÓRICA
3. METODOLOGIA
4. DESENVOLVIMENTO E RESULTADOS PRELIMINARES
5. CRONOGRAMA PARA O TCC2
6. CONSIDERAÇÕES FINAIS

ELEMENTOS PÓS-TEXTUAIS
├── Referências (obrigatório)
└── Apêndices (opcional)
```

---

# 1 INTRODUÇÃO

## 1.1 CONTEXTUALIZAÇÃO

A computação em nuvem transformou profundamente a maneira como organizações desenvolvem,
implantam e gerenciam infraestrutura tecnológica. Neste contexto, a prática de
Infraestrutura como Código (Infrastructure as Code - IaC) emergiu como um paradigma
fundamental para automatizar o provisionamento e a configuração de recursos computacionais
(MORRIS, 2020). Ferramentas como Terraform, desenvolvida pela HashiCorp, permitem que
equipes de desenvolvimento definam infraestrutura inteira através de arquivos de
configuração declarativos, possibilitando versionamento, replicação e automação de
ambientes complexos.

Apesar dos benefícios evidentes em termos de agilidade e consistência, a adoção de IaC
introduz novos vetores de risco à segurança organizacional. Configurações inadequadas
(misconfigurations) em arquivos de infraestrutura podem expor sistemas a vulnerabilidades
críticas antes mesmo de recursos serem provisionados na nuvem. Segundo relatório da
Gartner (2024), estima-se que 99% das falhas de segurança em ambientes de nuvem até 2025
serão causadas por erros de configuração do cliente, não por falhas dos provedores de
serviços.

A complexidade crescente de arquiteturas de nuvem, combinada com a velocidade de
implantação característica de metodologias DevOps, torna impraticável a revisão manual
exaustiva de configurações de infraestrutura. Este cenário demanda soluções automatizadas
capazes de identificar vulnerabilidades de segurança em código de infraestrutura de
forma proativa, antes da implantação em ambiente produtivo.

Ferramentas tradicionais de análise estática de segurança (SAST - Static Application
Security Testing) para IaC baseiam-se predominantemente em detecção baseada em regras
(rule-based detection), identificando padrões conhecidos de vulnerabilidades através de
assinaturas pré-definidas. Embora eficazes para detectar problemas catalogados, estas
abordagens apresentam limitações significativas na identificação de configurações
anômalas que não correspondem a padrões de ataque conhecidos, mas que ainda assim
representam riscos de segurança.

Neste contexto, técnicas de Inteligência Artificial, especificamente algoritmos de
aprendizado de máquina para detecção de anomalias, apresentam-se como complemento
promissor às abordagens tradicionais. O algoritmo Isolation Forest, proposto por Liu,
Ting e Zhou (2008), demonstrou eficácia na identificação de outliers em conjuntos de
dados estruturados, característica aplicável à análise de configurações de
infraestrutura.

## 1.2 PROBLEMA DE PESQUISA

O problema central que motiva este trabalho pode ser formulado através da seguinte
questão de pesquisa:

**"Como desenvolver um sistema inteligente capaz de identificar vulnerabilidades de
segurança em arquivos Terraform, combinando detecção baseada em regras determinísticas
com técnicas de aprendizado de máquina para detecção de anomalias, de modo a superar
as limitações de ferramentas tradicionais puramente baseadas em assinaturas?"**

Este problema desdobra-se em questões secundárias:

a) Como extrair features relevantes de arquivos HCL2 (HashiCorp Configuration Language)
   que representem adequadamente o perfil de segurança de uma configuração de
   infraestrutura?

b) Como integrar de forma complementar resultados de análise determinística (regras)
   com análise probabilística (aprendizado de máquina) em um score de risco unificado?

c) Como garantir que o sistema seja suficientemente explicável (explainable AI) para
   permitir que engenheiros compreendam as razões das classificações de risco?

d) Como otimizar o sistema para performance adequada em pipelines de CI/CD, onde latência
   é fator crítico?

## 1.3 JUSTIFICATIVA

A relevância deste trabalho fundamenta-se em três pilares principais:

### 1.3.1 Relevância Técnica e Econômica

Segundo o relatório "Cost of a Data Breach 2024" da IBM Security, o custo médio de uma
violação de dados relacionada a nuvem atinge US$ 5 milhões, representando aumento de
15% em relação ao ano anterior. Aproximadamente 70% das organizações reportaram
incidentes de segurança relacionados a IaC no último ano, sendo configurações inadequadas
o vetor de ataque mais comum.

A detecção proativa de vulnerabilidades em estágios iniciais do ciclo de desenvolvimento
(shift-left security) reduz significativamente custos de correção. Estudos indicam que
corrigir vulnerabilidades em produção custa até 100 vezes mais do que corrigi-las durante
o desenvolvimento (MCGRAW, 2006).

### 1.3.2 Justificativa para Uso de Inteligência Artificial

Ferramentas tradicionais de análise estática operam exclusivamente através de regras
pré-definidas, apresentando limitações fundamentais:

a) Incapacidade de detectar configurações anômalas não catalogadas;
b) Alta taxa de falsos negativos para padrões de ataque emergentes;
c) Necessidade de atualização manual constante de bases de regras;
d) Dificuldade em adaptar-se a contextos organizacionais específicos.

A integração de técnicas de aprendizado de máquina permite:

a) Detecção de padrões anômalos não previstos em regras estáticas;
b) Adaptação a baselines de segurança específicos de cada organização;
c) Aprendizado contínuo com novas configurações analisadas;
d) Scoring probabilístico que complementa análise determinística.

O algoritmo Isolation Forest é particularmente adequado por:

a) Operar em modo não-supervisionado, sem necessidade de datasets rotulados extensos;
b) Apresentar complexidade temporal O(n log n), adequada para pipelines de CI/CD;
c) Demonstrar eficácia comprovada em detecção de outliers em dados estruturados;
d) Permitir interpretabilidade através de scores de anomalia.

### 1.3.3 Contribuição Científica e Acadêmica

Este trabalho contribui para o estado da arte através de:

a) Integração de abordagens determinísticas e probabilísticas em sistema híbrido;
b) Desenvolvimento de metodologia de feature engineering específica para IaC;
c) Implementação de sistema production-ready com hardening de segurança;
d) Avaliação empírica de eficácia em cenários realísticos;
e) Disponibilização de ferramenta open-source para comunidade acadêmica e profissional.

## 1.4 OBJETIVOS

### 1.4.1 Objetivo Geral

Desenvolver e avaliar um sistema inteligente de análise de segurança para arquivos
Terraform que combine detecção baseada em regras com técnicas de aprendizado de máquina
(Isolation Forest) para identificação de vulnerabilidades e configurações anômalas em
Infraestrutura como Código.

### 1.4.2 Objetivos Específicos

Os objetivos específicos que viabilizam o objetivo geral são:

a) Implementar módulo de parsing de arquivos HCL2 (HashiCorp Configuration Language)
   capaz de extrair estruturas de recursos e configurações;

b) Desenvolver engine de detecção baseada em regras para identificação de
   vulnerabilidades conhecidas (portas expostas, credenciais hardcoded, criptografia
   desabilitada, configurações públicas);

c) Projetar e implementar pipeline de feature engineering que extraia características
   relevantes de configurações IaC para treinamento do modelo de ML;

d) Implementar modelo de detecção de anomalias utilizando algoritmo Isolation Forest,
   treinado em baseline de configurações seguras;

e) Desenvolver sistema híbrido de scoring que combine pesos de análise determinística
   (60%) e probabilística (40%) em score de risco unificado (0-100);

f) Integrar sistema com infraestrutura de produção, incluindo banco de dados PostgreSQL,
   cache Redis, e sistema de métricas Prometheus/Grafana;

g) Implementar hardening de segurança (validação de entrada, proteção contra path
   traversal, hashing de API keys, rate limiting);

h) Desenvolver API RESTful com FastAPI para integração com pipelines de CI/CD;

i) Avaliar eficácia do sistema através de testes com configurações vulneráveis, seguras
   e mistas, mensurando acurácia, precisão, recall e performance;

j) Comparar resultados com ferramentas estabelecidas no mercado (Checkov, Terrascan,
   tfsec).

## 1.5 ESTRUTURA DO TRABALHO

Este documento está organizado da seguinte forma:

O Capítulo 2 apresenta a fundamentação teórica, abordando conceitos de Infraestrutura
como Código, segurança em nuvem, DevSecOps, detecção de anomalias e algoritmo Isolation
Forest, além de revisão de trabalhos relacionados.

O Capítulo 3 descreve a metodologia de pesquisa e desenvolvimento, classificando a
natureza da pesquisa, detalhando o método de desenvolvimento do sistema, tecnologias
utilizadas e métricas de avaliação.

O Capítulo 4 apresenta o desenvolvimento da solução e resultados preliminares, incluindo
arquitetura do sistema, implementação dos módulos, melhorias de segurança e performance,
e resultados de testes realizados.

O Capítulo 5 estabelece cronograma detalhado para a fase TCC2, contemplando atividades
de aprimoramento, validação estendida e documentação final.

O Capítulo 6 apresenta considerações finais do TCC1, conclusões parciais, limitações
identificadas e direcionamentos para continuidade do trabalho.

---

# 2 FUNDAMENTAÇÃO TEÓRICA

**NOTA:** Este capítulo precisa ser expandido com pesquisa bibliográfica detalhada.
Ver arquivo `TCC1_LACUNAS_PESQUISA.md` para lista de referências e tópicos a pesquisar.

## 2.1 INFRAESTRUTURA COMO CÓDIGO (IAC)

### 2.1.1 Conceitos e Evolução

[REDIGIR: Histórico da evolução de gerenciamento de infraestrutura manual → scripts →
IaC declarativa. Discutir benefícios: versionamento, reprodutibilidade, documentação
como código, automação.]

### 2.1.2 Terraform e HashiCorp Configuration Language (HCL)

[REDIGIR: Arquitetura do Terraform (providers, resources, state), sintaxe HCL2,
ciclo de vida (init, plan, apply), comparação com alternativas.]

### 2.1.3 Desafios de Segurança em IaC

[REDIGIR: Tipos comuns de misconfiguration, impacto de vulnerabilidades em IaC,
shift-left security.]

## 2.2 SEGURANÇA EM COMPUTAÇÃO EM NUVEM

### 2.2.1 Vulnerabilidades e Misconfigurations

[REDIGIR: Modelo de responsabilidade compartilhada, categorização de vulnerabilidades.]

### 2.2.2 DevSecOps e Security as Code

[REDIGIR: Integração de segurança em pipelines CI/CD, conceito de security as code.]

### 2.2.3 Ferramentas de Análise Estática (SAST)

[REDIGIR: Fundamentos de SAST, aplicação para IaC, limitações.]

## 2.3 APRENDIZADO DE MÁQUINA PARA SEGURANÇA

### 2.3.1 Detecção de Anomalias

[REDIGIR: Conceitos de anomaly detection, tipos, aplicações em segurança.]

### 2.3.2 Algoritmo Isolation Forest

[REDIGIR: Fundamentos matemáticos, princípio de isolamento, complexidade O(n log n).]

### 2.3.3 Aprendizado Não-Supervisionado

[REDIGIR: Paradigmas de ML, justificativa para unsupervised learning em segurança.]

## 2.4 TRABALHOS RELACIONADOS

### 2.4.1 Ferramentas Comerciais de IaC Security

[REDIGIR: Análise de Checkov, Terrascan, tfsec. Criar tabela comparativa.]

### 2.4.2 Abordagens Baseadas em ML para Segurança de IaC

[REDIGIR: Estado da arte de ML em IaC security. Buscar em IEEE/ACM.]

### 2.4.3 Análise Comparativa e Posicionamento

[REDIGIR: Quadro comparativo posicionando TerraSafe, destacando diferenciais.]

---

# 3 METODOLOGIA

## 3.1 CLASSIFICAÇÃO DA PESQUISA

Este trabalho caracteriza-se como pesquisa aplicada de natureza tecnológica, com
abordagem predominantemente experimental e quantitativa.

Quanto à natureza, classifica-se como **pesquisa aplicada**, uma vez que objetiva gerar
conhecimentos para aplicação prática dirigida à solução de problema específico: detecção
automatizada de vulnerabilidades em Infraestrutura como Código (GIL, 2002).

Quanto aos objetivos, caracteriza-se como **pesquisa exploratória e descritiva**
(PRODANOV; FREITAS, 2013). Exploratória porque investiga a aplicabilidade de técnicas
de aprendizado de máquina (especificamente Isolation Forest) em domínio relativamente
novo (segurança de IaC). Descritiva porque documenta e analisa sistematicamente o
comportamento do sistema desenvolvido através de métricas objetivas.

Quanto à abordagem, utiliza **métodos quantitativos**, fundamentando conclusões em
dados mensuráveis: scores de segurança, tempos de execução, taxas de detecção,
cobertura de testes, entre outros indicadores objetivos.

Quanto aos procedimentos técnicos, adota **pesquisa experimental** combinada com
**estudo de caso**, conduzindo experimentos controlados com configurações Terraform de
diferentes perfis de segurança (vulnerável, seguro, misto) e analisando comportamento
do sistema em cenários realísticos.

## 3.2 MÉTODO DE DESENVOLVIMENTO

O desenvolvimento do sistema TerraSafe seguiu abordagem iterativa e incremental,
organizada em cinco fases principais, alinhadas com práticas de desenvolvimento ágil
de software.

### 3.2.1 Fase 1: Levantamento de Requisitos e Projeto Arquitetural

**Atividades realizadas:**

a) Estudo de vulnerabilidades comuns em Terraform através de:
   - Análise de documentação de ferramentas existentes (Checkov, Terrascan, tfsec)
   - Revisão de CIS Benchmarks para AWS, Azure e GCP
   - Estudo de casos de breaches causados por misconfiguration

b) Definição de requisitos funcionais:
   - RF01: Parser de arquivos HCL2
   - RF02: Detecção de vulnerabilidades conhecidas via regras
   - RF03: Extração de features para modelo ML
   - RF04: Classificação de risco via Isolation Forest
   - RF05: Agregação híbrida de scores (regras + ML)
   - RF06: Geração de relatórios detalhados
   - RF07: API RESTful para integração CI/CD

c) Definição de requisitos não-funcionais:
   - RNF01: Tempo de scan < 2 segundos para arquivo típico
   - RNF02: Suporte a arquivos até 10MB
   - RNF03: Cobertura de testes ≥ 85%
   - RNF04: Zero vulnerabilidades SAST críticas
   - RNF05: Hardening de segurança (OWASP Top 10)
   - RNF06: Documentação completa (código + API + usuário)

d) Projeto da arquitetura em pipeline

### 3.2.2 Fase 2: Implementação do Core Engine

**Módulo de Parsing** (terrasafe/infrastructure/parser.py)

Implementação de parser para arquivos Terraform utilizando biblioteca python-hcl2,
responsável por:
- Leitura e validação sintática de arquivos .tf
- Extração de blocos de recursos (resource, data, provider)
- Normalização de estruturas para análise posterior
- Validações de segurança (limite de tamanho, path traversal, timeout)

**Engine de Regras** (terrasafe/application/scanner.py)

Implementação de sistema de detecção baseado em padrões regex para identificar
vulnerabilidades críticas.

### 3.2.3 Fase 3: Implementação do Modelo de Machine Learning

**Feature Engineering**

Desenvolvimento de pipeline de extração de 5 features:
- open_ports_count: Número de portas expostas à internet
- hardcoded_secrets: Indicador de presença de credenciais
- public_access: Indicador de recursos públicos
- unencrypted_count: Número de recursos sem criptografia
- resource_count: Total de recursos definidos

**Modelo Isolation Forest**

Configuração dos hiperparâmetros:
- n_estimators=100
- max_samples='auto'
- contamination=0.1
- random_state=42

### 3.2.4 Fase 4: Sistema Híbrido e Integração

Implementação de sistema de pontuação ponderada:
```
final_score = (0.6 × rule_score) + (0.4 × ml_score)
```

### 3.2.5 Fase 5: Hardening de Segurança e Deployment

Implementação de melhorias de segurança:
- Autenticação via API key com bcrypt
- Validação robusta de entrada
- Cache seguro (Redis)
- Infraestrutura de produção (PostgreSQL, Prometheus/Grafana)

### 3.2.6 Tecnologias Utilizadas

| Camada | Tecnologia | Versão | Justificativa |
|--------|-----------|--------|---------------|
| Linguagem | Python | 3.11+ | Ecossistema ML, produtividade |
| Framework Web | FastAPI | 0.104+ | Performance, async, docs automáticas |
| ML Framework | scikit-learn | 1.3+ | Implementação Isolation Forest estável |
| Parser IaC | python-hcl2 | 4.3+ | Suporte completo HCL2 |
| ORM | SQLAlchemy | 2.0+ | Async support, type safety |
| Database | PostgreSQL | 15+ | ACID, performance, extensibilidade |
| Cache | Redis | 7+ | In-memory, distributed |
| Métricas | Prometheus | - | Padrão de mercado |

## 3.3 COLETA E ANÁLISE DE DADOS

### 3.3.1 Datasets de Teste

Desenvolvimento de três configurações Terraform representativas:

1. **vulnerable.tf** - 6 vulnerabilidades intencionais, score esperado: 90-100
2. **secure.tf** - Zero vulnerabilidades, score esperado: 0-20
3. **mixed.tf** - 2 vulnerabilidades médias, score esperado: 40-60

### 3.3.2 Métricas de Avaliação

**Métricas de Eficácia:**
- Acurácia de classificação
- Precisão na detecção de vulnerabilidades
- Taxa de falsos positivos/negativos
- Concordância entre rule-based e ML scores

**Métricas de Performance:**
- Tempo de parsing, scan total, inferência ML
- Taxa de cache hit/miss
- Throughput (scans/segundo)

**Métricas de Qualidade:**
- Cobertura de testes
- Vulnerabilidades SAST
- Dependências vulneráveis

---

**CONTINUA NO CAPÍTULO 4...**
*Ver próximo arquivo para Desenvolvimento e Resultados*
