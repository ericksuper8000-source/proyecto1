# Stage 14 — Observability & Alerting

> **Phase:** Phase 14 — Observability (route v2)
> **Estimated duration:** 4–5 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 13 complete (HTTPS + `/health` public). ADR-0011.

---

## Objective

Prove the system is watched: availability checks, metrics, dashboards, and a **real
alert that reaches the student's phone** — all self-hosted and free.

## Scenario (real world)

*"It's 3 a.m. The service is down. How do you find out before the users do?"*

## Concepts (why first)

- **Uptime vs metrics vs alerts (ADR-0011):** Uptime Kuma answers "is it reachable?";
  Prometheus/cAdvisor answer "how is it behaving?" (CPU, RAM, disk, containers);
  Alertmanager turns thresholds into notifications; Grafana makes it human-readable.
- **The alert path:** Uptime Kuma checks `/health` every 60 s → on failure it notifies
  → Telegram bot (free API) → phone. Grafana Alerting can also fire on metrics
  thresholds (disk > 80 %, CPU > 90 %).
- **Why self-hosted:** every component is free software that runs in the same compose
  stack (ADR-0005/0011). Grafana Cloud free tier is the documented fallback.
- **ARM check:** each monitoring image must support arm64 (official images do — verify,
  ADR-0010).
- **Drill, not config:** a monitoring stack with no proven alert is decoration. We stop
  the app and the phone must ring.

## Checklist

### Session 1 — Uptime

- [ ] Uptime Kuma container: checks `/health` every 60 s; public status page
- [ ] (Optional) status page linked from the README as live demo evidence

### Session 2 — Metrics & dashboards

- [ ] cAdvisor (container metrics) + Prometheus (scrape) + Alertmanager
- [ ] Grafana dashboards: node + containers (CPU/RAM/disk/restarts)
- [ ] Configs versioned in `monitoring/` (compose + prometheus.yml + dashboards)

### Session 3 — Alerts

- [ ] Telegram bot token (free); test message
- [ ] Alert rules: app down; disk > 80 %; CPU > 90 %; container restart loop
- [ ] **Alert drill:** stop the app → alert arrives on the phone → evidence (screenshot
      of the message + timestamps)

### Session 4 — Logs & close

- [ ] Log strategy documented: where to look for what (app, db, nginx, containers)
- [ ] Loki consciously deferred (ADR-0011) — written as a stretch goal
- [ ] Dashboard + alert screenshots as portfolio evidence

### Close-out

- [ ] Mentor Questions answered; evidence; session log; execution-plan updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. What question does each tool answer: Uptime Kuma, cAdvisor, Prometheus, Grafana,
   Alertmanager?
2. Trace the path of the alert from a failed `/health` to your phone.
3. Why is the drill the real deliverable of this stage?
4. Why is Loki deferred, and what would it add later?

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `docker compose up -d` (monitoring stack) | Start the observability services |
| `docker stop mi_app_container` | Trigger the alert drill |
| `curl http://localhost:9090/…` | Verify Prometheus scrapes |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> In your own words: what "observable" means now, compared to "it answers to curl".

### Evidence

- [ ] Uptime Kuma status page (public URL)
- [ ] Grafana dashboards (screenshots)
- [ ] Alert drill: phone screenshot + timeline
- [ ] Session log + execution plan updated; memory folder synced

> 🚀 **Next:** Stage 15 — Portfolio & Interview packaging.
