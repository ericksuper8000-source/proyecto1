# Stage 09 — Deploy Journal: Product, FastAPI, MySQL & CI/CD v2

> **Phase:** Phase 9 — Deploy Journal (product-first)
> **Estimated duration:** 6–8 sessions
> **Status:** ⬜ Pending — Current
> **Prerequisites:** Phases 0–8 complete. **ADR-0015** (product), **ADR-0016**
> (product-first derivation), ADR-0010 (multi-arch), ADR-0012 (MySQL 8),
> ADR-0013 (CI/CD v2), ADR-0008 (why the app comes before deployment).

---

## Objective

Build the **product first**: Deploy Journal, a small deployment-history service
(Python + FastAPI + MySQL 8) with a `/health` endpoint, tests, a container, and the
upgraded CI/CD v2 gates — deriving every stack choice and pipeline element from the
product's requirements (ADR-0016). **No server is touched in this stage.**

## Scenario (real world)

The team says: *"We need something we can actually ship and operate. It must record
every deployment we make, show the history, and tell us if it's alive. And the pipeline
must be built around this product — not the other way around."*

## Concepts (why first)

- **Product-first (ADR-0016):** scope → behaviors → data → API contract → stack →
  dependencies → tests → tooling → container → pipeline. No tool enters without a
  requirement or risk it addresses.
- **Data model:** `environments` and `deployments`; why each column, index and FK exists.
  The data defines the API.
- **`/health` with a DB check:** the endpoint later phases depend on — Nginx, CD
  post-deploy gate, Uptime Kuma, monitoring.
- **API key on writes:** the pipeline writes to the journal; the endpoint must be
  protected. Secret in CI + server `.env` (ADR-0013).
- **Config harmony:** Black 88 vs Flake8 79 — one `pyproject.toml`.
- **Pinned tooling:** `requirements-dev.txt` makes CI reproducible.
- **Multi-arch (ADR-0010):** buildx/QEMU for amd64+arm64 — required by the free ARM VPS.
- **Smoke test:** running the image and curling `/health` proves runtime, not just build.
- **Supply chain:** Trivy, Dependabot, gitleaks, pre-commit — each mitigates a named risk.

## Checklist

### Session 1 — Data model

- [ ] MySQL schema: `environments(id, name)` seeded dev/prod;
      `deployments(id, version, environment_id FK, status ENUM, message, deployed_by,
      created_at)` with indexes
- [ ] Init script (SQL) + explain every column/index/FK
- [ ] `schema.sql` versioned; how it will be applied locally (compose init)

### Session 2 — API contract

- [ ] FastAPI app + uvicorn; `GET /health` (returns DB status)
- [ ] `POST /api/deployments` (X-API-Key), `GET /api/deployments` (limit/filter),
      `GET /api/deployments/{id}`, `GET /api/stats`
- [ ] Pydantic models/validation; `/docs` OpenAPI visible
- [ ] `GET /` timeline page (Jinja2 or static HTML + fetch); no frontend framework

### Session 3 — Tests

- [ ] Unit tests for stats/logic
- [ ] API tests with `TestClient` (httpx)
- [ ] **MySQL service container in CI** for integration tests
- [ ] Coverage gate ≥ 80 % on app code (pytest-cov)

### Session 4 — Stack & tooling derivation

- [ ] `requirements.txt` (runtime: fastapi, uvicorn, sqlalchemy/pymysql…) vs
      `requirements-dev.txt` (pinned: pytest, httpx, coverage, ruff, black, flake8, mypy,
      bandit, pip-audit, pre-commit, gitleaks)
- [ ] `pyproject.toml`: Black 88 / Flake8 88 + E203,W503 / Ruff / MyPy + type hints
- [ ] `.env.example` committed; `.env` ignored; `X-API-Key` value documented as secret

### Session 5 — Container & local stack

- [ ] Dockerfile v2: non-root USER, HEALTHCHECK, EXPOSE 8000, pinned base digest
- [ ] `docker-compose.yml`: app + MySQL 8 (named volume, internal port only)
- [ ] `docker compose up` → `curl /health` → ok (evidence)

### Session 6 — CI/CD v2 (ADR-0013)

- [ ] Docker job gated to `push` (develop) + `tags`; `:latest` only from tags
- [ ] Smoke-test job: build → run → curl `/health` → 200
- [ ] pip cache; `permissions:`; `concurrency`; `timeout-minutes`
- [ ] Trivy image scan (fail HIGH/CRITICAL); Dependabot config; gitleaks; pre-commit

### Session 7 — Multi-arch & publish

- [ ] buildx + QEMU: `linux/amd64,linux/arm64`; manifest pushed to the 3 registries
- [ ] `docker manifest inspect` shows both platforms (evidence)

### Session 8 — Product demo evidence

- [ ] Timeline page renders recorded deployments (screenshot/GIF)
- [ ] Pipeline deploys the image locally via compose and records a deployment (the loop)
- [ ] Mentor Questions answered; session log; execution-plan updated; memory synced

---

## Mentor Questions

1. Why does the product define the stack and the pipeline (ADR-0016)? Give one example.
2. Who consumes `/health`, and what happens if it lies?
3. Why is the API key on the write endpoint, and where does it live?
4. Why do Black and Flake8 conflict by default, and how does `pyproject.toml` fix it?
5. What does the smoke test prove that `docker build` does not?
6. Why do we need arm64 images (ADR-0010)?
7. What does each supply-chain tool protect: Trivy, Dependabot, gitleaks, pre-commit?

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `uvicorn app.main:app` | Run the service |
| `pytest --cov` | Tests + coverage gate |
| `docker compose up -d` | Local stack (app + MySQL) |
| `docker buildx build --platform linux/amd64,linux/arm64` | Multi-arch image |
| `docker manifest inspect` | Verify both platforms |
| `trivy image …` | Scan the image for CVEs |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> In your own words: how the product requirements determined the stack, the tests, the
> container and every pipeline job — and why nothing here was chosen "because it's cool".

### Evidence

- [ ] Schema + explain every column/index
- [ ] `/docs` (OpenAPI) screenshot + `curl /health` output
- [ ] Tests green with MySQL service container in CI
- [ ] Pipeline green (GitHub + GitLab) screenshots
- [ ] `docker manifest inspect` output
- [ ] Smoke-test log showing `curl /health` → 200
- [ ] Timeline page with a recorded deployment (screenshot/GIF)
- [ ] Session log + execution plan updated; memory folder synced

> 🚀 **Next:** Stage 10 — VPS Provisioning with Terraform + cloud-init (the server is
> sized from this product, ADR-0016).
