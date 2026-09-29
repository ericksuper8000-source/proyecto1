# SESSION LOG

## Daily Diary — reverse chronological order

**Project:** CI/CD Pipeline Labs

---

## How to Write an Entry

Append every entry at the **top** of this file (under this header). One entry per session.
Keep it honest and specific: this log is the **permanent memory** that any AI (and you)
uses to resume work instantly. The mentor reviews the latest entry at the start of every
session and consults the per-topic question bank to avoid exact duplication.

### Template — v2 (Spiral Repetition + Permanent Memory)

```markdown
## YYYY-MM-DD — Session NN

**Phase / Stage:** Phase X — <phase name> · Stage NN — <stage title>

**Daily recap (start of day) — per-topic log (1–2 blocks, spiral repetition):**

> General journey summary given: <1 sentence — where we started → where we are>

| # | Block/Topic | Summary + Analogy given by mentor | Comprehension check | Evaluation Qs (varied, 1 at a time) + Your answers + Verdict | Your Qs for this topic | Topic verdict |
|---|---|---|---|---|---|---|
| 1 | Block B — Ruff vs Flake8 vs Black | "Ruff=fast guard, Flake8=style police, Black=formatter..." | ¿Entendido? → Asimilado ✅ (or Needed re-explanation → re-explained with X) | Q1: ¿Por qué Black usa --check en CI? → "para no modificar..." → ✅ correct / Q2: ... → ⚠️ gap → rephrased Q2b → ✅ | "¿y Bandit?" → explained: scans secrets... | ✅ |
| 2 | Block E — .dockerignore vs .gitignore | ".gitignore=qué no va a Git, .dockerignore=qué no va al contexto de build..." | Asimilado ✅ | Q1: ¿Qué pasa si .venv va a la imagen? → ... → ✅ | None | ✅ |

**Recap meta:** Topics repeated intentionally for retention; exact question repeated only if flagged `refuerzo útil ⏰`. All Qs above added to permanent bank.
**Recap timing:** 12 min — Blocks B,E (or Actual duration)

**Work session (today's build — feeds future recaps):**
- **What we built / did:** <stage checklist items, commands with why>
- **Concepts newly learned / deepened:** <tool purpose + how it intervenes in flow + failure mode>
- **Commands / tools used:** <command> — why (e.g., `docker build` — creates immutable layers)
- **Decisions made:** <ADR link if any>
- **Errors encountered:** <error> → <hypothesis> → <investigation> → <resolution>
- **Evidence:** screenshots/stage-NN/...

**Questions still open (for next recap rotation):**
- <question> (if none, write "None")

**Next session (target):**
- **Recap next:** <next blocks in rotation, e.g., Block F (registries) + Block C (Git) — with varied Qs, no exact repeat>
- **Work next:** <exact next checkbox, e.g., Phase 9 — generate id_ed25519_vps>

**Question bank update:** Added Qs: [list Q ids / hashes] — Last exact repeat: <none / Q X flagged refuerzo útil>

**Commit / push:** `docs(stage-08): ...` — pushed to GitHub ✅ GitLab ✅
```

**Rules for the log:**
- One row per topic of the day (1–2 rows). Never log "general recap only" — always per-topic.
- The `Summary + Analogy` column is mandatory and becomes source material for future spiral recaps.
- `Evaluation Qs` column must show variety: if a topic repeats, the question wording must differ unless marked `refuerzo útil ⏰`.
- The `Work session` section is **also permanent memory** — its concepts become future recap topics.
- The `Recap meta` + `Question bank update` lines let the next AI instantly avoid duplicate questions while keeping intentional topic repetition.

---

## Entries

---

## 2026-09-29 — Session 04 (Professional audit + approved improvement plan executed)

**Phase / Stage:** Phase 9 — VPS Provisioning · Stage 09 — Pending (audit session, work deferred)
**Recap status:** BLOCK F evaluation NOT closed — session pivoted to audit after student
feedback. Carried to next session.

**Daily recap (start of day) — per-topic log:**

> General journey summary given: full CI/CD flow started review (Block F — `.yml` pipelines);
> student interrupted with feedback: explanations too superficial → methodology reset (now in
> AGENTS.md: deep explanations, one concept → one question → evaluate → doubts → advance).

| # | Block/Topic | Summary + Analogy given by mentor | Comprehension check | Evaluation Qs (varied, 1 at a time) + Your answers + Verdict | Your Qs for this topic | Topic verdict |
|---|---|---|---|---|---|---|
| 1 | Block F — .yml pipelines (deep review, part 1) | Deep explanation of pipeline YAML structure delivered (jobs/steps/needs vs stages), immediately followed by student's methodology feedback — no evaluation round reached today | Feedback given: "explicaciones muy superficiales… hazlo profundo" → mentor reset method + wrote rule to AGENTS.md | None — Block F evaluation pending (restart with varied Qs next session) | Student requested full-flow review before new work → session became the audit (real-world deep review of the whole flow) | ⏳ pending |

**Recap meta:** Topic F started but not evaluated; no exact question consumed today — safe to reuse varied F questions next session.
**Recap timing:** ~10 min (pivoted to audit by request)

**Work session (today's build — feeds future recaps):**
- **What we built / did:**
  1. Full professional audit requested via `C:\Users\XPC\Desktop\Auditoria.txt` (auditor role,
     7 areas) → report delivered with findings F-01…F-15 and improvement plan 1–7 (approved).
  2. Pre-verification: fresh `git fetch` of both remotes → **F-01 was a false positive** (audit
     diffed stale refs): `git diff github/master gitlab/master` = 0 lines, both merges today
     (`838b945` GitHub, `5d356a0` GitLab), develop identical (`5de8f4b`). No force-push needed.
     Lesson: always fetch before comparing remotes.
  3. Local validation of ALL gates with Python 3.11.9 (mirrors CI images): 7/7 green —
     `flake8=0`, `black --check=0`, `ruff=0`, `mypy=0`, `bandit=0`, `pip-audit=0`,
     `pytest=4 passed`.
  4. Fixed what validation found (BEFORE any push):
     - **ruff I001** unsorted imports in `test_principal.py` → imports reordered.
     - **pip-audit PYSEC-2026-1845**: pytest 8.2.2 vulnerable (fix 9.0.3) →
       `requirements.txt` pinned `pytest==9.0.3`.
     - **bandit B101** (assert in tests, Low) → tests excluded: `bandit -r . -x "./__pycache__,./test_principal.py"`.
  5. Rewrote `.github/workflows/ci.yml`: lint += ruff + mypy; new `security` job (bandit +
     pip-audit); `docker` needs `[lint, test, security]`; image tagged `${GITHUB_SHA:0:8}`
     (8 chars = GitLab `CI_COMMIT_SHORT_SHA`) + `latest`, pushed to all 3 registries.
  6. `.gitlab-ci.yml`: stages `lint/test/security` (flake8+black+ruff+mypy, pytest, bandit +
     pip-audit) — validation only. Initial alignment also pushed to the 3 registries with
     `--password-stdin` (F-03), then **re-scoped by student decision → ADR-0007**: GitLab
     is storage + validation, GitHub Actions is the single publisher (commit `17892b8`).
  7. `docker-compose.yml`: watchtower pinned `containrrr/watchtower:1.7.1` (tag verified via
     Docker Hub API, same digest as `latest`); app stays `:latest` **deliberately** with
     comment (Watchtower/ADR-0004 needs it locally; VPS will pin commit tag).
  8. Repo hygiene: `git rm nuevo.py`, untracked 2 `__pycache__/*.pyc` files.
  9. Docs synced: environment.md (pytest 9.0.3, nuevo.py removed, toolchain row),
     execution-plan Current Status + Phase 2/4 checkboxes, evidence files.
- **Concepts newly learned / deepened:** audit as a real full-flow review; `git fetch` before
  any cross-remote comparison (stale refs → false findings); why pins must have no known CVEs
  (pip-audit as CI gate); test files excluded from security scanners (B101 noise);
  cross-platform tag parity (`${GITHUB_SHA:0:8}` ↔ `CI_COMMIT_SHORT_SHA`); `--password-stdin`
  (no password in argv/process list); credentials needed by platform boundaries (GitLab→GHCR
  requires PAT in GitLab CI variables).
- **Commands / tools used:** `git fetch` + `git diff github/master gitlab/master` — prove F-01
  false; `py -3.11 -m flake8/black/ruff/mypy/bandit/pip_audit/pytest` — local mirror of CI;
  Docker Hub API — verify watchtower tag + evidence; GitHub API — verify runs 105–109 green.
- **Decisions made:** 8-char commit tags on both platforms for identical cross-registry tags;
  app image kept `:latest` only in local compose (commented, ADR-0004); security job blocks
  `docker` via `needs` (quality+security before publish); plan 1–7 approved by student;
  **ADR-0007** (student architecture clarification): build once → GitHub pushes to the 3
  registries, GitLab = validation-only storage mirror, **Docker Hub = the consumption
  registry** (compose/VPS pull), GHCR + GitLab Registry = archives/redundancy → no PAT /
  no GHCR variables needed; one concept taught: platform boundary (`GITHUB_TOKEN` only
  exists inside GitHub) → credentials flow follows ownership.
- **Errors encountered:** ruff I001 → fixed imports; pip-audit vuln in our own pin → upgraded
  pytest; bandit B101 in tests → excluded tests (not product code). All three caught locally,
  none reached CI.
- **Evidence:** `screenshots/audit-2026-09-29/01-github-actions-runs-2026-09-29.txt`,
  `02-dockerhub-tags-2026-09-29.txt`, `03-master-sync-verified.txt`,
  `04-local-validation-2026-09-29.txt`

**Questions still open (for next recap rotation):**
- Block F evaluation round (varied Qs: needs vs stages, failure mode if docker runs without
  security, why 8-char tags must match across platforms, --password-stdin rationale).
- Student question pending from feedback flow: GitHub PAT + GitLab CI variables (next step).

**Next session (target):**
- **Recap next:** Block F (`.yml` pipelines, evaluation) + Block G failure modes — varied Qs, deep explanations, 1 question at a time
- **Work next:** Push audit commits (both remotes) → verify run 110+ green on GitHub and new GitLab pipeline green (requires student-created `GHCR_USERNAME`/`GHCR_TOKEN` GitLab variables) → then Phase 9 — Stage 09: Oracle Cloud account

**Question bank update:** Added Qs: F-eval-pending (restart F round), none consumed today — last exact repeat: none

**Post-cierre (mismo día) — incidente Git del estudiante + fix del mentor:**
- **Qué pasó:** el estudiante hizo dos PRs seguidos en GitHub (#67 → `90a343d`, #68 → `a23d1b6`),
  un MR en GitLab (`dbfa163`), y sincronizó `master` → `develop` (`0893f10`). Resultado:
  los dos `master` quedaron **sin** el commit final `1cdcb04` (docs de cierre) — 59 líneas
  detrás de `develop`. NADA perdido: árboles de ambos `master` idénticos entre sí, sin
  commits parásitos, sin PRs abiertos, working tree limpio.
- **Fix aplicado:** `github/master` fast-forward `f173cb1 → 0893f10` (ancestro directo);
  `gitlab/master` no podía ff (el merge del MR no está en `develop` → divergencia de
  historial normal en espejos) así que se creó el merge `a6f3a84` con el mismo árbol.
  Verificación final: `diff` entre los 6 refs = **0 líneas**.
- **Lección (para el banco):** **una sola PR basta** — la PR sigue la rama en vivo; si
  empujas más commits a `develop` la PR abierta los incluye sola. No abrir PR #2.
  `git merge --ff-only` cuando el target es ancestro; merge real cuando no (espejos).
- **Pendiente:** push a `gitlab/master` dispara el pipeline de GitLab en esa rama
  (lint/test/security sin `only:`) — estudiante confirma verde.

**Commit / push:** 7 commits on `develop` 2026-09-29:
`fd6c212` chore(repo) hygiene · `48d5fbd` chore(deps) pytest 9.0.3 · `04c2726` fix(tests)
ruff I001 · `25a0c8d` ci: jobs/tags/3 registries alignment · `05a5256` fix(compose)
watchtower pin · `90a343d` docs(audit) Session 04 · `17892b8` ci(gitlab) validation-only
(ADR-0007) · plus this docs/ADR-0007 sync commit.
Pushed to GitHub ✅ → runs 110–113 all success (4 jobs green each; push + open PR events),
Docker Hub shows `90a343d1` + `latest`. Pushed to GitLab ✅ → pipeline green with
`lint`/`test`/`security`, no `docker` job — **confirmed by student in session**
(evidence `05-gitlab-pipeline-green-confirmed.txt`). Session closed, ADR-0007 architecture
in effect.

---

## 2026-09-10 — Session 03 (Recap-only Blocks D-E, complete ✅ — no work by student decision)

**Phase / Stage:** Phase 9 — VPS Provisioning · Stage 09 — Pending (recap-only session, work deferred by student)

**Daily recap (start of day) — per-topic log (2 blocks, spiral repetition):**

> General journey summary given: small Python script → quality (Ruff/Flake8/Black/MyPy+Pytest) → Git mirrored GitHub+GitLab → pipelines lint+test+build+push → Docker → same image to 3 registries → Compose+Watchtower local → SSH done (Stage 08 ✅) → now Phase 9 Stage 09 VPS.

| # | Block/Topic | Summary + Analogy given by mentor | Comprehension check | Evaluation Qs (varied, 1 at a time) + Your answers + Verdict | Your Qs for this topic | Topic verdict |
|---|---|---|---|---|---|---|
| 1 | Block D — Pipelines | "Pipeline=trabajador automático, runner es quien ejecuta el YAML. YAML=plano, runner=obrero. CI=revisa (lint+test), CD=publica (build+push). GH Actions=jobs+steps+needs, GitLab=stages+jobs+scripts. Secrets en CI, nunca en repo." | ¿Entendido? → First "creo que lo entendi" → Asimilado ✅ | Q1: "Si quitas needs del job docker, ¿qué pasa?" → student rejected as unclear ("¿qué es job docker? ¿docker.yml o ci.yml?") → mentor clarified: job `docker` inside `.github/workflows/ci.yml` (lint/test/docker), rephrased descriptively → A1: "docker section hace login, build, tag x3 hubs, lint valida antes" → ⚠️ partial (missed parallel/failure mode) → explained gap (parallel run, publishes broken) → Q1b rephrased: "Si Pytest falla en division pero igual se publicó, ¿qué le llega al VPS en pull?" → "runner lanza 3 jobs en paralelo, VPS tendría imagen rota" → ✅ correct | "¿qué es job docker? ¿te refieres a docker.yml o yml de github/gitlab? sé más descriptivo" → explained: no docker.yml, job `docker` in `ci.yml` + equivalent in `.gitlab-ci.yml` | ✅ |
| 2 | Block E — Containers + F/G distinction (student-requested) | First: "Dockerfile=receta, imagen=molde congelado inmutable, contenedor=plato vivo. FROM/WORKDIR/COPY/RUN/CMD order matters for cache. Build context + .dockerignore. Desktop=Engine+Compose+BuildKit. Compose decide, Engine ejecuta." Second angle (mudanza chain, liked): "Dockerfile=plano fábrica, pipeline YML=jefe robot, imagen=caja sellada, registries=3 bodegas, compose.yml=plano sala, compose=decorador, Engine=brazos, Watchtower=vigilante nocturno 30s mini-CD local, Desktop=edificio en PC, VPS flow=clone trae plano → Compose pide → Engine pull desde bodega → crea." + "Watchtower=mini-CD mentira vs CD real=pipeline SSH `pull && up -d`" + "Watchtower tonto (¿hay imagen nueva?) vs GitOps inteligente ArgoCD (¿Git==real? + healthcheck + rollback)" | ¿Entendido? → "explícalo diferente, distingue etapas y archivos (dockerfile, compose.yml, compose, engine, repos, yml general, watchtower, desktop, proceso VPS con GHCR/GitLab/Docker Hub)" → re-explained with mudanza chain → "a ver si entendí... ¿papel real watchtower? ¿no lo cumplen otros?" → explained vigilante vs una sola vez → "¿solo local o también VPS?" → explained local-only by decision, prod risk → "¿nunca servicio CD en VPS? ¿cómo lo hacen expertos?" → explained pipeline SSH push-based + GitOps pull-based → "creo que lo entendí bien" → Asimilado ✅ | Evaluation round for Block E deferred (deep Q&A consumed time cap, student validated via own explanation + targeted Qs). Next: 1-2 varied Qs on E (e.g., layers/cache order, .dockerignore vs .gitignore, Compose vs Engine failure mode) | Q1: "¿papel real watchtower si ya hay plano+compose+engine?" → vigilante vs una vez. Q2: "¿solo local o también en VPS?" → solo local por decisión, prod usa SSH. Q3: "¿nunca servicio CD en VPS? ¿cómo expertos sin watchtower?" → push-based SSH + pull-based GitOps. Q4: "guarda esto en memoria como adicional para resúmenes/prácticas futuras" → saved to AGENTS.md Sticky Frames 2026-09-10 | ✅ (understanding validated, evaluation Qs pending) |

**Recap meta:** Topics repeated intentionally (D pending from Session 01 closed today); exact question never repeated (Q1 rephrased descriptively per student feedback "sé más descriptivo"). All Qs below added to permanent bank. New analogies saved to AGENTS.md Sticky Frames as additional future recap material per student request (mudanza chain, mini-CD mentira vs CD real, tonto vs inteligente, lasaña/caché, efímeros vs inmutables, 3 discos, Git vs registry, biblioteca, mercado vs cocina, frescura vs estabilidad, verbos build/run).
**Recap timing:** ~60 min — Blocks D,E (over 15 min cap: extended deep-dive requested by student, all doubts resolved, recap-only session)

**Work session (today's build — feeds future recaps):**
- **What we built / did:** Recap-only by student decision ("No quiero trabajar hoy, solo repaso"). No Stage 09 work started. Closed Blocks D+E validation.
- **Concepts newly learned / deepened:** `needs` ordering prevents publishing broken images; full chain `Dockerfile → YML pipeline → image → 3 bodegas → compose.yml → compose → Engine → Watchtower local vs CD real SSH → VPS pull flow`; layers/cache order (deps first reuses `pip install`); images immutable persist local vs containers ephemeral (`rm` vs `rmi`); 3 disks (PC survives, runner destroyed → mandatory `push`, VPS like PC); Git repo (code, `git pull`) vs registry (images, `docker pull`); `pull` always contacts registry vs `up/run` uses local if present; pros do `pull` then `up` (fail fast, no downtime); local=`versión conocida buena` vs `pull`=cambio consciente; verbs build image / run container.
- **Commands / tools used:** None (recap + documentation). Reviewed `.github/workflows/ci.yml` read-only (jobs lint/test/docker: login+build+tag x3+push).
- **Decisions made:** Added 2026-09-10 Sticky Frames parts 1+2 to AGENTS.md (mudanza + watchtower + cache + persistence + pull/up) — part of this commit. Student asked all of today be reused in future summaries/practices.
- **Errors encountered:** Q1 phrasing unclear ("Si quitas needs...") → student feedback "sé más descriptivo, ¿docker.yml o ci.yml?" → rephrased with file+job names. Logged as permanent rule in AGENTS.md. Misconceptions corrected: order-inversion-breaks-image → explained cache-only; rm-deletes-image → explained rm vs rmi; pull-checks-local-first → corrected pull always contacts, up checks local; up-then-pull order → corrected pull-then-up.
- **Evidence:** N/A (recap-only)

**Questions still open (for next recap rotation):**
- None blocking. D+E validated ✅. Next rotation: Block F (registries auth `--password-stdin`, same image 3 tags, pull on server) + Block C (Git) with varied Qs.

**Next session (target):**
- **Recap next:** Block F (registries) + Block G (Compose/Watchtower failure modes) — with varied Qs, no exact repeat, reuse mudanza/biblioteca/mercado analogies
- **Work next:** Phase 9 — Stage 09 Session 1: create Oracle Cloud account, quotas, Always Free vs trial (deferred from today by student decision)

**Question bank update:** Added Qs: D-Q1-needs-removal-unclear, D-Q1b-descriptive-needs (file+job named), D-Q1c-broken-division-to-VPS-pull ✅, E-Q1-cache-order-inverted-Dockerfile (partial → rephrased E-Q1b-print-only-rebuild ✅), E-Q2-rm-deletes-image (❌ → corrected rm vs rmi → E-Q2b-build-or-run ✅), E-deep-watchtower-role, E-deep-local-vs-VPS, E-deep-experts-no-watchtower, E-deep-3-disks-runner-destroyed, E-deep-pull-vs-up-order, E-deep-local-vs-pull-frescura — Last exact repeat: none (all rephrased, never duplicated)

**Commit / push:** `docs(session-log,agents): close Session 03 recap-only D+E + save mudanza/watchtower/cache/pull-up analogies` — memory folder updated 2026-09-10, to be synced to `C:\Repo2` and pushed to GitHub + GitLab next work session

---

## 2026-08-25 — Session 02 (Stage 08 — SSH mental model + practice + Part C)

**Phase / Stage:** Phase 8 — SSH & Remote Connections · Stage 08 — COMPLETE ✅

**Daily recap (start of day):**
- Recap covered Blocks A-C (Phases 1-7). Passed ✅: general summary of the delivery
  cycle, quality tools, Git & branches.
- Reinforced: SSH concept (canal seguro, puerto 22), host authenticity warning (seguridad
  contra ataques hombre-en-el-medio), public vs private keys (cerradura/llave).

**Worked on:**
- Explained **what SSH is and what problem it solves** (secure tunnel for remote access).
- Explained **why the first connection shows a host authenticity warning** (host key
  verification, man-in-the-middle protection).
- Explained **public key vs private key authentication** (asymmetric cryptography, why it's
  more secure than passwords).
- Explained **why SSH is relevant to this project** (only way to reach the VPS, install
  Docker, clone repo, run compose, deploy).
- Explained **why servers have no GUI** (resources for processing, not peripherals).
- Explained **SSH daemon (sshd)** — the service that accepts connections on port 22.
- Explained **6-step SSH connection process** (DNS → TCP → key exchange → encryption → auth → shell).
- Updated **AGENTS.md** with new Student Session Rules (recap question categories, memory
  of explanations, 3 question categories, no questions on unregistered topics).
- **Practiced with ssh-keygen**: generated practice key pair, inspected both files
  (public and private), deleted them.
- **Fixed private key permissions** on Windows (changed to read-only for user).
- **Decided SSH key strategy for Phase 9**: create third separate key pair (`id_ed25519_vps`).
- **Answered all 7 Part C questions** with mentor validation — all correct.

**Concepts learned / reinforced:**
- SSH = secure shell, encrypted channel over untrusted network.
- Port 22 = the specific port SSH daemon listens on.
- SSH daemon (sshd) = service on server that accepts SSH connections.
- Host authenticity warning = first-time key exchange, man-in-the-middle protection.
- Private key stays on user's machine, never shared; public key goes to server.
- Key-based auth uses challenge-response: server encrypts with public key, private key
  decrypts without ever leaving the machine.
- 6-step connection: DNS → TCP port 22 → host key exchange → encryption negotiation → auth → shell.
- Servers have no GUI to save resources for processing.
- SSH is the only door into the VPS for all future phases (9-14).

**Commands / tools used:**
- `ssh-keygen -t ed25519 -C "practice@demo"` — generated practice key pair
- `cat ~/.ssh/id_ed25519_practice.pub` — inspected public key format
- `cat ~/.ssh/id_ed25519_practice` — inspected private key format
- `rm ~/.ssh/id_ed25519_practice*` — deleted practice keys
- `icacls` — fixed Windows permissions on private key

**Errors encountered:**
- `chmod` didn't work properly on Windows (Git Bash POSIX layer doesn't affect NTFS permissions). Solution: used `icacls` (Windows native tool).

**Questions still open:**
- Block D pending from Session 01 (relationship between GitHub `needs` and GitLab `stages`) — to be closed in next recap with varied Qs.

**Next session (target):**
- Phase 9 — VPS Provisioning: create Oracle Cloud Free Tier account, generate VPS key
  pair, provision Ubuntu server, connect for the first time.

**Commit / push:** `4b31242` — `docs(execution-plan): update Current Status` — pushed to GitHub ✅ GitLab ✅ (2026-09-08). Prior pending from 2026-08-25 resolved via `db953fa`/`4b31242`. `requirements.txt` pin fixed in next commit.

---

## 2026-08-11 — Session 01 (Recap method + first general recap)

**Phase / Stage:** Phase 8 (in progress) · Method change + recap only (no stage work)

**Daily recap (start of day):**
- First general recap run. Passed ✅: **Block A** (cycle + `requirements.txt` + YAML),
  **Block B** (quality tools), **Block C** (Git & branches). Partially covered ⚠️:
  **Block D** (pipeline + CI/CD definitions clear; the structure comparison `needs` vs
  `stages` left pending).
- Reinforced during the round: Python version lives in Dockerfile/setup-python, **not** in
  `requirements.txt`; flake8 is a **linter**, not a formatter; **CI = Continuous
  Integration** (Integración Continua); CD = Delivery / Deployment.

**Worked on:**
- Adopted the **general recap** covering the complete delivery flow (Block A→H) instead of
  only the recent stage. Recorded in `AGENTS.md` (*General Recap Map*) and `execution-plan.md`.
- Refined cadence with the student: recap capped at **~15 min/day** — full simple summary
  every day, **questions from only 1–2 blocks/day** (rotating Mon–Fri), never all 8.
- Saved **Sticky Frames** in `AGENTS.md` (the 4 analogies the student asked to keep in the
  summaries: runner executes the YAML, requirements = app's parts list, compose reads the
  local file then moves to the server, Watchtower = local mini-CD).
- Corrected memory-folder name references to `CICD - Project` and refreshed
  `environment.md` file list (added `.gitattributes`, removed nonexistent `Mapa CI-CD.txt`).
- Reviewed the real repo `C:\Repo2` (read-only): pipelines run Flake8 + Black + Pytest;
  GitHub Actions pushes to the 3 registries, GitLab CI only to Docker Hub. Repo is out of
  sync with the memory changes made today.

**Concepts learned / reinforced:**
- `requirements.txt` = the app's parts list · YAML = the plan, runner = the executor ·
  linter (Ruff/flake8) vs formatter (Black) · `--check` in CI · CI vs CD (Delivery vs
  Deployment) · professional compose flow is automated by a CD pipeline on the server.

**Commands / tools used:**
- None (recap + documentation only).

**Errors encountered:**
- None.

**Questions still open:**
- Block D pending: relationship between GitHub `needs` and GitLab `stages` — carried to next spiral cycle with varied Qs.

**Next session (target):**
- Recap: close **Block D** (pipeline structure `needs` vs `stages`), then **Block E**
  (containers).
- Then **Stage 08** — the SSH mental model (questions before any command, no VPS created).

**Commit / push:** `4b31242` — resolved via `db953fa`/`4b31242` (2026-09-08) — methodology v2 + path fixes. Original `Pending` from 2026-08-11 now synced.

---

## 2026-08-04 — Session 00 (Documentation Architecture)

**Phase / Stage:** Phase 0 — Planning · Created the memory/documentation architecture

**Daily recap (start of day):** N/A — first session with the new structure.

**Worked on:**
- Reviewed the 3 original draft files (Filosofia, Estado actual, Explicacion del proyecto)
  and the real repository (`C:\Repo2`) to capture the verified state of Phases 1–7.
- Moved the original drafts to `_archive/` to keep the root clean.
- Created the full documentation architecture following the Linux DevOps Labs template:
  `AGENTS.md`, `README.md`, `.gitignore`, `INSTRUCCIONES SESION DIARIA - IA.txt`,
  `docs/` (specification, mentor constitution, execution plan, learning roadmap,
  session log, environment, ADRs, stages).
- Recorded decisions as ADRs: 0001 version control from day one, 0002 mirror GitHub +
  GitLab, 0003 multi-registry publishing, 0004 Docker Compose early + Watchtower,
  0005 zero-cost cloud strategy, 0006 English documentation.
- Defined the remaining roadmap: Phase 8 (SSH) → Phase 9 (VPS) → Phase 10 (Linux) →
  Phase 11 (deploy) → Phase 12 (hardening) → Phase 13 (FastAPI) → Phase 14 (portfolio).

**Concepts learned / reinforced:**
- A portfolio is stronger when the repository shows the *evolution*, not just the result.
- An AI mentor can recall project state instantly if a single status file is maintained.
- Phases 1–7 are done; from now on every session starts with the recap ritual.

**Commands / tools used:**
- None (documentation/planning only).

**Errors encountered:**
- None.

**Questions still open:**
- Whether to add Ruff/MyPy to the current CI pipelines (recommended optional improvement).

**Next session (target):**
- Phase 8 — Stage 08: build the SSH mental model (what is SSH, what happens on connect,
  how authentication works) — **before** creating any VPS.

**Commit / push:** N/A — memory folder; will be synced to `C:\Repo2` and pushed in the
first commit of the stage-08 work.
