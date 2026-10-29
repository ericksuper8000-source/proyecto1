# Stage 12 — Deployment: immutable tag, CD over SSH, rollback

> **Phase:** Phase 12 — Deployment (route v2)
> **Estimated duration:** 2–3 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stages 09–11 complete. ADR-0013 (release strategy).

---

## Objective

Make the pipeline deliver to the server with a **verified, immutable artifact**, a
post-deploy healthcheck, and a **practiced rollback** — never by hand, never `:latest`.

## Scenario (real world)

*"Push a change. We want it on the server in minutes. And if it breaks, we want the
previous version back while you investigate — not after."*

## Concepts (why first)

- **Immutable tag:** the server pins the commit SHA tag. `:latest` is a pointer that
  moves without evidence; the SHA tag is what was tested and what can be rolled back.
- **Compose on the server, build in CI:** the server clones only the compose file and
  pulls the image — the server never compiles anything.
- **Scoped deploy key:** a dedicated SSH key, read-only, limited to this repository.
  If it leaks, it can only read one repo, never push code or touch other machines.
- **Post-deploy healthcheck:** deploy is not "done" when `up -d` returns; it is done
  when `curl /health` answers. The pipeline verifies what the user will hit.
- **Rollback:** redeploy the previous tag. Because deploys are one-line, rollback is
  one-line — but it must be *practiced* (drill with measured time).

## Checklist

### Session 1 — First deployment

- [ ] Generate the scoped deploy key; add to GitHub as a deploy key (read-only)
- [ ] Server clones the repo (compose file only, `--depth 1`)
- [ ] `.env` on the server (chmod 600); secrets never in Git
- [ ] Compose pins the immutable SHA tag
- [ ] `docker compose pull && up -d` → `curl <ip>/health` → 200 (evidence)

### Session 2 — CD over SSH

- [ ] CD job in GitHub Actions: SSH → pull → up -d → curl `/health`; runs on push to
      `develop` and on tags
- [ ] Deploy key + server host/user as CI secrets (least privilege)
- [ ] A real change deployed end-to-end via `git push` (evidence: diff in the response)

### Session 3 — Rollback & reboot drills

- [ ] **Rollback drill:** deploy a deliberately broken tag → healthcheck fails → deploy
      previous tag → `/health` 200 → record total recovery time
- [ ] Write the rollback runbook (3 steps, exact commands)
- [ ] **Reboot drill:** restart the server → app + db come back (`restart: always`)

### Close-out

- [ ] Mentor Questions answered; evidence; session log; execution-plan updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. Why does production never consume `:latest`?
2. What can a leaked deploy key do — and not do?
3. Why is `docker compose up -d` not the end of a deploy?
4. What makes rollback safe? How fast is yours (measured)?
5. Why does the server clone only the compose file?

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `docker compose pull && docker compose up -d` | Deploy the pinned tag |
| `curl <ip>/health` | Verify the deploy |
| `git log --oneline -3` | Identify the previous tag for rollback |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> In your own words: the difference between "container started" and "service healthy",
> and why rollback is a drill, not a hope.

### Evidence

- [ ] First deploy: `curl /health` → 200
- [ ] CD job green from a real `git push`
- [ ] Rollback drill timings + runbook
- [ ] Reboot drill evidence
- [ ] Session log + execution plan updated; memory folder synced

> 🚀 **Next:** Stage 13 — Hardening: Nginx, HTTPS, backups.
