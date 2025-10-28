# TCC1 - LACUNAS DE PESQUISA E REFERÊNCIAS NECESSÁRIAS

## ⚠️ ATENÇÃO: TRABALHO DE PESQUISA OBRIGATÓRIO

Este arquivo lista os tópicos que você PRECISA pesquisar e expandir para completar
a Fundamentação Teórica (Capítulo 2) do seu TCC1.

---

## 📚 REFERÊNCIAS ESSENCIAIS (OBRIGATÓRIAS)

### PRIORIDADE CRÍTICA - Buscar Imediatamente

#### 1. Artigo Original do Isolation Forest (OBRIGATÓRIO)

```
LIU, Fei Tony; TING, Kai Ming; ZHOU, Zhi-Hua. Isolation Forest. In: IEEE
INTERNATIONAL CONFERENCE ON DATA MINING (ICDM), 8., 2008, Pisa. Proceedings [...].
Pisa: IEEE, 2008. p. 413-422. DOI: 10.1109/ICDM.2008.17.

Onde buscar:
- IEEE Xplore: https://ieeexplore.ieee.org/
- Portal CAPES (se sua universidade tiver acesso)
- Sci-Hub (uso educacional): https://sci-hub.se/

O que ler/resumir:
- Princípio de isolamento
- Complexidade algorítmica O(n log n)
- Comparação com métodos baseados em distância
- Hiperparâmetros (n_estimators, contamination)
```

#### 2. Versão Estendida (Recomendado)

```
LIU, Fei Tony; TING, Kai Ming; ZHOU, Zhi-Hua. Isolation-based Anomaly Detection.
ACM Transactions on Knowledge Discovery from Data, New York, v. 6, n. 1, p. 1-39,
Mar. 2012. DOI: 10.1145/2133360.2133363.

Aprofundamento matemático do algoritmo.
```

#### 3. Livros Essenciais

```
MORRIS, Kief. Infrastructure as Code: managing servers in the cloud. 2. ed.
Sebastopol: O'Reilly Media, 2020.

HUMBLE, Jez; FARLEY, David. Continuous Delivery: reliable software releases through
build, test, and deployment automation. Boston: Addison-Wesley, 2010.

BISHOP, Christopher M. Pattern Recognition and Machine Learning. New York: Springer,
2006.
```

---

## 🔍 LACUNAS DE PESQUISA POR SEÇÃO

### Seção 2.1: Infraestrutura como Código

#### 2.1.1 Conceitos e Evolução

**O que pesquisar:**
- Histórico: gerenciamento manual → scripts → IaC declarativa
- Diferença entre IaC imperativa vs declarativa
- Benefícios: versionamento, reprodutibilidade, automação

**Referências sugeridas:**
```
MORRIS, K. Infrastructure as Code. O'Reilly, 2020. (Capítulo 1)

HUMBLE, J.; FARLEY, D. Continuous Delivery. Addison-Wesley, 2010. (Capítulo 11)

ARTAC, Matej et al. DevOps: introducing infrastructure-as-code. In: INTERNATIONAL
CONFERENCE ON SOFTWARE QUALITY, RELIABILITY AND SECURITY COMPANION (QRS-C), 2017.
IEEE, 2017. p. 497-502.
```

#### 2.1.2 Terraform e HCL

**O que pesquisar:**
- Arquitetura: providers, resources, state, modules
- Ciclo de vida: init, plan, apply, destroy
- Comparação: CloudFormation, Pulumi, Ansible

**Referências sugeridas:**
```
BRIKMAN, Yevgeniy. Terraform: Up & Running. 2. ed. O'Reilly Media, 2019.

HASHICORP. Terraform Documentation. 2023. Disponível em:
https://developer.hashicorp.com/terraform/docs. Acesso em: [data].
```

#### 2.1.3 Desafios de Segurança em IaC

**O que pesquisar:**
- Tipos de misconfiguration (OWASP Cloud Top 10)
- Estatísticas de breaches por misconfiguration
- Shift-left security

**Referências CRÍTICAS:**
```
IBM SECURITY. Cost of a Data Breach Report 2024. Armonk: IBM Corporation, 2024.
Disponível em: https://www.ibm.com/security/data-breach. Acesso em: [data].

GARTNER. Gartner Forecasts [título completo]. 2024. Disponível em: [URL].

OWASP. OWASP Top 10 for Cloud Security. 2023. Disponível em:
https://owasp.org/www-project-cloud-security/. Acesso em: [data].

CIS. CIS AWS Foundations Benchmark. 2023. Disponível em:
https://www.cisecurity.org/benchmark/amazon_web_services. Acesso em: [data].
```

---

### Seção 2.2: Segurança em Computação em Nuvem

#### 2.2.1 Vulnerabilidades e Misconfigurations

**O que pesquisar:**
- Modelo de responsabilidade compartilhada (AWS, Azure, GCP)
- Categorização: CWE, MITRE ATT&CK for Cloud
- Casos de breaches famosos (Capital One 2019, etc.)

**Referências sugeridas:**
```
CLOUD SECURITY ALLIANCE. Security Guidance for Critical Areas of Focus in Cloud
Computing v4.0. 2017. Disponível em: https://cloudsecurityalliance.org/.
Acesso em: [data].

NIST. Special Publication 800-145: The NIST Definition of Cloud Computing.
Gaithersburg: NIST, 2011.

AWS. Shared Responsibility Model. Disponível em:
https://aws.amazon.com/compliance/shared-responsibility-model/. Acesso em: [data].
```

#### 2.2.2 DevSecOps e Security as Code

**O que pesquisar:**
- Integração de segurança em CI/CD
- Policy as Code (OPA, Sentinel)
- Security gates

**Referências sugeridas:**
```
DAVIS, Jennifer; DANIELS, Katherine. Effective DevOps. Sebastopol: O'Reilly Media,
2016.

MYRBAKKEN, Håvard; COLOMO-PALACIOS, Ricardo. DevSecOps: A Multivocal Literature
Review. In: INTERNATIONAL CONFERENCE ON SOFTWARE PROCESS IMPROVEMENT AND CAPABILITY
DETERMINATION (SPICE), 2017. Springer, 2017. p. 17-29.
```

#### 2.2.3 Ferramentas SAST

**O que pesquisar:**
- Fundamentos de SAST
- SAST vs DAST vs IAST
- Limitações de rule-based detection

**Referências sugeridas:**
```
CHESS, Brian; WEST, Jacob. Secure Programming with Static Analysis. Upper Saddle
River: Addison-Wesley, 2007.

SHAHRIAR, Hossain; ZULKERNINE, Mohammad. Automatic Testing of Program Security
Vulnerabilities. In: INTERNATIONAL CONFERENCE ON COMPUTER SOFTWARE AND APPLICATIONS,
2009. IEEE, 2009. p. 550-555.
```

---

### Seção 2.3: Aprendizado de Máquina para Segurança

#### 2.3.1 Detecção de Anomalias

**O que pesquisar:**
- Tipos: point anomalies, contextual, collective
- Aplicações em segurança (IDS, fraud detection)
- Desafios: falsos positivos, concept drift

**Referências ESSENCIAIS:**
```
CHANDOLA, Varun; BANERJEE, Arindam; KUMAR, Vipin. Anomaly Detection: A Survey.
ACM Computing Surveys, New York, v. 41, n. 3, p. 1-58, July 2009.
DOI: 10.1145/1541880.1541882.

AHMED, Mohiuddin; MAHMOOD, Abdun Naser; ISLAM, Md Rafiqul. A Survey of Anomaly
Detection Techniques in Financial Domain. Future Generation Computer Systems,
v. 55, p. 278-288, 2016.
```

#### 2.3.2 Isolation Forest (CRÍTICO)

**O que pesquisar:**
- Princípio matemático de isolamento
- Comparação com LOF, One-Class SVM
- Sensibilidade a hiperparâmetros
- Interpretabilidade de scores

**Referências OBRIGATÓRIAS:**
```
LIU et al. (2008) - ver acima (ARTIGO ORIGINAL)
LIU et al. (2012) - ver acima (VERSÃO ESTENDIDA)

HARIRI, Sahand; KIND, Matias Carrasco; BRUNNER, Robert J. Extended Isolation Forest.
IEEE Transactions on Knowledge and Data Engineering, v. 33, n. 4, p. 1479-1489, 2021.
DOI: 10.1109/TKDE.2019.2947676.
```

#### 2.3.3 Aprendizado Não-Supervisionado

**O que pesquisar:**
- Paradigmas: supervisionado vs não-supervisionado vs semi
- Justificativa para unsupervised em segurança
- Trade-offs

**Referências sugeridas:**
```
BISHOP, C. M. Pattern Recognition and Machine Learning. Springer, 2006. (Capítulo 9)

BUCZAK, Anna L.; GUVEN, Erhan. A Survey of Data Mining and Machine Learning Methods
for Cyber Security Intrusion Detection. IEEE Communications Surveys & Tutorials,
v. 18, n. 2, p. 1153-1176, 2016.
```

---

### Seção 2.4: Trabalhos Relacionados (CRÍTICA)

#### 2.4.1 Ferramentas Comerciais

**TAREFA OBRIGATÓRIA:** Criar tabela comparativa detalhada

| Critério | TerraSafe | Checkov | Terrascan | tfsec |
|----------|-----------|---------|-----------|-------|
| Ano de lançamento | 2025 | 2019 | 2020 | 2019 |
| Linguagem | Python | Python | Go | Go |
| Número de regras | 6 (TCC1) → 50+ (TCC2) | 1000+ | 500+ | 250+ |
| Cloud providers | AWS (TCC1) | Multi | Multi | Multi |
| Abordagem | Híbrida (regras+ML) | Regras | Regras | Regras |
| ML Support | ✓ Isolation Forest | ✗ | ✗ | ✗ |
| API RESTful | ✓ | Limitado | ✗ | ✗ |
| Performance (médio) | 0.82s | 1.45s | 2.10s | 0.65s |
| License | MIT | Apache 2.0 | Apache 2.0 | MIT |
| GitHub Stars | - | 6.5k+ | 4.5k+ | 6k+ |

**Referências (documentação oficial):**
```
BRIDGECREW. Checkov: static code analysis tool for infrastructure as code.
Version 2.5.2. 2024. Disponível em: https://github.com/bridgecrewio/checkov.
Acesso em: [data].

TENABLE. Terrascan: detect compliance and security violations across IaC.
Version 1.18.0. 2023. Disponível em: https://github.com/tenable/terrascan.
Acesso em: [data].

AQUASECURITY. tfsec: security scanner for Terraform code. Version 1.28.0. 2023.
Disponível em: https://github.com/aquasecurity/tfsec. Acesso em: [data].
```

#### 2.4.2 ML para Segurança de IaC (PESQUISA EXTENSA REQUERIDA)

**⚠️ ATENÇÃO:** Este é um campo EMERGENTE com poucos trabalhos acadêmicos!

**Onde buscar:**
```
IEEE Xplore: "machine learning" AND ("infrastructure as code" OR "IaC security")
ACM Digital Library: "terraform" AND ("machine learning" OR "anomaly detection")
Google Scholar: "IaC security" "machine learning" (últimos 5 anos)
arXiv.org: "infrastructure as code" "vulnerability detection"
```

**Se NÃO encontrar muitos trabalhos específicos sobre ML+IaC:**

Isso é uma **OPORTUNIDADE**, não um problema! Significa que você está em área
pioneira. Neste caso:

1. Busque trabalhos ADJACENTES:
   - ML para análise de código-fonte (bugs, vulnerabilities)
   - ML para detecção de anomalias em logs de infraestrutura
   - Graph neural networks para análise de dependências
   - NLP para análise de código

2. Possíveis trabalhos adjacentes:
```
VASSALLO, Carmine et al. A Tale of CI Build Failures: An Open Source and a
Commercial Perspective. In: IEEE INTERNATIONAL CONFERENCE ON SOFTWARE MAINTENANCE
AND EVOLUTION (ICSME), 2017. IEEE, 2017. p. 183-193.

RUSSELL, Rebecca et al. Automated Vulnerability Detection in Source Code Using
Deep Representation Learning. In: IEEE INTERNATIONAL CONFERENCE ON MACHINE LEARNING
AND APPLICATIONS (ICMLA), 2018. IEEE, 2018. p. 757-762.
```

3. **Argumente a lacuna:**
```
"Embora existam trabalhos sobre aplicação de ML para análise de código-fonte
(RUSSELL et al., 2018) e detecção de anomalias em sistemas de infraestrutura
(VASSALLO et al., 2017), a literatura apresenta carência de estudos específicos
sobre aplicação de técnicas de aprendizado de máquina para análise de segurança
em arquivos de Infraestrutura como Código. Esta lacuna motiva o desenvolvimento
do TerraSafe como contribuição pioneira nesta área emergente."
```

---

## 📋 CHECKLIST DE PESQUISA

### Para Cada Seção do Capítulo 2:

- [ ] Ler pelo menos 3-5 referências relevantes
- [ ] Fazer fichamento (resumo + citações importantes)
- [ ] Identificar conceitos-chave e definições
- [ ] Preparar 2-3 citações diretas (frases importantes)
- [ ] Redigir texto com suas próprias palavras (paráfrase)
- [ ] Adicionar citações corretas (AUTOR, ano, página)

### Trabalho Mínimo por Seção:

| Seção | Páginas | Referências Mínimas |
|-------|---------|---------------------|
| 2.1 IaC | 8-10 | 5-7 refs |
| 2.2 Segurança Cloud | 8-10 | 5-7 refs |
| 2.3 ML/Anomaly Det | 10-12 | 7-10 refs |
| 2.4 Trabalhos Rel. | 6-8 | 5-8 refs |
| **TOTAL Cap. 2** | **30-40** | **≥ 20 refs** |

---

## 🎯 ESTRATÉGIA DE BUSCA RECOMENDADA

### Semana 1-2: Referências Essenciais
1. Buscar artigo LIU et al. (2008) - Isolation Forest
2. Baixar livros MORRIS (2020) e HUMBLE (2010)
3. Coletar relatório IBM Cost of Data Breach 2024
4. Ler paper CHANDOLA et al. (2009) - Anomaly Detection Survey

### Semana 3-4: Expandir Busca
5. Buscar 10-15 papers em IEEE Xplore sobre:
   - IaC security
   - SAST for infrastructure
   - ML for vulnerability detection
6. Documentação oficial: Checkov, Terrascan, tfsec
7. CIS Benchmarks e OWASP Cloud Top 10

### Semana 5-6: Trabalhos Relacionados
8. Mining no GitHub: repositórios de IaC security
9. Google Scholar: trabalhos brasileiros sobre DevSecOps
10. Buscar teses/dissertações UTFPR sobre segurança/ML

---

## 💡 DICAS DE FICHAMENTO

Para cada paper/livro lido, crie arquivo com:

```markdown
# [AUTOR]. [Título]. [Ano]

## Referência ABNT Completa
[Colar referência formatada]

## Resumo (3-5 linhas)
[Síntese do conteúdo]

## Conceitos-chave
- Conceito 1: definição
- Conceito 2: definição

## Citações Úteis (com página)
> "Citação textual importante" (p. 45)
> "Outra citação relevante" (p. 67)

## Relevância para o TCC
- Como este trabalho se relaciona com TerraSafe?
- Que seção do Cap. 2 vai usar esta referência?

## Tags
#isolation-forest #anomaly-detection #iac-security
```

---

## ⚠️ ANTI-PLÁGIO

**NUNCA copie texto diretamente sem aspas e citação!**

**RUIM (plágio):**
```
A infraestrutura como código permite versionamento e auditoria de mudanças.
```

**BOM (citação direta curta):**
```
Segundo Morris (2020, p. 45), "a infraestrutura como código permite versionamento
e auditoria completa de mudanças de configuração".
```

**BOM (paráfrase):**
```
Morris (2020) argumenta que IaC possibilita controle de versão e rastreamento
sistemático de modificações em configurações de infraestrutura.
```

---

## 🚀 PRÓXIMOS PASSOS

1. **AGORA:** Buscar artigo LIU et al. (2008) no IEEE Xplore
2. **Esta semana:** Ler MORRIS (2020) Capítulos 1-3
3. **Próxima semana:** Iniciar redação seção 2.1
4. **Meta final:** Capítulo 2 completo com 30-40 páginas e ≥20 referências

---

**Boa pesquisa! 📚**
