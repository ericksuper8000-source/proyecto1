# Stages

## Index & Evidence Rules

**Project:** CI/CD Pipeline Labs

---

## Index

| Stage | Title | Phase | Status |
|---|---|---|---|
| 08 | [SSH & Remote Connections](stage-08-ssh-remote-connection.md) | 8 | ✅ Complete (2026-08-25) |
| 09 | [VPS Provisioning with Terraform + cloud-init](stage-09-vps-provisioning.md) | 9 | ⬜ Pending — Current (route v2) |
| 10 | [FastAPI + MySQL Evolution](stage-10-fastapi-mysql-evolution.md) | 10 | ⬜ Pending (route v2) |
| 11 | [Linux Administration + Ansible](stage-11-linux-admin-ansible.md) | 11 | ⬜ Pending (route v2) |
| 12 | [Deployment: immutable tag, CD, rollback](stage-12-deployment-cd-rollback.md) | 12 | ⬜ Pending (route v2) |
| 13 | [Hardening: Nginx, HTTPS, backups](stage-13-hardening-https-backups.md) | 13 | ⬜ Pending (route v2) |
| 14 | [Observability & Alerting](stage-14-observability-alerting.md) | 14 | ⬜ Pending (route v2) |
| 15 | [Portfolio & Interview Packaging](stage-15-portfolio-packaging.md) | 15 | ⬜ Pending (route v2) |

> **Route v2 (2026-10-29 audit):** stages 09–15 were reordered and redefined by the
> audit (ADR-0008…0014). Each stage document exists in detail **now** so the route is
> always clear; they are refined when each stage is reached.

---

## Evidence Rules

Every stage produces **evidence** — proof that the work happened and can be reproduced.

### Screenshots

- One folder per stage: `screenshots/stage-08/`, `screenshots/stage-09/`, …
- Name files descriptively: `01-ssh-connect.png`, `02-keygen-output.png`, …
- Capture what matters (commands + output), not the whole screen.

### Command logs

- Save meaningful command output as text files under `screenshots/stage-NN/` when a
  screenshot is not practical.

### Reproducibility

- Another person must be able to follow the stage document and get the same result.
- Include every command with a one-line "why".

---

## Definition of Done (applies to every stage)

A stage is complete when **all** are true:

- [ ] All checklist items in the stage document are ticked.
- [ ] The **Report** section at the bottom of the stage is filled by the student.
- [ ] Evidence exists in `screenshots/stage-NN/`.
- [ ] ADR written if a meaningful decision was made.
- [ ] `session-log.md` has a new entry.
- [ ] `execution-plan.md` checkboxes + Current Status updated.
- [ ] Memory folder synced to `C:\Repo2`, committed and pushed to **both** GitHub and GitLab.
- [ ] The student can explain the stage back to the mentor (mentor validation passed).

---

## Stage Template

Every stage file follows `_template.md`. The template guarantees consistency, which makes
the repository easy to read for an interviewer and easy to resume for an AI.
