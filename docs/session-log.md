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
- Block D pending from Session 01 (relationship between GitHub `needs` and GitLab `stages`).
- `requirements.txt` unpinned (only `pytest`).

**Next session (target):**
- Phase 9 — VPS Provisioning: create Oracle Cloud Free Tier account, generate VPS key
  pair, provision Ubuntu server, connect for the first time.

**Commit / push:** Pending — memory folder changes (session log, AGENTS.md, execution
plan, stage-08 complete) to be synced to `C:\Repo2` and pushed.

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
