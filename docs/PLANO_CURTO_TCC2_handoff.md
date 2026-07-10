# PROMPT DE HAND-OFF — Fechar o TCC2 (TerraVault) em nota A+

> **SUPERADO por `ESTADO_TCC2_2026-07-10.md`.** Mantido apenas como registro histórico do plano de 09/07.
> Não use este arquivo como estado atual: ele ainda parte de 49 páginas, ausência da Folha de Aprovação
> e PDF/A pendente, todos corrigidos em 10/07.

> Cole este bloco numa **nova sessão do Claude Code (Opus, max effort)**.
> Reescrito em 2026-07-09 contra o estado real do manuscrito — **a maior parte do plano antigo já foi executada**.
> O que resta é verificação, um apêndice provavelmente desatualizado, e faxina de arquivos.

---

Você vai **FECHAR** o meu TCC 2 — TerraVault, relatório técnico final (Bacharelado em Engenharia de
Software, UTFPR Dois Vizinhos, IN nº 7/2023, Art. 18). O manuscrito já está **quase pronto**: compila
limpo, com figuras reais, tabela de ablação e ameaças à validade escritas. **Não refaça o que já está feito.**

Regra de ouro: **nunca invente número**. Toda afirmação numérica do texto tem de bater com a saída real de
comando. Escreva em PT-BR/ABNT, preservando o tom honesto do texto atual.

## ⚠️ RESTRIÇÃO DE INFRAESTRUTURA (obrigatória até 2026-07-22)
Minha máquina local vive ocupada — **só trabalho básico nela** (ler/editar arquivo, git, compilar texto).
**Todo trabalho pesado roda no GCP via `gcloud` CLI**, nunca localmente:
- pesado = `make evaluate` (baixa e roda 3 imagens Docker: Checkov, tfsec, Terrascan), `pytest` completo,
  qualquer re-treino de ML.
- leve = editar `.tex`, `git`, inspecionar JSON, compilar o LaTeX (use o **Overleaf**, que compila na nuvem).

Infra já existente (`docs/GCP_TRAINING.md`, `.gcp-train.json`): projeto **`terravault`**, zona
**`us-central1-a`**, bucket **`gs://terravault-ml-artifacts`**, scripts `scripts/gcp_setup.ps1`,
`scripts/gcp_train_launch.ps1`, `scripts/gcp_train_status.ps1`. `gcloud` já está no PATH.
Os créditos GCP expiram em **22/07/2026** — use-os.

## Artefatos (ambos em `G:`, nunca salve em `C:` nem em pasta temp)
- **Manuscrito**: `G:\Temp\Template-Relatório-Técnico-BES-UTFPR\`
  (mestre `ModeloTCC.tex`; capítulos `Capitulos/`: `Introducao`, `Fundamentacao`, `Arquitetura`,
  `Avaliacao`, `Resultados`, `Conclusoes`, `ApendiceA`; bibliografia `reflatex.bib`; figuras `Imagens/`).
- **Código**: `G:\Workspace\oguarni\terravault\`
- **Avaliação**: `evaluation/` (`make evaluate` → `evaluation/results/{report.md,metrics.json}`)
- Orientador: Prof. Dr. Newton Carlos Will · Coorientador: Prof. Dr. Marlon Marcon

## Estado real verificado em 2026-07-09 (NÃO refazer)
| Item | Estado |
|---|---|
| Compilação | **49 páginas, 0 erros TeX, 0 refs/citações indefinidas, 0 overfull hbox** ✓ |
| Figuras | **4 figuras reais** (`arquitetura_vector.pdf`, `pipeline_ml_vector.pdf`, `recall_comparativo_vector.pdf`, `score_dispersao_vector.pdf`) + fluxo de dados desenhado em **TikZ**. Sem `dummy.png`. ✓ **Não regerar.** |
| Lista de Siglas | reescrita com as siglas reais (API…VPC) ✓ |
| Tabela de ablação (regras 33,3 / ML 3,2 / híbrido 21,4) | **escrita** (`tab:ablacao`) ✓ |
| Ameaças à validade (circularidade taxonomia↔regras, viés de autor) | **escritas** ✓ |
| Números sincronizados com o modelo re-treinado (49,1 / 27,7 / 35.594 amostras) | ✓ em `Resultados.tex` |
| Severidade do egresso = *Low* · `info` reservado · 11 regras ≠ 11 categorias | ✓ corrigidos |
| Referências (`reflatex.bib`) | prenomes corrigidos (Rashika Singh, Dheer Toprani); venues fracos removidos ✓ |
| "TerraSafe" / `\onelineskip` | eliminados ✓ |
| Apresentação de defesa | **já feita** — fora do escopo |

Modelo atual: `v20260708_015533` (treinado 2026-07-07 22:58, 35.594 amostras reais Registry+GitHub).
`metrics.json` gerado 2026-07-07 23:24. `.ratchet.json` registra `coverage_pct: 76.8`.

---

## TAREFAS — o que realmente falta

### P0 · Apêndice A provavelmente desatualizado (o único ponto falsificável)
`Capitulos/ApendiceA.tex` foi escrito em **02/07 07:13**, mas o modelo foi re-treinado em **07/07 22:58**.
`Resultados.tex` (23:26) e a figura de dispersão (23:28) foram atualizados depois do re-treino — **o apêndice não**.
Ele afirma `score: 84`, `ml_score: 62.27`, `confidence: "MEDIUM"`, 12 vulnerabilidades.

→ Rode a ferramenta com o modelo atual **no GCP** e compare:
```bash
python -m terravault.cli --output-format json test_files/vulnerable.tf
```
Se `ml_score`/`score`/`confidence` mudaram, **regenere o bloco JSON do apêndice com a saída real** e ajuste o
parágrafo introdutório (que cita 84 e 62,27). Se não mudaram, registre a confirmação e siga. **Não force o número.**

### P0 · Reproduzir os números no GCP (verificação, não reescrita)
Suba uma VM que roda tudo, envia os artefatos para o GCS e se desliga sozinha:

```bash
gcloud config set project terravault
RUN=verify-$(date +%Y%m%d-%H%M%S)
gcloud compute instances create "tv-$RUN" \
  --zone=us-central1-a --machine-type=e2-standard-4 \
  --image-family=ubuntu-2404-lts-amd64 --image-project=ubuntu-os-cloud \
  --boot-disk-size=50GB --scopes=cloud-platform \
  --max-run-duration=90m --instance-termination-action=DELETE \
  --metadata=run-id="$RUN",startup-script='#!/bin/bash
set -x; exec > >(tee /var/log/tv.log) 2>&1
RUN=$(curl -s -H "Metadata-Flavor: Google" http://metadata/computeMetadata/v1/instance/attributes/run-id)
apt-get update && apt-get install -y python3-pip python3-venv git docker.io make
git clone https://github.com/oguarni/terravault.git /opt/tv && cd /opt/tv
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pytest --cov=terravault --cov-report=term --cov-report=xml | tee /tmp/pytest.txt
make evaluate | tee /tmp/evaluate.txt
python -m terravault.cli --output-format json test_files/vulnerable.tf > /tmp/apendiceA.json
gsutil -m cp /tmp/pytest.txt /tmp/evaluate.txt /tmp/apendiceA.json coverage.xml \
  evaluation/results/metrics.json evaluation/results/report.md \
  gs://terravault-ml-artifacts/runs/$RUN/
poweroff'
```
Acompanhe de qualquer máquina e colete:
```bash
gcloud compute instances list --filter="name~tv-verify"
gsutil ls gs://terravault-ml-artifacts/runs/          # acha o RUN
gsutil cat gs://terravault-ml-artifacts/runs/<RUN>/pytest.txt | tail -5
gsutil cp -r gs://terravault-ml-artifacts/runs/<RUN>/ .
```
> ⚠️ O modelo treinado (`models/`) **não** vem do `git clone` se estiver gitignorado. Se `ml_score` sair `-1`
> ou o modelo faltar, copie-o para a VM antes de rodar:
> `gsutil cp -r gs://terravault-ml-artifacts/runs/<run-de-treino>/models/ /opt/tv/models/`
> Um `ml_score` de −1 invalida o apêndice — **não publique esse número**.

Confirme **exatamente** contra o texto:
- `137 casos de teste` e `76,80%` de cobertura (`Avaliacao.tex:9`, `Conclusoes.tex:5`, `Arquitetura.tex:353`).
- Detecção: TerraVault 100/100/100 · Checkov 100/95,7/97,8 · tfsec 100/87,0/93,0 · Terrascan 100/47,8/64,7; brutos 23/187/107/63.
- Híbrido: regras 50,0/16,7 · ML 48,7/45,5 · final 49,1/27,7; separações 33,3 / 3,2 / 21,4.
- Tempos 0,66 / 152,08 / 36,49 / 159,65 s.

Divergiu? Atualize **o texto** para o dado real (nunca o contrário) e diga o que mudou.

### P0 · Faxina (`erase`/`sanitize`) — o manuscrito ainda carrega lixo
1. **`Capitulos/Desenvolvimento.tex` está MORTO** — não é mais `\include`-ído (foi dividido em
   `Fundamentacao`/`Arquitetura`/`Avaliacao`), aponta para imagens inexistentes (`Imagens/arquitetura.png`,
   `fluxo.png`, `pipeline_ml.png`) e ainda afirma **"133 testes / 76,67%"**, contradizendo o texto vivo.
   → **Apagar** (o git guarda o histórico).
2. **Imagens não usadas** — só os quatro `*_vector.pdf` entram no PDF. `fluxo_vector.pdf`/`.png` sobraram
   (o fluxo virou TikZ), assim como `arquitetura_vector.png`, `pipeline_ml_vector.png`,
   `recall_comparativo.png`, `recall_comparativo_vector.png`, `score_dispersao.png`, `score_dispersao_vector.png`.
   → Confirme com `grep -rn includegraphics Capitulos/` e mova os órfãos para `Imagens/_unused/` (ou apague).
3. **Artefatos de build** (`.aux .log .out .toc .lof .lot .bbl .blg`) não devem ir na entrega. Compile limpo e
   entregue só o PDF. Adicione um `.gitignore` se o diretório virar repositório.
4. **Dois PDFs idênticos**: `ModeloTCC.pdf` e `TERRAVAULT-SCANNER_HIBRIDO_DE_SEGURANCA.pdf`.
   → Decida qual é o artefato de submissão e elimine a duplicata (evita entregar a versão errada).
5. **`Diretrizes TCC - Relatório Técnico.md`** é material de apoio — não deve estar na pasta de entrega.

### P1 · Refinar a Tabela 5 (quebras de linha feias)
`Tabela~\ref{tab:comparativo}` — "Comparação de características entre as ferramentas"
(`Capitulos/Avaliacao.tex`, p. 34 do PDF) — está com quebras de linha ruins.

**Diagnóstico.** As colunas são `p{3.2cm}p{2.9cm}p{2.4cm}p{1.5cm}p{2.4cm}` = **12,4 cm fixos**, que não
preenchem a `\textwidth`, e colunas `p{}` são **justificadas**. Com a hifenização ativa (`hyphenat` é
carregado *sem* a opção `[none]`), células estreitas — sobretudo `tfsec` com apenas 1,5 cm e
`Terrascan` com "\textit{Policy-as-code} (OPA/Rego)" — partem palavras no meio e abrem buracos entre
palavras. Nem `tabularx` nem `array` estão no preâmbulo.

**Conserto sugerido** (o mais limpo): usar `tabularx` ocupando a largura do texto, com colunas
*ragged-right* (sem justificação → sem buracos nem hífens no meio de célula) e larguras iguais para as
quatro ferramentas, mantendo a primeira coluna fixa e um pouco mais larga.

1. No `ModeloTCC.tex`, adicionar ao preâmbulo: `\usepackage{array}` e `\usepackage{tabularx}`.
2. Em `Avaliacao.tex`, trocar o `tabular` da Tabela 5 por:
```latex
\newcolumntype{L}{>{\raggedright\arraybackslash}X}
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{3.6cm} L L L L@{}}
```
   (mantenha `\footnotesize`, os `\hline` e o `\fonte{}` como estão — é o padrão ABNT do template).
3. Encurtar dois rótulos que forçam três linhas:
   - "\textit{Score} de risco agregado e ponderável" → "\textit{Score} agregado ponderável";
   - "Serviço REST + observabilidade" → manter, mas a célula "\textbf{Sim} (FastAPI, Prometheus/Grafana)"
     pode virar "\textbf{Sim} (FastAPI + Prometheus/Grafana)".
4. Recompilar e conferir: nenhuma palavra hifenizada dentro da tabela, colunas das quatro ferramentas com a
   mesma largura, cabeçalho alinhado, e **0 overfull hbox** (o documento está hoje em zero — não regrida).

> Alternativa mínima, se não quiser mexer no preâmbulo: manter `tabular`, mas aplicar
> `>{\raggedright\arraybackslash}` a cada coluna `p{}` (exige `array`) e rebalancear as larguras para somar
> ~15,5 cm — por exemplo `p{3.6cm}p{3.0cm}p{2.6cm}p{2.2cm}p{2.6cm}`. Resolve os buracos, mas distribui pior.

### P1 · Revisão final antes da defesa
- Reler `Conclusoes.tex` cobrando coerência com os resultados: ela deve dizer, sem rodeios, que **as regras
  isoladas separam melhor (33,3)** e que o ML é **sinal ortogonal** para anomalias fora do catálogo — nunca
  vender o híbrido como ganho de separação. Se destoar de `Resultados.tex:128`, alinhe.
- `Termo de Aprovação`: **manter comentado** no `ModeloTCC.tex` agora. Ele entra na **versão final**,
  entregue em até **10 dias após a defesa** (Art. 21 §2º) — o `TermoAprovacao.pdf` já está na pasta.
- Verifique que `Introducao.tex` (objetivos específicos) casa 1:1 com o que `Conclusoes.tex` declara atingido.

## Critérios de aceite
- [ ] Apêndice A reproduz **exatamente** a saída atual da CLI (ou foi regenerado), com `ml_score` ≠ −1.
- [ ] `137` / `76,80%` / benchmark / híbrido confirmados por saída de comando **rodada no GCP**.
- [ ] `Desenvolvimento.tex` apagado; nenhum `includegraphics` órfão; nenhuma imagem não usada na entrega.
- [ ] Tabela 5 (`tab:comparativo`) ocupa a largura do texto, sem palavra hifenizada dentro de célula.
- [ ] Compila em 0 erros, 0 refs/citações indefinidas, 0 overfull hbox.
- [ ] Um único PDF de entrega; Termo de Aprovação ainda fora.
- [ ] Nenhum número no texto sem comando que o comprove.

Entregue: PDF recompilado + resumo curto do que mudou por item, com evidência (`arquivo:linha` ou saída de
comando) e o `RUN` do GCS usado na verificação. Se algo não puder ser verificado, **diga explicitamente**.
