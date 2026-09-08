# SESSION LOG

## Daily Diary — reverse chronological order

**Project:** CI/CD Pipeline Labs

---

## How to Write an Entry

Append every entry at the **top** of this file (under this header). One entry per session.
Keep it honest and specific: this log is the "memory" that any AI (and you) uses to resume
work instantly. The mentor reviews the latest entry at the start of every session.

### Template

```markdown
## YYYY-MM-DD — Session NN

**Phase / Stage:** Phase X — <phase name> · Stage NN — <stage title>

**Daily recap (start of day):**
- Passed ✅ / Areas to reinforce ⚠️: <what was asked and how it went>

**Worked on:**
- <what was done this session>

**Concepts learned / reinforced:**
- <concept, in your own words>

**Commands / tools used:**
- <command> — why

**Errors encountered:**
- <error> → <what you investigated> → <resolution>

**Questions still open:**
- <question> (if none, write "None")

**Next session (target):**
- <exact next checkbox to complete>

**Commit / push:** `docs(stage-08): ...` — pushed to GitHub ✅ GitLab ✅
```

---

## Entries

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
- Block D pending: relationship between GitHub `needs` and GitLab `stages`.
- `requirements.txt` is unpinned (only `pytest`) — dependency pinning is planned material.

**Next session (target):**
- Recap: close **Block D** (pipeline structure `needs` vs `stages`), then **Block E**
  (containers).
- Then **Stage 08** — the SSH mental model (questions before any command, no VPS created).

**Commit / push:** Pending — memory folder changes to be synced to `C:\Repo2` and pushed
(method, cadence, sticky frames, folder renames).

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
