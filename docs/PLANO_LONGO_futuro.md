# Long-term plan — after TCC2 ships

Revised 2026-07-10 against the real state of the final manuscript and code.

Once the short plan lands (TCC2 defended + final version archived), you have two coherent tracks.
Track A protects and compounds what you already built; Track B is where the "autonomous vulnerability
research agent" idea belongs — reframed and scoped so it's actually achievable and thesis-worthy.

The unifying thesis identity across both: **hybrid deterministic + ML/LLM security analysis that finds,
ranks, explains, and fixes issues in CI, gated on reproducibility.** TerraVault is the *static/config*
half; the vuln agent is the *dynamic/memory-safety* half of the same story.

## Ground truth as of 2026-07-21 (use these, not older numbers)
- Final manuscript artifact: 50 pages with Folha de Aprovação on page 3; PDF/A-3b valid by veraPDF
  (`compliant: true`); delivery PDF md5 `7f20a1ae086b2e20593f3fc30c3b9b6a`.
- Pre-approval SIACOES PDF: 49 pages, 703.984 bytes, md5 `d65aed08…`; it declared PDF/A-3b but failed
  veraPDF because link annotations lacked `/F`.
- Test suite: **137 tests, 76,80% line coverage** (`.ratchet.json` → `coverage_pct: 76.8`).
- Rules: 11 · ML features: 8 · default weights: 60% rules / 40% ML (operator-configurable).
- Detection benchmark: TerraVault 100/100/100 · Checkov 100/95,7/97,8 · tfsec 100/87,0/93,0 ·
  Terrascan 100/47,8/64,7 (precision/recall/F1); raw findings 23/187/107/63.
- Ablation (the honest core): **rules alone separate by 33,3 pts; hybrid 21,4; ML alone 3,2.**
  The ML *compresses* the rules' separation — it is an orthogonal out-of-catalog signal, not a
  separation improver. Never restate this as a win.
- ML model `v20260708_015533`: Isolation Forest trained on **35.594 real vectors** (Terraform Registry
  21.746 + GitHub 13.548) — the "synthetic baseline" criticism is already partly retired.
- **A.2 done** (third-party KICS corpus, 57 fixtures the author did not write): TerraVault
  70,4/59,4/64,4 P/R/F1. The decomposition is the result: **83% recall (19/23) inside its rule scope**
  vs **0/9 outside** it. Checkov leads in-scope (96%). The drop from the home 100/100/100 is
  *coverage breadth*, not detection quality — the construct-validity threat is now bounded by data,
  not merely disclosed. Evidence: `evaluation/results/foreign/`.
- **A.3 done** (does the ML win where the rules are silent?): on 18.041 real configs, the **437
  rule-clean** ones show a strictly monotone flag rate along an *independent* Mahalanobis atypicality
  axis — 2,0% (typical half) → 59,8% → 100% → 100% (extreme). **Lift 50,25×**, ranking AUC 0,9151,
  Spearman ρ 0,748. Orthogonality runs the other way too: the IF flags **37,5% of rule-clean** vs only
  **8,9% of rule-flagged** configs. Evidence: `evaluation/results/ml_atypicality/`.
- The ablation above is **unchanged and still must not be spun as a win**: on the *home* corpus the ML
  compresses the rules' separation. A.3 answers a *different* question — in a population the rules say
  nothing about, the anomaly signal is real, orthogonal and selective. Both statements are true; do not
  let the second be quoted as refuting the first.

## Infrastructure constraint (until 2026-07-22)
All heavy compute runs on **GCP via `gcloud` CLI** — the local machine is for basic work only, and the
GCP credits expire on 22/07/2026. Heavy = `make evaluate` (three Docker scanners), full `pytest`, any ML
training or fuzzing. Existing scaffolding: project `terravault`, zone `us-central1-a`, bucket
`gs://terravault-ml-artifacts`, runbook `docs/GCP_TRAINING.md`, scripts `scripts/gcp_*.ps1|.sh`.
Prefer a GCE VM with a startup-script that uploads to GCS and powers itself off, so jobs survive
disconnects. Anything below marked *(GCP)* should not run locally.

---

## Track A — Evolve TerraVault into a real product / publication (weeks → a few months)

Ordered by value-for-effort.

1. **Publish the evaluation as an SBC paper (highest ROI).** The benchmark plus the honest ablation
   (33,3 / 3,2 / 21,4) is already a 6–10 page paper — the ablation *is* the interesting result, because
   "our ML component does not help the way you'd assume, and here is why" is a more publishable finding
   than another 100% table. IN nº 7/2023 Art. 33–34: a Qualis paper *convalidates* TCC, an A-tier one
   scores 10. Art. 37 gives you 6 months of first-author rights. Best next move.
2. ~~**Third-party labeled corpus**~~ — **DONE 2026-07-16/21.** KICS fixtures were chosen precisely
   because KICS is *not* one of the four compared tools, so no tool plays at home. Numbers in the ground
   truth above; harness `evaluation/kics_mapping.py` + `dataset/build_foreign_corpus.py`, report
   `evaluation/results/foreign/report_foreign.md`. What is left is *writing it up*: the in-scope/out-of-
   scope split is the paper-grade finding, and the named coverage gaps (RDS clusters, non-role IAM,
   standalone SG rules, account-level S3) are a concrete, costed roadmap for item 5.
3. ~~**Give the ML something it can actually win at.**~~ — **DONE 2026-07-21. The open question is
   answered: it can.** Where the rules are silent, the Isolation Forest flags the structurally atypical
   decile at 100% and the typical half at 2,0% (lift 50,25×), and it fires *more* on rule-clean than on
   rule-flagged configs — the two signals are genuinely orthogonal. Three honest limits are recorded in
   the report and must travel with the claim: (a) the model trained on essentially all public Terraform,
   so this is an **in-distribution** study — 18.013/18.041 configs reproduce a training vector and there
   is no meaningful held-out real corpus to be had; (b) Mahalanobis↔IF correlation is partly circular by
   construction, so the load-bearing evidence is the orthogonality and the selectivity, not ρ; (c) in
   this sample the atypicality is pure **resource-graph shape** (no top-atypical config had low
   encryption coverage or public exposure), so *structurally unusual is not evidence of vulnerability* —
   the signal is for **prioritising human review**, never an automatic gate.
   **Next on this thread:** threshold calibration. `contamination=0.1` is trained-in, yet 37,5% of the
   rule-clean population trips it; the *ranking* is sound (AUC 0,9151) so the fix is a percentile-based
   cutoff on the anomaly score rather than the raw `predict == -1`, plus a second corpus to check whether
   the 2,0% typical-half rate holds outside this mine.
4. **LLM-assisted remediation (the strategic bridge to Track B).** Add an optional LLM layer that
   (a) explains each finding in plain language and (b) drafts the *fix* as a diff/PR, re-scanning to
   confirm the finding clears before proposing it. Low-risk (findings are already deterministic) and a
   direct prototype of the **patch-drafting** capability the vuln agent needs.
5. **Multi-cloud + module/remote-state coverage.** Azure and GCP rule packs; parse modules and remote
   state. Turns a demo into something adoptable.
6. **Deeper CI/PR integration.** SARIF → GitHub Code Scanning is partly there; add inline PR comments, a
   policy-as-code DSL for org rules, and a severity gate.

---

## Track B — The autonomous vulnerability research agent (master's-thesis / research scale)

**Verdict on the idea:** genuinely strong and current (the space of OSS-Fuzz-Gen, Google's Big Sleep /
Project Zero "Naptime", ClusterFuzz). But as originally written it is 4–5 research projects stacked:
"autonomous", find+repro+rank+patch, memory-safety **and** logic bugs, C/C++ **and** Rust **and** Go, on
**private** codebases. Ship a narrow, credible core first.

### Scope adjustments (before any code)
- **One language family first: C/C++.** Best fuzzer + sanitizer ecosystem (libFuzzer/AFL++ +
  ASan/UBSan/MSan). Rust/Go later.
- **Memory-safety + crashes first; drop "logic bugs" from the MVP.** Fuzzing finds crashes and UB, not
  semantic errors. Re-add a narrow logic-bug class later via differential/property testing **with an oracle**.
- **Open-source targets first, not private code.** Sending proprietary source to a hosted LLM needs
  self-hosted models or strict redaction — a hardening phase, not phase one. Until then, "private
  codebases" is not an honest claim.
- **Don't rebuild fuzzing infra.** Stand on libFuzzer/AFL++, the sanitizers, ClusterFuzzLite/OSS-Fuzz.
  Your contribution is the **LLM layer**, not the fuzzer.
- **Reproducibility as a hard gate.** Report a bug only if a sanitizer confirms it *and* a minimized input
  replays it deterministically. This is TerraVault's "precision by construction" carried forward — and it
  is what separates a thesis from a demo.

### Staged build
- **Stage 0 — Benchmark & baseline.** Ground truth with *known* bugs: Magma, fuzzer-test-suite, or
  historical OSS-Fuzz issues. Establish a plain-fuzzing baseline (bugs found, time-to-repro). Without
  this you cannot claim the LLM added anything — the same discipline as TerraVault's ablation. *(GCP)*
- **Stage 1 — LLM fuzz-harness synthesis.** LLM reads headers/call-graph and writes libFuzzer harnesses.
  Metric: coverage reached and bugs found vs. hand-written and vs. OSS-Fuzz-Gen harnesses. *(GCP)*
- **Stage 2 — Triage + root-cause.** Dedup crashes by stack/sanitizer signature, classify the bug class,
  explain root cause. Metric: dedup accuracy and triage agreement vs. a human-labeled set.
- **Stage 3 — Patch drafting with a verify loop** (the hard, high-value part). Accept a patch **only if**
  it makes the crashing input pass, keeps the test suite green, and survives re-fuzzing. Metric: patch
  correctness / regression rate. You'll have prototyped this in Track A.4. *(GCP)*
- **Stage 4 — Ranking + CI.** Rank surviving bugs by exploitability (sanitizer class, reachability, crash
  type). Wire ClusterFuzzLite into GitHub Actions. SARIF output → unify with TerraVault's reporting.
- **Stage 5 — Hardening for private codebases.** Self-hosted model or redaction pipeline; document the
  data-governance story. Only now is "private codebases" honest.

### The thesis question
"Does an LLM layer over fuzzing+sanitizers measurably improve bug **yield**, **time-to-reproduce**,
**triage quality**, and **patch correctness** versus plain fuzzing and versus OSS-Fuzz-Gen — while
preserving zero false reports via a reproducibility gate?" Defensible, measurable, master's scale.

### Honest risks (name them up front)
- Fuzzing infra is heavy and slow to stand up. Budget for it — and note that after 2026-07-22 the free
  GCP credits are gone, so cost becomes a real design constraint.
- LLM patch correctness is an open problem; the verify loop is what makes it publishable, not a demo.
- Logic bugs remain hard — keep them out of the core claim.
- LLM cost/latency at fuzzing scale: cache, batch, and gate calls behind the repro filter.

---

## Suggested sequencing
1. Ship TCC2 (short plan) → defend → archive the final version (≤10 days after defense, Art. 21 §2º).
2. Track A.1 (SBC paper) + A.4 (LLM remediation) in parallel — the paper credentials you; the LLM
   remediation de-risks Track B's patching.
3. ~~Track A.2 + A.3~~ — **done 2026-07-21**; the science is hardened. Both now have committed evidence
   and a rendered report, and both feed A.1 directly: the paper's contribution is no longer "another
   100% table" but *an honest external-validity bound plus an ablation-driven account of when the ML
   half earns its place*.
4. Open Track B as a master's proposal: C/C++ MVP, Stages 0–3, reproducibility gate as the through-line.

> **Credits status (2026-07-21).** A.2 and A.3 are spent and banked — the two compute-hungry,
> thesis-critical experiments are done, and everything they produced is reproducible from committed
> code (`scripts/gcp_eval_foreign.sh`, `scripts/gcp_ml_atypical.sh`) plus the GCS run ids recorded in
> each result directory. With under a day of credits left, the only remaining item worth the compute is
> **Stage 0 of Track B** (a plain-fuzzing baseline on known-bug targets); it will not complete in the
> window, so treat anything started now as scaffolding, and expect Track B to be planned against paid
> compute from here on. Do **not** spend the remainder re-running A.2/A.3 — their marginal value is now
> in the write-up, not in more samples.
>
> Operational lesson, paid for twice: the A.3 scan died on the 150-min cap because a handful of
> pathological files pinned workers. Any future corpus-scale job must ship with the three guards the
> launcher now has — parallel workers, a per-file `SIGALRM` budget, and a heartbeat that streams partial
> state to GCS so a killed run still leaves a trail.
