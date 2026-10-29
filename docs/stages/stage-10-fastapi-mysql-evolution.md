# Stage 10 — FastAPI + MySQL Evolution (before deployment)

> **Phase:** Phase 10 — FastAPI + MySQL Evolution (route v2)
> **Estimated duration:** 5–7 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Phases 0–8 complete. Phase 9 not required to start coding (the app
> evolves on the local machine first). ADR-0008 (order), ADR-0010 (multi-arch),
> ADR-0012 (MySQL 8), ADR-0013 (CI/CD v2).

---

## Objective

Turn the print-loop script into a real **FastAPI service with MySQL 8 and a `/health`
endpoint**, and upgrade the pipeline to CI/CD v2 — *before* any deployment work, so
the server phases are built once on the final architecture.

## Scenario (real world)

The team says: *"the script is fine, but we need something we can actually ship,
monitor and put behind a proxy. Make it a service with a healthcheck, and make sure
the pipeline can't publish broken or unverified images."*

## Concepts (why first)

- **Why now (ADR-0008):** hardening a print loop is wasted work; the pipeline is born
  from the application. The app reaches its final shape first.
- **`/health`:** the single endpoint every later phase depends on (monitoring, Nginx,
  CD post-deploy checks).
- **Why MySQL 8 (ADR-0012):** aligns with the student's study path; official image is
  multi-arch; simple, free, real backup story.
- **Config harmony:** Black formats at 88 columns, Flake8 defaults to 79 — they fight.
  One `pyproject.toml` fixes it: `max-line-length = 88`, `extend-ignore = E203,W503`.
- **Pinned dev tools:** `requirements-dev.txt` with exact versions makes CI
  reproducible; an unpinned `pip install` is a time bomb (audit C5).
- **Publishing gate (ADR-0013):** PRs must never publish images; `:latest` is only for
  tagged releases. The docker job gets `if: github.event_name == 'push'`.
- **Smoke test:** `docker build` proves nothing about runtime. A CI job runs the image
  and curls `/health` (audit C9).
- **Multi-arch (ADR-0010):** buildx + QEMU build `linux/amd64,linux/arm64` so the image
  runs on the Oracle ARM server.
- **Supply chain (ADR-0013):** Trivy (image CVEs), Dependabot (updates), gitleaks
  (secrets in history), pre-commit (local gate before push).

## Checklist

### Session 1 — The service

- [ ] FastAPI app: `GET /health` → JSON `{"status":"ok"}`
- [ ] `GET /api/suma?a=2&b=3` moving the core functions behind HTTP
- [ ] uvicorn as the server; `EXPOSE 8000` in the Dockerfile
- [ ] Type hints on the app code (MyPy finally has something to check)

### Session 2 — Tests & config

- [ ] API tests with `TestClient` (httpx) + keep the unit tests
- [ ] Coverage gate: `pytest-cov`, ≥ 80 % on app code
- [ ] `pyproject.toml`: Black 88 / Flake8 88 + E203,W503 / Ruff / MyPy — all green
- [ ] `requirements.txt` (runtime) vs `requirements-dev.txt` (pinned tools)

### Session 3 — Database (local dev)

- [ ] MySQL 8 service in `docker-compose.yml` (named volume, port internal only)
- [ ] `.env.example` committed; `.env` ignored (MYSQL_DATABASE/USER/PASSWORD)
- [ ] App connects to MySQL through env-based config
- [ ] `docker compose up` → stack healthy locally

### Session 4 — CI/CD v2 (ADR-0013)

- [ ] Docker job gated to `push` (develop) + `tags`; `:latest` only from tags
- [ ] Container smoke test job: build → run → curl `/health` → 200
- [ ] `permissions:` least-privilege; pip cache in `setup-python`
- [ ] `concurrency` groups; `timeout-minutes` on every job

### Session 5 — Multi-arch & supply chain

- [ ] buildx + QEMU: build `linux/amd64,linux/arm64`; push the manifest to the 3
      registries
- [ ] `docker manifest inspect` shows both platforms (evidence)
- [ ] Trivy scan job (fail on HIGH/CRITICAL)
- [ ] Dependabot config (`dependabot.yml`: actions, pip, docker)
- [ ] gitleaks + pre-commit locally; document the hooks
- [ ] Dockerfile v2: non-root `USER`, `HEALTHCHECK`, pinned base digest

### Close-out

- [ ] Pipeline fully green with the new stack (evidence)
- [ ] Mentor Questions answered; session log; execution-plan updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. Why does the app evolve *before* the server phases (ADR-0008)?
2. Who consumes `/health`, and what happens if it lies?
3. Why do Black and Flake8 conflict by default, and how does `pyproject.toml` fix it?
4. Why must PRs never publish images? What did the audit catch (C2)?
5. What does the smoke test prove that `docker build` does not?
6. Why do we need arm64 images (ADR-0010)?
7. What does each supply-chain tool protect: Trivy, Dependabot, gitleaks, pre-commit?

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `uvicorn app.main:app` | Run the FastAPI service |
| `pytest --cov` | Tests + coverage gate |
| `docker buildx build --platform linux/amd64,linux/arm64` | Multi-arch image |
| `docker manifest inspect` | Verify both platforms |
| `trivy image …` | Scan the image for CVEs |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> In your own words: why a healthcheck changes everything downstream, and what
> "reproducible CI" means after pinning tools.

### Evidence

- [ ] Pipeline green (GitHub + GitLab) screenshots
- [ ] `docker manifest inspect` output
- [ ] Smoke-test job log showing `curl /health` → 200
- [ ] Trivy scan output
- [ ] Session log + execution plan updated
- [ ] Memory folder synced to `C:\Repo2`

> 🚀 **Next:** Stage 11 — Linux Server Administration + Ansible.
