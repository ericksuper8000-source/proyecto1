# Stage 13 — Production Hardening: Nginx, HTTPS, persistence, backups

> **Phase:** Phase 13 — Hardening (route v2)
> **Estimated duration:** 5–7 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 12 (deploy + CD + rollback working). ADR-0005 (zero cost),
> ADR-0012 (MySQL), ADR-0013 (secrets & rotation).

---

## Objective

Move from "it runs" to "it runs like production": reverse proxy, HTTPS with a **free**
hostname, persistence, log limits, secrets hygiene, and a backup with a **practiced
restore**.

## Scenario (real world)

*"The app works. Now a stranger on the internet will use it. Encrypt the traffic, keep
the data safe, and prove we can recover the database if the server dies tonight."*

## Concepts (why first)

- **Reverse proxy:** the app binds to 127.0.0.1:8000; only Nginx faces the internet on
  80/443. The app is not directly exposed, and TLS is handled in one place.
- **HTTPS with a free hostname:** Let's Encrypt cannot issue free certificates for bare
  IPs. DuckDNS (free subdomain) or sslip.io/nip.io (DNS aliases for IPs) give a valid
  name at $0 (ADR-0005). Auto-renewal = cron/systemd timer + renewal hook.
- **Persistence:** MySQL data in a named volume; containers are ephemeral, data is not.
- **Log limits:** `json-file` with max-size/max-file — otherwise a busy app fills the
  disk and takes the server down.
- **Secrets:** `.env` chmod 600; token scopes documented; rotation procedure written
  (ADR-0013).
- **Backups:** daily `mysqldump` (scheduled container/cron) + off-site copy to a free
  target (Cloudflare R2 free 10 GB / Google Drive 15 GB via rclone). A backup that was
  never restored is not a backup — **drill it**.

## Checklist

### Session 1 — Reverse proxy & HTTPS

- [ ] Nginx (or Caddy) container in compose; app bound to 127.0.0.1:8000
- [ ] Free hostname (DuckDNS/sslip.io/nip.io) pointing at the server IP
- [ ] Let's Encrypt certificate + auto-renewal; verify rating (e.g., SSL Labs-style
      check); `curl https://…` evidence

### Session 2 — Persistence, logs, secrets

- [ ] Named volume for MySQL; verify data survives container recreation
- [ ] Log rotation limits on all services (`json-file`, max-size/max-file)
- [ ] `.env` chmod 600; token scopes + rotation steps documented in the runbook

### Session 3 — Backups & restore drill

- [ ] Daily `mysqldump` job (cron/container) with retention
- [ ] Off-site copy (rclone → R2/Drive free tier)
- [ ] **Restore drill:** fresh MySQL container → restore dump → verify data → evidence

### Close-out

- [ ] Mentor Questions answered; evidence; session log; execution-plan updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. Why is the app never exposed directly to the internet?
2. Why do we need a hostname for HTTPS, and how do we get one for $0?
3. What happens to the MySQL data if the container is deleted — and why?
4. Why do log rotation limits protect the whole server?
5. What does the restore drill prove that the backup alone does not?

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `curl https://…/health` | Verify HTTPS end-to-end |
| `docker exec db mysqldump …` | Create the backup |
| `docker compose down && up -d` | Prove the volume survives recreation |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> In your own words: the three things that turn "it runs" into "it can be trusted by
> strangers".

### Evidence

- [ ] HTTPS certificate + rating screenshot
- [ ] Volume persistence demo
- [ ] Backup job + off-site copy + restore drill (screenshots)
- [ ] Session log + execution plan updated; memory folder synced

> 🚀 **Next:** Stage 14 — Observability & Alerting.
