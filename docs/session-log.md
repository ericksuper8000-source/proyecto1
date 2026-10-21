# SESSION LOG

## Daily Diary — reverse chronological order

**Project:** CI/CD Pipeline Labs

---

## How to Write an Entry

Append every entry at the **top** of this file (under this header). One entry per session.
Keep it honest and specific: this log is the **permanent memory** that any AI (and you)
uses to resume work instantly. The mentor reviews the latest entry at the start of every
session and consults the per-concept question bank to avoid exact duplication.

### Template — v4 (2026-10-21 — current)

A session has three blocks: **review (3–5 concepts) → practice (one objective) → documentation**.
Use the v3 concept cycle inside the review: one concept per row, canonical explanation +
example/analogy, explicit connection, "todo claro" gate, one verification question, verdict
(solid/partial/fragile). **No general summary and no full delivery-story dump.** Log what was
built, what was learned, what was confusing, tomorrow's review queue, and actual timings.
Commit/push only if the student explicitly asks. See the Session 06 entry (2026-10-21) for
the canonical concept explanations; Session 07 for the v4 process definition.

### Template — v2 (historical, superseded by v3)

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

**Rules for the log (v4):**
- **3–5 concepts per session** (hard cap 40 min), not the whole map. Never log a general
  summary dump; log **concept by concept**.
- One row/step per concept: explanation/analogy, connection, comprehension check, student's
  questions, **one verification Q&A**, and verdict (solid/partial/fragile) are mandatory.
- Question wording must differ unless marked `refuerzo útil ⏰`; consult the bank first.
- The `Work session` section is **also permanent memory** — its concepts become future review
  topics. Include what was learned, what was confusing, evidence, and tomorrow's review queue.
- Record actual review/practice/documentation timings when they differ from the standard.
- Commit/push are logged only when they actually happen; sync-only is the default.

---

## Entries

---

## 2026-10-21 — Session 07 (Process definition — daily session model v4)

**Phase / Stage:** Phase 9 — VPS Provisioning · Stage 09 — Pending (documentation only)

**Session type:** Definition and documentation of the new daily session model. No concepts
reviewed, no practical work, no Stage 09 checkboxes marked.

**Decision — time budget (student delegated the decision):**
- Standard day: **120 min** → 5 open + 30 review + 70 practice + 15 documentation.
- Heavy day (new infrastructure): **150 min max** → 5 + 35 + 90 + 20.
- Minimum day: **45–60 min** → 15 review of 2 concepts + 25–35 practice + 5–10 docs.
- **5 days/week** + 45–60 min weekly consolidation. No daily 3-hour routine.

**Daily contract v4:**
1. **Review (3–5 concepts, hard cap 40 min):** fragile yesterday → new yesterday → today's
   dependencies → one older concept from the rotation map. One concept at a time, canonical
   explanation + analogy, connection, "todo claro" gate, then one verification question
   (purpose + connection + failure mode). Verdict: **solid / partial / fragile**.
   Partial → reinforce the gap; fragile → re-teach with another analogy, requeue tomorrow,
   and do not unlock dependent practical work until reinforced.
2. **Bridge concept:** if a missing prerequisite appears, create a short bridge explanation
   or schedule a new canonical concept; log it.
3. **Practice (one objective):** next execution-plan checkbox; state why, plan, evidence and
   safe stop; student executes, mentor guides; no full solutions. Blocked >10–15 min → hint;
   still blocked → document and stop safely.
4. **Documentation:** stage report, session-log, execution-plan, ADR if needed, evidence,
   tomorrow's review queue and exact next objective. Sync memory ↔ `C:\Repo2`.
5. **Close:** student explains one thing and names one doubt; unresolved items go first next day.
6. **Commit/push only on explicit request.** Current preference remains sync-only.

**Why not all 18 concepts daily:** the 18/18 pass was a one-time baseline. Repeating it would
consume 2.5–3 h, leave no practice time, and turn the session into a lecture. Retrieval works
better with spaced rotation plus deliberate return of fragile items.

**Canonical material:** concepts 1–18 remain in the Session 06 entry and `delivery-story.md`;
v4 reuses those explanations instead of inventing new ones.

**Files updated:** `AGENTS.md`, `INSTRUCCIONES SESION DIARIA - IA.txt`,
`docs/execution-plan.md`, `docs/session-log.md`, `README.md`.

**Evidence:** documentation diff; no code or infrastructure changes.

**Questions still open:** none about the model. Pending decision: evaluate Block F before
Stage 09, or begin Stage 09 directly.

**Next session (target):**
- **Review next:** first v4 queue, proposed: Registries (Block F — never formally evaluated),
  Compose/Watchtower, SSH/VPS, Dockerfile/.dockerignore. Confirm at session start.
- **Work next:** Block F evaluation, then Stage 09 first checkbox (Oracle Cloud account).

**Question bank update:** no new technical questions; process questions defined for review.

**Commit / push:** none (sync-only preference).

---

## 2026-10-21 — Session 06 (Review-only — v3 interactive format + Concepts 1–18)

**Phase / Stage:** Phase 9 — VPS Provisioning · Stage 09 — Pending (review-only; no new work)

**Session type:** Return after a long break. The student explicitly requested no new topics,
only recap/explanation/quizzes. The student defined the new **v3 interactive format** and
asked for it to be documented permanently. No Stage 09 checkboxes marked.

**Recap log (v3 — one concept at a time):**

| # | Concept | Explanation + analogy | Connection to previous | Student check / questions | Verdict |
|---|---|---|---|---|---|
| 1 | Código fuente (`Principal.py`) | "El código es el guion de la obra; la app ejecutándose es la obra en escena." Explained the three functions and the loop; code is the only real value. | Foundation; no previous concept. Next: dependencies. | "Lo entendí." Student insight: all infrastructure is born from the code; without knowing the app you cannot define dependencies, tests, tools or pipeline. Mentor confirmed and added the professional nuance (generic stages universal, implementation app-specific; company templates are parameterized). | ✅ |
| 2 | Dependencias (`requirements.txt`) | "El código es la receta; `requirements.txt` es la lista de compra con marca y versión exactas; el pipeline es la cocina que compra esa lista antes de cocinar." `requirements.txt` lists **Python packages**, not the Python version; here only `pytest==9.0.3`. `==` pins the exact version. Python 3.11 is defined in `setup-python`, the GitLab image and `FROM python:3.11-slim`. | Code → dependencies: `Principal.py` uses only stdlib; `test_principal.py` needs pytest; the test job installs the list, `pip-audit` audits it, and Docker installs it before copying code. | Student liked the salt analogy and asked what a more ambitious `requirements.txt` contains and which processes it affects. Mentor explained runtime vs dev, version specifiers, transitive deps/lock files, markers, extras, private indexes/hashes, composition; local install, CI tests, security, Docker cache/image, runtime/deploy, reproducibility, supply chain. Student: "es suficiente; no profundizar más." | ✅ |
| 3 | Tests (`test_principal.py` + pytest) | "El código es la receta; `requirements.txt` es la lista de compra; los tests son el catador que prueba el plato antes de que salga." 4 funciones con `assert`; pytest descubre `test_*`; el archivo no importa pytest. | Código → funciones; requirements → pytest; el job `test` ejecuta `pip install -r` + `pytest`; si falla, el job se pone rojo y `docker` no corre por `needs`. | Student asked if tests are a cornerstone, whether all serious projects have them, and if 20 `.py` files require 20 tests. Mentor: la práctica > el nombre del archivo; la mayoría de proyectos de producción tienen tests automatizados, pero no todos; los tests se escriben por comportamiento/riesgo, no por archivo; pirámide de tests; la cobertura es un mapa, no una meta; este proyecto tiene 4 casos básicos y huecos (bucle, división por cero). Student liked it and asked to preserve it. | ✅ (accepted) |
| 4 | Calidad y seguridad (puerta de 7 revisores) | "La cocina tiene inspectores: presentación, legibilidad, etiquetas, higiene y medidas; el plato sale solo si pasan todos." Roles: Ruff (lint rápido), Flake8 (estilo), Black (formato), MyPy (tipos), Pytest (comportamiento), Bandit (seguridad del código), pip-audit (vulnerabilidades de dependencias). | Tests prueban comportamiento; la puerta añade legibilidad, tipos, seguridad y salud de dependencias. GitHub corre `lint`/`test`/`security` en paralelo y `docker` necesita los tres; GitLab va `lint→test→security`. | Student asked to save the stage overview; mentor clarified that this is one concept and each tool will be taught separately. | ✅ (accepted) |
| 5 | Ruff | "Inspector rápido con checklist: ingredientes sin usar, envases sin etiqueta, cuchillos fuera de sitio." Linter estático en Rust; lee sin ejecutar; detecta imports/variables sin usar, nombres no definidos, comparaciones sospechosas, `except` amplios y código muerto. | Lee el código (C1); no ejecuta tests (C3); es el primer inspector de la puerta (C4); se instala en el job `lint`, no en `requirements.txt`. | Student liked it and asked to save it. | ✅ (accepted) |
| 6 | Flake8 | "Corrector de estilo del código: revisa que la receta esté escrita de forma legible y consistente." Linter estático; combina PyFlakes + pycodestyle + mccabe; reporta, no reescribe. | Lee el código (C1); complementa tests (C3); es otro inspector de la puerta (C4); se solapa con Ruff y contrasta con Black (informa vs reescribe). | Student liked it and asked to save it. | ✅ (accepted) |
| 7 | Black | "Planchador/maquetador del código: deja la presentación impecable y siempre igual." Formateador opinionated y determinista; reescribe comillas, espacios, paréntesis y saltos; 88 columnas por defecto. | Lee el código (C1); es otro inspector de la puerta (C4); contraste con Flake8 (informa vs reescribe); se solapa con `ruff format`, que aquí no se usa. | Student liked it and asked to save it. | ✅ (accepted) |
| 8 | MyPy | "Inspector de medidas/unidades: verifica que las recetas usen las mismas unidades antes de cocinar." Chequeador de tipos estático; lee anotaciones; detecta argumentos/retornos incompatibles, `Optional` sin `None`, contenedores/atributos; no ejecuta. | Código (C1); tests runtime vs estático (C3); gate (C4); tipos vs estilo/formato (C5–C7). | Student liked it and asked to save it. | ✅ (accepted) |
| 9 | Bandit | "Inspector de higiene de la cocina: revisa carne cruda junto a la ensalada, productos de limpieza cerca de la comida." Escáner de seguridad estático (SAST); lee el código sin ejecutarlo; busca secretos, `eval`/`exec`, `pickle`, `yaml.load`, `subprocess` con `shell=True`, `os.system`, `assert`, cripto débil; reporta severidad/confianza. | Código (C1); complementa tests (C3); es el inspector de seguridad de la puerta (C4); contrasta con calidad/tipos (C5–C8); pip-audit mirará dependencias. | Student liked it and asked to save it. | ✅ (accepted) |
| 10 | pip-audit | "Inspector de recalls del proveedor: comprueba si los ingredientes traen una alerta sanitaria conocida." Auditor de dependencias; resuelve `requirements.txt` (incluye transitivas) y compara con PyPI Advisory DB/OSV; detecta CVEs conocidos, no código, zero-days, SO, imagen base ni Actions. | Dependencias (C2); pytest y transitivas (C3); cierra el job `security` de la puerta (C4); Bandit mira el código (C9). | Student liked it and asked to save it. | ✅ (accepted) |
| 11 | Git/`.gitignore` | "Git es el álbum de fotos del proyecto; `.gitignore` es la lista de lo que no quieres fotografiar." Git guarda snapshots (working tree → staging → commits); `.gitignore` excluye archivos no trackeados, no los borra; si ya están trackeados, `git rm --cached`. | Código fuente (C1); dependencias (C2); cachés generadas por pytest/MyPy/Ruff (C3–C10); el push es otro tema. | Student liked it and asked to save it. | ✅ (accepted) |
| 12 | YAML/pipelines | "Orden de trabajo de un taller: estaciones, qué se hace en cada una y cuál debe terminar antes." YAML describe datos/configuración (indentación, `clave: valor`, listas con `-`); el pipeline declara eventos, jobs, runners y pasos; `needs`/stages ordenan; el runner ejecuta. | Materializa la puerta (C4); usa dependencias (C2), tests (C3) y herramientas (C5–C10); el YAML se versiona con Git (C11). | Student liked it and asked to save it. | ✅ (accepted) |
| 13 | Flujo del push | "El commit cierra y etiqueta el paquete; el push lo entrega en el edificio central; los inspectores lo abren." `commit` guarda local; `push` envía commits (no working tree) a `github`/`gitlab`; push a `develop` dispara CI; PR a `master` también; GitLab es espejo manual. | Git (C11); despierta YAML (C12); activa la puerta (C4); oficializa C2–C10. | Student liked it and asked to save it. | ✅ (accepted) |
| 14 | Docker/Dockerfile | "Receta → kit de comida sellado → kit abierto y funcionando." Dockerfile es la receta; imagen es el paquete inmutable (Python + deps + código); contenedor es la instancia en ejecución. `FROM`, `ENV`, `WORKDIR`, `COPY`, `RUN`, `CMD`; build cache por capas. | Código (C1) y dependencias (C2); el job `docker` corre tras la puerta (C4/C12/C13); `.dockerignore` y registries son temas aparte. | Student liked it and asked to save it. | ✅ (accepted) |
| 15 | `.dockerignore` | "`.gitignore` decide qué no va al álbum; `.dockerignore` decide qué no va en la caja de envío." Filtra el contexto de build; no borra archivos ni cambia Git; no entra en la imagen por sí solo, lo que entra lo decide `COPY`. | Complementa `.gitignore` (C11) y el Dockerfile/contexto (C14); protege secretos y acelera builds; requirements/código sí entran (C1–C2). | Student liked it and asked to save it. | ✅ (accepted) |
| 16 | Registries | "Almacén de kits de comida sellados; cada kit tiene dirección y etiqueta." Docker Hub, GHCR y GitLab Registry guardan imágenes, no código; login con token, build una vez, `tag` y `push` a cada uno; etiqueta por commit + `latest`. | Git (C11) guarda recetas, registry guarda imágenes; Dockerfile (C14), `.dockerignore` (C15), job tras la puerta (C4/C12/C13); VPS hará `pull`. | Student liked it and asked to save it. | ✅ (accepted) |
| 17 | Compose/Watchtower | "Compose es el director de orquesta; Watchtower es el vigilante nocturno." Compose declara servicios (`app`, `watchtower`) y Engine los monta; Watchtower revisa cada 30s, hace `pull` y recrea el contenedor (no reconstruye). | Dockerfile (C14) crea la imagen, registry (C16) la guarda, Compose la ejecuta; `latest` local simula CD; VPS fijará commit; SSH sigue. | Student liked it and asked to save it. | ✅ (accepted) |
| 18 | SSH/VPS | "El VPS es una casa remota sin recepcionista; SSH es la puerta blindada; la pública es el candado y la privada la llave del bolsillo." VPS = máquina Linux persistente con IP, sin GUI, no un contenedor. SSH = túnel cifrado cliente `ssh` ↔ `sshd` puerto 22; host key la primera vez; autenticación por llaves. | Cierra el recorrido: registry (C16) surte la imagen, Compose (C17) la corre en el VPS; SSH es la puerta de administración; push/gate (C4/C13) antes. | Student liked it and asked to save it. | ✅ (accepted) |

**Concept 2 — canonical explanation (2026-10-21, student-requested permanence):**
- **Correction:** `requirements.txt` does **not** install Python. It lists Python
  packages. The Python version is defined outside: GitHub Actions `python-version: "3.11"`,
  GitLab `image: python:3.11`, Docker `FROM python:3.11-slim`.
- **What it is here:** one line, `pytest==9.0.3`. The `==` pins the exact version; it is a
  test dependency, not a runtime dependency. The app uses only `time` from the stdlib.
- **Analogy to reuse:** the code is the recipe; `requirements.txt` is the shopping list
  with exact brand/version; the pipeline is the kitchen that buys that list before cooking.
  Without a pinned version, each kitchen uses a different salt and the dish changes;
  without the list, the kitchen does not know what to buy.
- **What a more ambitious file contains:** runtime deps; dev/test deps (often in
  `requirements-dev.txt`); version specifiers (`==`, `~=`, ranges); transitive deps and
  lock files; environment markers (`; sys_platform == "win32"`); extras
  (`uvicorn[standard]`); private indexes and hashes; composition (`-r`, `-c`).
- **Processes it affects:** local install/onboarding; CI test job (`pip install -r`);
  security (`pip-audit -r`, Dependabot/Renovate); Docker build (layer cache, image size,
  attack surface); runtime/deploy (what is inside the image); reproducibility/rollback;
  supply chain (pinned versions, hashes, private indexes).
- **Project-specific nuances:** quality/security tools (`flake8`, `black`, `ruff`, `mypy`,
  `bandit`) are installed ad hoc in CI, not pinned in `requirements.txt` — a reproducibility
  gap for a more ambitious project. The Dockerfile installs `pytest` into the runtime image;
  separating runtime/dev requirements or using a multi-stage build is a future optimization.
- **Status:** student said the explanation was sufficient and asked not to go deeper.
  Future reviews must reuse this explanation and the salt analogy, not replace them.

**Concept 3 — canonical explanation (2026-10-21, student-requested permanence):**
- **The cornerstone is the practice, not the filename:** automated, repeatable behavior
  verification. `test_*.py` is only pytest's discovery convention.
- **Do all serious projects have tests?** Most production projects have some automated
  tests, but "all" is too absolute. Prototypes, temporary scripts or exploratory notebooks
  may not; critical systems (money, auth, data, public APIs) normally do. Tests include
  unit, integration, end-to-end, API, load and security tests — not only `test_*.py`.
- **Why they matter:** only tests prove the program does what it promises. Ruff checks
  style, Black format, MyPy types, Bandit security — none proves `suma(2, 3) == 5`. Tests
  are a safety net for refactoring and make CI meaningful. Without tests, a green pipeline
  can publish wrong behavior.
- **20 source files ≠ 20 tests:** tests are written by behavior/risk, not by file count.
  A single test can cross several files; one file can need many cases. Examples: 20 source
  files → 8 test files with 150 cases; or 20 test files with 1 case each; or 5 integration
  files covering cross-file flows.
- **Test pyramid:** many unit tests (fast, isolated), fewer integration tests (several
  pieces together), few end-to-end tests (full flow, slow). Not every file needs a unit
  test: generated code, config, trivial wrappers and one-off scripts often do not.
- **Coverage caveat:** 100% coverage does not mean good tests. Coverage is a map to find
  gaps, not a goal by itself; assertions, edge cases and behavior matter more.
- **Project-specific:** `test_principal.py` has 4 cases for 3 functions. It does not test
  the `while True` loop or division by zero; it is a basic suite, not exhaustive. In a
  20-file project, organize tests by module or feature and add integration tests for flows
  that cross files.
- **Analogy to reuse:** code = recipe; `requirements.txt` = shopping list; tests = the
  taster/quality control at the kitchen pass. You do not need one taster per cook; you put
  checks at the critical points.
- **Connection:** code functions (Concept 1) → pytest dependency (Concept 2) → `test` job
  → a failed test stops `docker` via `needs`.
- **Status:** student liked the explanation and asked to preserve it; no further questions
  at this time. Reuse this explanation; do not expand unless the student asks.

**Concept 4 — canonical explanation (2026-10-21, student-requested permanence):**
- **Scope:** this is the **quality/security gate as one concept**, not the individual tools.
  Each tool will be taught separately (Ruff first, then Flake8, Black, MyPy, Bandit,
  pip-audit).
- **Why the gate exists:** tests prove behavior, not readability, formatting consistency,
  type safety, code security or dependency health. A program can pass tests and still be
  hard to maintain or dangerous to publish.
- **The 7 reviewers and their questions:**
  - **Ruff:** cheap lint errors (unused imports, undefined names, bad practices); in this
    repo it caught disordered imports in `test_principal.py`.
  - **Flake8:** PEP 8 style/readability (spaces, line length, naming).
  - **Black `--check`:** formatting consistency; CI only checks, does not modify.
  - **MyPy:** static type checking without running the program.
  - **Pytest:** behavior tests (already validated as Concept 3).
  - **Bandit:** code security (hardcoded secrets, dangerous calls); excludes tests.
  - **pip-audit:** known vulnerabilities in `requirements.txt`.
- **Quality vs security:** Ruff, Flake8, Black, MyPy and Pytest cover
  correctness/readability/types/behavior; Bandit and pip-audit cover security of code and
  dependencies.
- **Pipeline placement:** GitHub Actions has `lint`, `test` and `security` jobs in parallel;
  `docker` has `needs: [lint, test, security]`. GitLab runs `lint → test → security`. Any
  failure blocks image build/publish. That is the gate.
- **Analogy to reuse:** the kitchen pass with inspectors: presentation, recipe readability,
  ingredient labels/expiry, hygiene and measurements. The dish only leaves if all pass.
  Tests are the taster; the gate adds the inspectors.
- **Nuance:** Ruff/Flake8/Black overlap; a real project may consolidate them. No tool is
  infallible (false positives/negatives); tests and human review are still necessary.
- **Status:** student asked to save this explanation; no further questions at this time.
  Reuse it; teach the individual tools one at a time.

**Concept 5 — Ruff (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it is:** a **static linter** written in Rust. It reads the code without executing
  it and is very fast. It is not a test runner, formatter, type checker, security scanner or
  dependency auditor.
- **What it catches:** unused imports and variables, undefined names, suspicious
  comparisons, overly broad `except`, dead code, f-strings without placeholders and other
  cheap hygiene errors. In this project it flagged an import issue in `test_principal.py`.
- **What it does not do:** run `pytest`, check types (MyPy), scan secrets/dangerous calls
  (Bandit), audit dependencies (pip-audit) or enforce formatting (Black). Ruff also offers
  `ruff format`, but this project does not use it for that.
- **Pipeline placement:** the `lint` job runs `ruff check .`. If Ruff fails, `lint` is red
  and `docker` does not run because of `needs`. Ruff is installed ad hoc in the job, not from
  `requirements.txt`.
- **Configuration:** this repo has no `pyproject.toml`/`ruff.toml`, so Ruff runs its default
  rules. Real projects configure selected/ignored rules, auto-fixes and per-file ignores.
- **Connection:** reads the code from Concept 1; complements tests (Concept 3); is the first
  inspector of the quality gate (Concept 4). It overlaps with Flake8; a real project may
  consolidate them.
- **Analogy to reuse:** the fast inspector with a checklist who catches obvious kitchen
  hazards (unused ingredients, unlabeled containers, knives left out), not the deep quality
  of the dish.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 6 — Flake8 (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it is:** a **static Python linter** that reads code without executing it. It
  combines **PyFlakes** (simple logic errors such as unused imports or undefined names),
  **pycodestyle** (PEP 8 style: spaces, line length, indentation) and **mccabe** (complexity).
  It reports problems; it does **not** rewrite files.
- **What it catches:** lines too long, wrong spacing/indentation, misplaced blank lines,
  unused imports, undefined names, odd comparisons with `None`, empty/overly broad `except`,
  and unnecessarily complex code. With plugins it can check naming, security, etc.; this
  project runs it with default configuration (no `.flake8`, `setup.cfg` or `tox.ini`).
- **What it does not do:** run `pytest`, check types (MyPy), scan secrets/dangerous calls
  (Bandit), audit dependencies (pip-audit) or fix formatting (Black). It tells you something
  is wrong or unreadable; you decide how to fix it.
- **Pipeline placement:** the `lint` job runs `flake8 .` before Black, Ruff and MyPy. If it
  fails, the job stops and `docker` does not run via `needs`. Flake8 is installed ad hoc in
  the job, not from `requirements.txt`.
- **Connection:** reads code from Concept 1; complements tests (Concept 3); is another
  inspector of the quality gate (Concept 4). It overlaps heavily with Ruff; this project uses
  both for learning, but a real project may consolidate. Key contrast with Black: Flake8
  **reports**, Black **rewrites**.
- **Analogy to reuse:** the code style proofreader; it checks that the recipe is written
  legibly and consistently, not whether the dish tastes good (tests) or the ingredients are
  safe (Bandit).
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 7 — Black (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it is:** a **formatter**, not a linter. It rewrites the file to a single consistent
  format. It is opinionated (few options) and deterministic (same input → same output).
- **What it changes:** quotes, spacing, parentheses, line breaks and line length (88 columns
  by default). It normalizes presentation; it does not change logic, rename variables, sort
  imports or fix errors.
- **Local vs CI:** locally `black .` rewrites files. In CI `black --check .` does not modify
  anything; it only verifies the code is already formatted. If it fails, run Black locally,
  review the diff, commit and push again.
- **What it does not do:** run tests, check types (MyPy), scan secrets (Bandit), audit
  dependencies (pip-audit) or detect logic/lint issues (Ruff/Flake8).
- **Pipeline placement:** runs in the `lint` job after Flake8 and before Ruff/MyPy. Failure
  stops the job and `docker` does not run via `needs`. No Black configuration in this repo,
  so defaults apply.
- **Connection:** reads code (Concept 1); is another inspector of the quality gate
  (Concept 4); contrasts with Flake8 (Concept 6): Flake8 **reports**, Black **rewrites**.
  It overlaps with Ruff, which can format via `ruff format`, but here Ruff is only the linter.
  Black uses 88 columns and Flake8 defaults to 79; real projects align them to avoid conflict.
- **Analogy to reuse:** the code's ironer/typesetter: it makes the presentation impeccable
  and consistent, but does not decide whether the recipe is good (tests) or the ingredients
  are safe (Bandit).
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 8 — MyPy (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it is:** a **static type checker**. It reads type annotations and verifies
  consistency without executing the program. It is not a test, formatter or security tool.
- **What it catches:** wrong argument types for annotated functions, wrong return types,
  `Optional` used without checking `None`, incompatible list/dict element types, missing
  attributes and incompatible overrides.
- **What it does not catch:** logic errors, division by zero, tests, style, secrets,
  dependencies. Python does not enforce type hints at runtime; annotations are a promise
  MyPy checks before execution. `division(10, 0)` remains a runtime error, not a type error.
- **Project-specific:** `Principal.py` and `test_principal.py` have **no type annotations**.
  `mypy .` runs in CI, but without annotations its real coverage is limited: many functions
  are `Any` and default MyPy does not deeply check untyped definitions. This is a
  debt/improvement: annotating functions would let MyPy catch `suma("2", 3)` or a wrong
  return type.
- **Pipeline placement:** last step of the `lint` job, after Flake8, Black and Ruff. Failure
  turns `lint` red and `docker` does not run via `needs`. Installed ad hoc in CI, not from
  `requirements.txt`. No MyPy configuration in this repo; real projects configure strictness
  (`strict`, `disallow_untyped_defs`, etc.).
- **Connection:** reads code (Concept 1); complements runtime tests (Concept 3); is another
  inspector of the gate (Concept 4). Tests check real values; MyPy checks type coherence
  before running. Ruff/Flake8 check style/simple logic; Black formats; MyPy checks types.
- **Analogy to reuse:** the kitchen measurement/unit inspector: verifies that a recipe asking
  for 200 grams is not using 200 liters. It does not taste the dish (tests) or check hygiene
  (Bandit).
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 9 — Bandit (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it is:** a **static security scanner** for Python (SAST). It reads code without
  executing it and looks for dangerous patterns. It is not a test, formatter, type checker
  or dependency auditor.
- **What it finds:** hardcoded secrets/passwords, `eval`/`exec`, unsafe `pickle`
  deserialization, `yaml.load`, `subprocess` with `shell=True`, `os.system`,
  `tempfile.mktemp`, weak cryptography and `assert` in production code. Findings carry
  severity and confidence; not every finding is a real vulnerability, so triage is required.
- **Project-specific:** the `security` job runs
  `bandit -r . -x "./__pycache__,./test_principal.py"`. Tests are excluded because they use
  `assert` intentionally; Bandit flags `assert` because Python removes it under `-O`, so it
  is not a production safety control. No Bandit configuration in this repo; default rules.
- **What it does not do:** detect dependency CVEs (pip-audit), execute the program, test
  logic, check style/types or replace secure design and human review. It can produce false
  positives and false negatives.
- **Pipeline placement:** runs in the `security` job alongside pip-audit. Failure turns
  `security` red and `docker` does not run via `needs`. Installed ad hoc in CI, not from
  `requirements.txt`. Real projects adjust severity/confidence thresholds, skip specific
  checks and justify `# nosec` suppressions.
- **Connection:** reads code (Concept 1); complements tests (Concept 3); is the security
  inspector of the gate (Concept 4). Ruff/Flake8/Black/MyPy cover quality/style/format/types;
  Bandit covers dangerous practices inside the code. pip-audit covers dependencies.
- **Analogy to reuse:** the kitchen hygiene/food-safety inspector: checks raw chicken next to
  salad or cleaning products near food; does not taste the dish (tests) or check supplier
  recalls (pip-audit).
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 10 — pip-audit (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it is:** a **dependency security auditor**. It resolves `requirements.txt`, obtains
  exact versions including transitive dependencies, and compares them with known
  vulnerability databases (PyPI Advisory Database and OSV).
- **Project command:** `pip-audit -r requirements.txt` in the `security` job. It also audits
  pytest's transitive dependencies, not just the single direct pin. A known vulnerability
  turns `security` red and blocks `docker` via `needs`. No configuration or ignored
  vulnerabilities; installed ad hoc in CI.
- **What it finds:** known CVEs/advisories in installed or resolved Python packages.
- **What it does not do:** find errors in your code (Bandit), detect unknown malware or
  zero-days, audit the OS, Docker base image or GitHub Actions, or guarantee a package is
  safe. It only compares against known advisories.
- **Caveat:** `requirements.txt` is not a lock file. pip-audit resolves current versions, so
  results can change if transitive dependencies change. A lock file improves reproducibility
  but is not a security guarantee. Dev dependencies are audited too because they are attack
  surface in CI. Real projects use justified `--ignore-vuln` entries and may use `--fix`.
- **Connection:** dependencies (Concept 2); pytest/transitive deps (Concept 3); closes the
  gate's `security` job (Concept 4). Bandit scans code patterns; pip-audit scans third-party
  packages. Ruff/Flake8/Black/MyPy cover quality/style/format/types.
- **Analogy to reuse:** the supplier-recalls inspector: checks whether ingredients have a
  known health alert. Bandit checks how you cook; pip-audit checks what ingredients you use.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 11 — Git/`.gitignore` (canonical explanation, 2026-10-21, student-requested permanence):**
- **Git:** version-control system that records the project's history. Three zones:
  **working tree** (current files), **staging area** (what `git add` prepares) and
  **repository** (commits, snapshots). `git status` shows changes, staged files and untracked
  files. A commit is local; push is a separate topic.
- **`.gitignore`:** tells Git which **untracked** files not to track. It does not delete
  files. If a file is already tracked, adding it to `.gitignore` has no effect; use
  `git rm --cached <file>` and commit. `git check-ignore -v <file>` shows which rule matches.
- **Project rules:** `_archive/` (planning-only, not public repo), Python caches
  (`__pycache__/`, `*.py[cod]`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`), local
  environments (`.venv/`, `venv/`), OS/editor cruft (`.DS_Store`, `Thumbs.db`, `.idea/`,
  `.vscode/`, `*.swp`, `*~`), sensitive material (`*.key`, `*.pem`, `.env`, `.env.*` with
  `!.env.example`) and `*.log`. Patterns apply top-down; `!` negates.
- **Commit:** source, tests, `requirements.txt`, `Dockerfile`, CI config, `.gitignore`,
  `.gitattributes`, docs and `.env.example`. **Do not commit:** virtualenvs, caches, logs,
  real `.env`/keys or local Docker state.
- **Security caveat:** `.gitignore` is not a security barrier. A secret already committed
  remains in history; rotating it and removing it from history is required. `.gitattributes`
  is separate: it controls line endings (`LF`/`CRLF`), not ignore rules.
- **Connection:** protects source (Concept 1) and dependencies (Concept 2); quality tools
  (Concepts 5–10) generate caches that should be ignored. YAML/push/Docker are separate.
- **Analogy to reuse:** Git is the project's photo album; `.gitignore` is the list of things
  you do not want to photograph: temporary trash, perishable food and private documents.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 12 — YAML/pipelines (canonical explanation, 2026-10-21, student-requested permanence):**
- **YAML:** text format for data/configuration; it declares, it does not execute. Indentation
  defines structure (two spaces, never tabs); `key: value`; `-` lists; quote ambiguous values
  such as `"3.11"` to avoid numeric parsing; quote strings containing `:`.
- **GitHub Actions structure:** `on` triggers (push to `develop`, pull request to `master`;
  a direct push to `master` does not match this `on`); `jobs` (`lint`, `test`, `security`,
  `docker`); `runs-on: ubuntu-latest`; `steps` with `uses:` (prebuilt actions) or `run:`
  (shell; `run: |` for multiple commands); `needs: [lint, test, security]` makes `docker`
  wait for all three.
- **Execution model:** each job starts on a fresh runner, so every job does its own
  `checkout` and installs what it needs. `lint`, `test` and `security` run in parallel;
  `docker` waits. A failed step fails its job; a failed required job blocks dependent jobs.
- **GitLab CI:** different schema, also YAML. `stages: lint → test → security`; each job has
  `stage`, `image` and `script`. Jobs in the same stage run in parallel; the next stage waits.
  Here each stage has one job, so it is sequential. This file is **validation-only**; image
  publishing happens only in GitHub Actions (ADR-0007).
- **YAML vs pipeline:** YAML is the work order/plan; the runner is the workshop that executes
  it. The YAML lives in Git, is reviewed and versioned as code. Tools from Concepts 5–10
  appear as commands inside steps.
- **Connection:** materializes the gate (Concept 4); installs dependencies (Concept 2), runs
  tests (Concept 3), and calls Ruff/Flake8/Black/MyPy/Bandit/pip-audit (Concepts 5–10); the
  YAML is tracked via Git (Concept 11). Push/registries are separate topics.
- **Analogy to reuse:** the workshop work order: stations, tasks and which station must finish
  first; the runner is the workshop.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 13 — Push flow (canonical explanation, 2026-10-21, student-requested permanence):**
- **Commit vs push:** `commit` stores a snapshot in the **local** repository; `push` sends
  those commits to a **remote**. It does not upload uncommitted working-tree changes or
  ignored files.
- **Project remotes:** `github` (GitHub `proyecto1`, main; full pipeline, image publishing)
  and `gitlab` (GitLab `repo2`, mirror/storage; validation-only). No `origin`; push explicitly
  to each remote. `develop` is the working branch; `master` is the stable/showcase branch.
- **Normal flow:** `git status` → `git add <intended files>` → `git commit` → `git fetch
  github` → `git push github develop`. The push triggers the GitHub workflow (`on: push:
  branches: ["develop"]`); `lint`/`test`/`security` run and `docker` runs only if all pass.
  Local checks are rehearsal; the official verdict is remote CI.
- **Mirror:** `git push gitlab develop` separately; Git does not auto-push to all remotes.
- **Branches/PR:** develop → pull request to master; `pull_request` toward master also
  triggers CI. A feature-branch push alone does not trigger this workflow; a direct push to
  master is not in the `on` and must be avoided. Merge to master only after green CI.
- **Practical:** rejected push (non-fast-forward) → fetch/integrate; do not `--force` shared
  branches. `pull` = fetch + integrate; `fetch` only downloads refs. GitHub uses HTTPS/token;
  GitLab uses SSH (`git@gitlab.com:...`); keys/secrets are not in the YAML. At the time of
  this concept, `C:\Repo2` had 8 modified docs **uncommitted**, so a push would not include
  them.
- **Connection:** Git (C11) stores; push wakes YAML (C12) and the gate (C4); only then
  C2–C10 run officially. Registries/Docker publishing are later.
- **Analogy to reuse:** commit seals/labels the package; push delivers it to the central
  building; the pipeline inspectors open it and decide whether it reaches the factory.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 14 — Docker/Dockerfile (canonical explanation, 2026-10-21, student-requested permanence):**
- **Three levels:** Dockerfile = recipe; image = immutable sealed package (Python, deps,
  code); container = running instance of the image. An image is the mold; a container is the
  piece running.
- **Project Dockerfile:** `FROM python:3.11-slim` (base with Python 3.11, not project deps);
  `ENV PYTHONDONTWRITEBYTECODE=1` avoids `__pycache__`; `ENV PYTHONUNBUFFERED=1` makes logs
  immediate; `WORKDIR /app`; `COPY requirements.txt .`; `RUN pip install --no-cache-dir ...`
  during build; `COPY Principal.py .`; `CMD ["python", "Principal.py"]` at container start.
- **Build vs run:** `docker build -t mi-app:latest .` creates the image; the `.` is the build
  context. `docker run --rm mi-app:latest` creates/starts a container; this app prints and
  exits, so the container stops; `--rm` removes it.
- **Layer cache:** changing `Principal.py` reuses the pip-install layer and only redoes the
  code copy. Changing `requirements.txt` invalidates pip install and later layers. That is why
  requirements are copied before code.
- **Project realities/debt:** the image installs pytest because it is in `requirements.txt`,
  although tests are not copied and `Principal.py` uses only stdlib; splitting prod/dev deps
  or multi-stage is an optimization. No `USER` → runs as root; no `EXPOSE` (no port); the
  `python:3.11-slim` tag can move (pin a digest for strict reproducibility); never bake
  secrets into the image.
- **Connection:** packages code (Concept 1) and dependencies (Concept 2); `docker` runs after
  the gate (Concepts 4/12/13); tests are not inside the image; `.dockerignore` and registries
  are separate topics.
- **Analogy to reuse:** Dockerfile = recipe; image = sealed meal kit with ingredients/tools;
  container = that kit opened and running in any Docker kitchen.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 15 — `.dockerignore` (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it does:** filters the **build context** sent by `docker build ... .` before the
  daemon sees it. It does not delete local files, does not change Git tracking and does not
  by itself put/remove files in the image; `COPY` decides what enters the image.
- **Difference from `.gitignore`:** `.gitignore` controls what enters Git; `.dockerignore`
  controls what enters Docker's context. `.dockerignore` can exclude tracked files (e.g.,
  `docs/`); overlap exists but they are not interchangeable.
- **Project rules:** excludes `.git` metadata, Python caches/venvs, logs, OS/editor cruft,
  keys/`.env`, `_archive/`, `docs/`, `screenshots/`, `scripts/`, `CICD.txt`. It must not
  exclude `requirements.txt` or `Principal.py`. Tests may be in the context but this
  Dockerfile only copies the app file; with `COPY . .` they would enter.
- **Benefits:** smaller/faster context, fewer cache invalidations, less risk of secrets.
  Ignored files that change do not invalidate the build context. A secret already baked into
  an old layer is not fixed by adding it to `.dockerignore`; rebuild without it and rotate it.
- **Connection:** complements Git/`.gitignore` (Concept 11) and the Dockerfile/build context
  (Concept 14); code/deps must enter (Concepts 1–2); tests run in CI, not in the image.
  Registries are next.
- **Analogy to reuse:** `.gitignore` decides what stays out of the photo album;
  `.dockerignore` decides what stays out of the shipping box to the workshop.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 16 — Registries (canonical explanation, 2026-10-21, student-requested permanence):**
- **What it is:** a warehouse for Docker images (layers), not source code. Git moves text;
  the registry moves images. A name is `registry/namespace/repository:tag`; without registry,
  Docker assumes Docker Hub.
- **Project registries:** Docker Hub `erickdev8/mi-app` (consumption), GHCR
  `ghcr.io/ericksuper8000-source/mi-app` (GitHub backup), GitLab
  `registry.gitlab.com/ericksuper80-group/repo2` (GitLab backup). Same image in three places
  for redundancy. Only GitHub Actions publishes (ADR-0007); GitLab validates.
- **Job flow:** login to all three with `--password-stdin` and scoped tokens → build once →
  tag with `${GITHUB_SHA:0:8}` and `latest` → `docker tag` for each registry name → `docker
  push` to each. `docker tag` is an alias, not a copy.
- **Security:** use scoped tokens, not account passwords; secrets live in GitHub/GitLab;
  never in YAML/repo; rotate leaked tokens. `--password-stdin` avoids exposing them in
  processes/logs.
- **Tags:** commit tag traces image → code; `latest` is a mutable convention and gets
  overwritten; deploy by commit tag or immutable digest for precision.
- **Push/pull:** push uploads missing layers; pull downloads missing layers; shared layers
  are reused. A failed push fails the job; if another registry already received the image,
  state is partial and rerunning is effectively idempotent for the same tags.
- **Connection:** code in Git (C11/C13); image from Dockerfile (C14); context filtered by
  `.dockerignore` (C15); gate green before publishing (C4/C12). VPS/server will `docker pull`
  later.
- **Analogy to reuse:** registry = warehouse of sealed meal kits; each has an address and
  label; `latest` is “newest on the shelf”; commit tag is the batch number tracing the recipe.
  Git stores recipes; the registry stores kits.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 17 — Compose/Watchtower (canonical explanation, 2026-10-21, student-requested permanence):**
- **Compose:** declarative multi-container tool. `docker-compose.yml` declares `services`;
  Compose asks the Docker Engine to converge to that state. Compose decides, Engine executes.
  It does not build images here (no `build:`); it pulls them from the registry.
- **Project services:** `app` uses `erickdev8/mi-app:latest`, fixed container name,
  `restart: always` (the app loops printing every 5 seconds); `watchtower` uses pinned
  `containrrr/watchtower:1.7.1`, `restart: always`, mounts `/var/run/docker.sock` (powerful,
  sensitive access to Engine), `DOCKER_API_VERSION=1.41` and `command: --interval 30`.
- **Commands:** `docker compose up -d`, `ps`, `logs -f app`, `down`. `up` creates/starts;
  `down` removes containers/network, not images.
- **Watchtower/CD simulation:** every 30s it checks whether a watched container's image has a
  newer version; if so, stops, removes, pulls and recreates it with the same configuration.
  It does not rebuild. Compose does not watch the registry; Watchtower does.
- **`latest` local vs commit tag:** `app` uses `latest` deliberately only locally so
  Watchtower detects changes and simulates CD (ADR-0004). The VPS (Phase 11) will pin the
  commit tag for deterministic deployments. `latest` is not a production best practice.
- **Connection:** Dockerfile (C14) builds, registry (C16) stores, Compose runs, Watchtower
  updates; after gate/push (C4/C13). SSH/VPS is next.
- **Analogy to reuse:** Compose is the orchestra conductor reading the plan; Engine is the
  workshop; Watchtower is the night watchman who checks every 30s and swaps the old meal kit
  for the new one without rebuilding it.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Concept 18 — SSH/VPS (canonical explanation, 2026-10-21, student-requested permanence):**
- **VPS:** a persistent Linux machine in a data center, with its own IP, running 24/7 and
  headless (no monitor/keyboard). It is a virtual machine, **not** a container; Docker runs
  containers inside it. Oracle Cloud Always Free is the planned provider (Phase 9).
- **SSH:** Secure Shell, an encrypted remote-control channel. Client `ssh` on the PC; server
  `sshd` listening on port **22**; gives a remote shell, not a GUI.
- **Connection sequence:** resolve IP → TCP to port 22 → server presents host key → client
  checks `known_hosts` (first time shows the authenticity warning) → encrypted tunnel →
  authentication (password or key) → remote shell; prompt shows the remote hostname.
- **Keys:** public key = padlock left on the server; private key = key that never leaves the
  local machine. Server sends a challenge only the private key can answer; the private key is
  never transmitted. One key per door: GitHub, GitLab and VPS (`id_ed25519_vps`); alias in
  `~/.ssh/config` (`mi-vps`). Never share/commit the private key.
- **First connection:** the warning is normal once; verify the fingerprint and accept; it is
  stored. A later unexplained fingerprint change is an alert (possible MITM). Never accept
  blindly.
- **Headless:** CLI is enough to install Docker, run containers, read logs. Closing SSH does
  not stop the server or containers.
- **Project:** the VPS pulls the image from the registry; it never builds. Compose runs it.
  Local uses `latest` for CD simulation; VPS will pin the commit tag. Phase 9 creates the
  Oracle account/VPS; Phase 10 hardens SSH (keys only, no root, no password).
- **Connection:** push (C13) → gate (C4) → registry (C16) → VPS pulls → Compose (C17) runs;
  SSH (C18) is the administration door.
- **Analogy to reuse:** VPS = house in another city with no receptionist; SSH = armored door
  with intercom; public key = padlock left on the door; private key = the only key in your
  pocket; one key per door.
- **Status:** student liked the explanation and asked to save it. Reuse it; do not expand
  unless the student asks.

**Student insight — permanent principle (documented 2026-10-21):**
- The code defines the stack; the stack defines dependencies, tests, build and pipeline.
  A pipeline cannot be designed without knowing the application. Analogy: you do not
  build the road before knowing whether cars or trains will use it.
- Documented in `AGENTS.md` → "Permanent Engineering Principles" and in
  `docs/delivery-story.md` → "Reglas de Oro" (v2.8).

**New review format — v3 (student decision, permanent):**
- One concept at a time, simple explanation + example/analogy.
- Explicit connection to previously validated concepts.
- Space for comprehension check and student questions; wait for "asimilado y sin
  preguntas" before advancing.
- No large general summaries and no full delivery-story dump; the story is source
  material, told incrementally.
- Optional quiz at the end, one question at a time.
- Mandatory before every work session, especially after a break.
- Documented in `AGENTS.md` (Daily Recap v3 + Session Flow Preference v3) and
  `docs/delivery-story.md` rule.

**Work session:** None — review only. No Stage 09 work.

**Repo state verified (2026-10-21, real `git fetch` to both remotes):**
- `develop` = `github/develop` = `gitlab/develop` = `fe37aa7` (contains the feature6/feature7 commits).
- `github/master` = `2fd2de9`; `gitlab/master` = `8cce10c`; both contain `fe37aa7`; `git diff` between all refs = 0.
- Local `master` = `1dc240a` (behind remotes, content identical); working tree was clean at
  verification time (the docs were synced later and remain uncommitted).
- The earlier `feature6` branch no longer exists locally; its content is on `develop`.

**Questions still open (next review concept):**
- **Review complete:** Concepts 1–18 validated/accepted. Next is **Block F formal
  evaluation** (registries), then **Stage 09** (Oracle Cloud account and VPS).
- Housekeeping: `E:\Datos\IA\CICD - Project\requirements.txt` still says `pytest==8.2.2`;
  the real repo uses `9.0.3`. Decide whether to update the memory-folder copy during sync.

**Next session (target):**
- **Review next:** none pending in the current v3 list; run Block F formal evaluation.
- **Work next:** Stage 09 Session 1 (Oracle Cloud account, Always Free quotas), with the VPS
  key `id_ed25519_vps` and `~/.ssh/config` alias `mi-vps`.

**Question bank update:** Concepts 1–18 validated/accepted; no evaluation question consumed
yet. Last exact repeat: none. Canonical Concept 2–18 explanations recorded above; reuse them.

**Commit / push:** Memory files updated locally in `E:\Datos\IA\CICD - Project`
(`AGENTS.md`, `README.md`, `docs/execution-plan.md`, `docs/session-log.md`,
`docs/delivery-story.md`, `docs/learning-roadmap.md`, `docs/environment.md`,
`INSTRUCCIONES SESION DIARIA - IA.txt`). **Synced to the `C:\Repo2` working tree on
2026-10-21** (student chose sync-only; includes the Concept 2–18 updates). **Not
committed/pushed yet** — pending explicit commit instruction.

---

## 2026-10-01 — Session 05 (Recap-only — Block D pipelines validated ✅, debt closed)

**Phase / Stage:** Phase 9 — VPS Provisioning · Stage 09 — Pending (recap-only session; Stage 09
still has **zero** checkboxes marked)

**Daily recap (start of day) — per-topic log (1 block, spiral repetition):**

> General journey summary given: script Python → 7 puertas de calidad/seguridad → Git
> espejado GitHub+GitLab → pipelines (GitHub fabrica y publica, GitLab solo valida) →
> Dockerfile con capas ordenadas → la misma imagen en 3 registries → Compose + Watchtower
> como ensayo local de CD → SSH validado (Stage 08 ✅) → hoy se cierra la deuda de Block D
> y después Phase 9 Stage 09.

| # | Block/Topic | Summary + Analogy given by mentor | Comprehension check | Evaluation Qs (varied, 1 at a time) + Your answers + Verdict | Your Qs for this topic | Topic verdict |
|---|---|---|---|---|---|---|
| 1 | **Block D — Pipelines** (`.github/workflows/ci.yml` job `docker` + `.gitlab-ci.yml`) | "El pipeline es el jefe robot que obedece una lista: la lista es el YAML (el papel), el runner es el obrero que la ejecuta. Un espacio mal puesto **tumba la lista** y no se contrata a nadie. En `ci.yml`: `lint`/`test`/`security` son cuadrillas en paralelo y `docker` solo entra si los 3 pasan (`needs` = freno). Cada trabajo va en fila: clonar → Python 3.11 → instalar → correr. En `.gitlab-ci.yml`: turnos, y un turno no arranca hasta que el anterior termina; nadie fabrica (ADR-0007)." + identidad de etiquetas: "el SHA es el **número de serie pintado en la caja**; `latest` es el **letrero de la repisa**, y cada almacén tiene el suyo" | "¿Lo entendiste o necesitas que lo explique diferente?" → "sí entendí continuemos" → Asimilado ✅ | **Q1:** "¿Por qué en `ci.yml` los 3 corren en paralelo y en `.gitlab-ci.yml` en serie? ¿Qué se pierde en cada lado?" → "prácticamente ambos hacen casi lo mismo pero con gramáticas diferentes, ambos evalúan en paralelo... GitLab solo valida y cuando la imagen es creada en GitHub la recibe y guarda en GitLab Registry" → ❌ **dos errores**: (a) GitLab NO corre en paralelo — los turnos son secuenciales por diseño; (b) GitLab NO recibe la imagen — no hay transferencia entre plataformas, son 3 `docker push` dentro del job `docker` de `ci.yml` → gap explicado (GH = paralelo por defecto + dependencia explícita; GL = secuencial por defecto + paralelo dentro del turno; y el coste/beneficio de cada uno) → **Q1b** rephrased (reloj): "si cada turno tarda 40s, ¿cuánto tarda el pipeline y por qué?" → "120 segundos, ya que no corren en paralelo, corren uno detrás del otro" → ✅ correcto | — | ✅ |
| | | | | **Q2:** "¿Por qué 8 caracteres del commit y no `v1` o la fecha? ¿Por qué el mismo texto en las 3 etiquetas?" → "eso no me lo explicaste en tu resumen" → ⚠️ **fallo del mentor** (dado por supuesto en vez de explicado) → explicación completa (identidad de contenido; `latest` es nombre móvil; `v1` es manual y miente; SHA inmutable + `git show`/`git checkout` para reproducir el bug; 8 = convención de `git log` y de `CI_COMMIT_SHORT_SHA`; conmutar de registro con una línea; **deriva silenciosa**) → **Q2b** rephrased (escenario Docker Hub → GHCR con `latest` distintos): "¿qué versión entra, qué descubres al comparar con lo que probaste, y por qué ningún pipeline se puso rojo?" → "no sé, explícame esto bien fácil y corto" → analogía de las **dos cajas selladas** (mismo aspecto, distinto número de serie; cada bodega con su propio letrero) + por qué nada falla (la mentira está en los nombres, no en los sistemas) → **Q2c** rephrased: "si el servidor pide `mi-app:1a2b3c4d` en vez de `:latest`, ¿qué te garantiza?" → "garantiza que el código corre en producción exactamente igual al código que probé" → ✅ correcto + matiz del mentor (son los **mismos bytes**, no "el mismo código" aproximado; cubre **dos** regresiones: la versión equivocada y la versión que ya no existe = **punto de retorno**; conecta con `restart: always` + Watchtower: el `latest` también puede hacer mentir al ensayo local) | — | ✅ |

**Recap meta:** Tema D repetido a propósito — hoy se cerró **la deuda de evaluación que Session 04 dejó abierta**. Sin duplicación literal: no se repitió ni la pregunta de quitar `needs` ni la de "Pytest falla pero igual se publicó" (ambas consumidas en Session 03). Ángulos nuevos: (a) semántica paralelo-vs-serie entre plataformas, (b) identidad de etiqueta y deriva silenciosa.
> **⚠️ Corrección de nombres (regla permanente):** Session 04 registró "Block F — .yml pipelines", pero el mapa canónico de `AGENTS.md` asigna **Block D = Pipelines** y **Block F = Registries**. Hoy se usaron los nombres canónicos. **Block F (Registries) sigue sin evaluarse** — es el bloque de la próxima sesión.
> **⚠️ Registro de evaluación:** hoy respondiste en 2–3 palabras (Q1, Q2, Q2c). En futuras rondas el mentor pide explícitamente la mitad de "qué pasa si" antes de aceptar ✅.

**Recap timing:** ~20 min — 1 bloque (Block D), explicación profunda por el feedback del 2026-09-29. Sin trabajo de etapa (el estudiante cerró el día tras validar el tema: "no tengo preguntas, pero quiero terminar aquí por hoy").

**Work session (today's build — feeds future recaps):**
- **What we built / did:** nada de código. Sesión de repaso puro.
- **Concepts newly learned / deepened:** semántica de ordenamiento por plataforma (GitHub DAG con `needs` explícito vs GitLab turnos secuenciales); coste en tiempo de reloj de los turnos secuenciales; identidad de imagen por SHA vs `latest` móvil; **deriva silenciosa entre registries** (nada falla, todo verde, tres software distintos bajo el mismo nombre); SHA como punto de retorno y como garantía de "mismos bytes"; por qué el rojo del pipeline es la alarma que evita la deriva.
- **Commands / tools used:** ninguno.
- **Decisions made:** regla recordada — **`:latest` solo local; en el VPS siempre el SHA** (consistente con el comentario ya existente en `docker-compose.yml` y con ADR-0004/ADR-0007). Se agregaron 2 analogías nuevas a las Sticky Frames de `AGENTS.md` para futures recap.
- **Errors encountered:** ninguno técnico. Dos errores de comprensión detectados y corregidos (paralelismo en GitLab; "GitLab recibe la imagen") + un fallo del mentor (explicación dada por supuesta en el resumen).
- **Evidence:** N/A (recap-only).

**Questions still open (for next recap rotation):**
- **Block F — Registries** (canónico): *nunca evaluado*. Ángulos no preguntados todavía: verbos `tag`/`push`/`pull` sobre la misma imagen; `--password-stdin` (por qué el secreto no va en la línea de comandos); token vs contraseña; qué es un registry cuando el disco del runner muere.
- **Refuerzo (débil hoy):** semántica paralelo-vs-serie entre las dos plataformas; identidad de etiqueta / deriva `latest` vs SHA.

**Next session (target):**
- **Recap next:** **Block F (Registries)** — 1 bloque, preguntas variadas, reutilizando las analogías "bodegas / caja sellada / número de serie vs letrero".
- **Work next:** Phase 9 — Stage 09 **Session 1: cuenta Oracle Cloud (Always Free), cuotas, Always Free vs créditos de prueba**. Stage 09 sigue con 0 checkboxes marcados.
- **Housekeeping pendiente:** decidir si se descartan las variables `GHCR_USERNAME`/`GHCR_TOKEN` de GitLab CI — ADR-0007 las volvió innecesarias y la "Next session target" de `execution-plan.md` todavía las menciona.

**Question bank update:** Added Qs: D-Q1-parallel-vs-serial-platforms (❌ → corregido → **D-Q1b-wall-clock-timing** ✅), D-Q2-why-8char-commit-tag (⚠️ no explicado → explicación completa → **D-Q2b-silent-drift-hub-to-ghcr** ❌ → analogía dos cajas → **D-Q2c-sha-guarantee** ✅), D-Q3-block-letter-naming-correction. Last exact repeat: none.

**Post-cierre (2026-10-01) — auditoría del estado real del repo `C:\Repo2` (findings):**
> El estudiante dijo que el commit/push ya estaba hecho. **El mentor NO había hecho ningún
> commit ni push en la sesión** — solo edité 3 archivos markdown en la carpeta de memoria. Se
> auditó el repo en lugar de asumir, y aparecieron 4 hallazgos.
- **H1 — Los 7 commits de hoy (2026-10-01) no están documentados.** Tocan **solo `nuevo.py`**:
  `eb0c9ca` (add) → `99a1434` → `0968c30` → `ffe257c` → `0618ba0` → `c533b6e` → `dc41430`
  (format). No son progreso del proyecto y no tienen entrada en este log. Además sus mensajes
  (`feature3 commit 0` … `feature4 commit 1`) violan la convención de *conventional commits*
  del `AGENTS.md` → defecto de portafolio.
- **H2 — `nuevo.py`: NO era una regresión — decisión del estudiante (cerrado).** La Session 04 lo
  borró por higiene (`fd6c212`) y hoy volvió a entrar (`eb0c9ca` + 6 commits). El mentor lo
 Catalogado como regresión y recomendó borrarlo + `.gitignore`. **El estudiante decide lo contrario: es un
  archivo de práctica deliberado y se queda en el repo.** Verificado que el impacto es nulo: el
  `Dockerfile` hace `COPY Principal.py .`, así que **nunca entra en la imagen ni llega a producción**.
  Trade-off real y aceptado: pasa por las 7 puertas de CI en cada push (de ahí el commit
  `dc41430 fix: format nuevo.py to pass linting`). Corrección de perspectiva del mentor: el
  defecto nunca fue el archivo, fue que estaba **sin documentar y por accidente**. → regla
  reescrita en `AGENTS.md` (Repo Hygiene #1): la regla es *documentar*, no *ignorar*.
- **H3 — Estado de refs (VERIFICADO con `git fetch` real a los dos remotos):**
  `develop` = `dc41430` = `github/develop` = `gitlab/develop` ✅ · `master` = `f51df86` =
  `github/master` ✅ · `gitlab/master` = **`2ce2b11`** ✅. **Las 6 refs tienen contenido idéntico**
  (`git diff` = 0 en todos los pares) y `develop` es ancestro de todas. **Nada está
  desincronizado.**
  > **Los 68 commits de merge que "sobran" en `gitlab/master` son divergencia normal de espejo**:
  > GitLab crea un merge cada vez que subes `master` allí. Dos espejos pueden tener **historiales
  > distintos con contenido idéntico**. La única verificación válida es `git diff` entre refs = 0,
  > nunca "¿los SHA se ven iguales?".
  > **SSH a GitLab funciona:** `id_ed25519_gitlab` + el bloque `Host gitlab.com` de `~/.ssh/config`
  > → `Welcome to GitLab, @ericksuper80!`. Una llave por puerta, como en Stage 08.
- **H4 — Pipelines: RESUELTO.** El estudiante confirma que **todo está verde** (pruebas +
  lint + security) en `dc41430`, después del commit que formatea `nuevo.py`. Los 6 commits
  anteriores de esa serie pueden conservar runs rojos en el historial — irrelevante para
  producción (lo que despliega es HEAD) pero visible para quien lea la lista de runs como
  entrevistador.
- **⚠️ FALSO POSITIVO DEL MENTOR — 2ª vez, misma causa que el hallazgo F-01 de la Session 04.**
  Primero afirmé que el historial de la Session 04 faltaba del repo: **falso**, venía de mirar solo
  `git log -5` (sí están `1cdcb04`, `90a343d`, `17892b8`, `25a0c8d`…). Después afirmé que
  `gitlab/master` estaba stale y sin verificar, y culpé a la llave del estudiante: **también falso**,
  el remoto estaba en `2ce2b11` desde el principio. Causa raíz del segundo: el propio
  `GIT_SSH_COMMAND='ssh -o BatchMode=yes'` del mentor bloqueó el `fetch` —la confirmación de
  `AddKeysToAgent` requiere interacción, así que murió el diálogo y quedó un `publickey` falso— y
  luego el ref de seguimiento viejo se tomó como si fuera el remoto.
  **Reglas permanentes:** (a) *un remoto no se conoce hasta hacer `fetch`; un remote-tracking ref es
  la memoria de Git sobre el remoto, no el remoto*; (b) *nunca escribir el estado de un remoto en la
  documentación a partir de un ref de seguimiento*; (c) *no añadir `BatchMode` a un `fetch` de
  diagnóstico*, porque impide distinguir "llave rota" de "falta confirmación". → añadidas a
  `AGENTS.md` (Repo Hygiene #3 y #4).
- **Sync + commit + push (por instrucción del estudiante):** Copiados los archivos de memoria a
  `C:\Repo2/docs/` (incluido `docs/delivery-story.md` no rastreado). Commit `0b15177`:
  `docs(session-05): close Block D recap, repo audit + student decision on nuevo.py, sync delivery-story v1.0`
  (5 archivos: +343/−35). Push a `github/develop` ✅ y a `gitlab/develop` ✅. Los master remotos ya
  contenían `develop` (fusionado por el estudiante a `github/master`=`1dc240a`, `gitlab/master`=`74102e8`).
  `master` local actualizado por FF desde `github/master` sin reescribir historia. Verificación con
  `fetch` real: todas las refs con contenido idéntico (`git diff develop <cualquiera master/*>` = 0) y
  `develop` ancestro de todos los master. La divergencia de historia en `gitlab/master` (68 merges)
  es normal para espejos con push a master por ambos lados. Working tree limpio en `develop`.

**Commit / push:** memoria actualizada 2026-10-01 (este log, `execution-plan.md`, `environment.md`,
`AGENTS.md`). **Nada commiteado ni pusheado por el agente.** Último commit que toca
`docs/session-log.md` en `C:\Repo2` = `371303a` (2026-09-29). Pendiente: sync + commit + push a
GitHub y GitLab (lo hace el estudiante).

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
- **Pipelines tras el fix:** ✅ **verde confirmado por el estudiante en GitHub Y GitLab**
  (incluidos los pipelines disparados por los pushes a `master` — lint/test/security).
  Sesión con cero pendientes.

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
