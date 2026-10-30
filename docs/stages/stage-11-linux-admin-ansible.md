# Stage 11 — Linux Server Administration + Ansible

> **Phase:** Phase 11 — Linux Administration + Ansible (route v2)
> **Estimated duration:** 5–7 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 10 complete (server provisioned with Terraform). ADR-0009.

---

## Objective

Administer the VPS like a professional — and finish with a **reproducible bootstrap**:
everything is done manually first to understand it, then encoded once in an idempotent
Ansible playbook that can rebuild the server state from zero.

## Scenario (real world)

*"Your server is ready. Now make it safe and make it repeatable: the next server must
be configured the same way without you remembering a single command."*

## Concepts (why first)

- **Why Ansible (ADR-0009):** agentless, runs over SSH, free. The playbook is another
  piece of versioned infrastructure — and another interview artifact.
- **Idempotency:** running the playbook twice must change nothing the second time.
  That is the proof the server is *declared*, not *described by hand*.
- **Users & permissions:** the app never runs as root; least privilege on the server,
  not only in the pipeline.
- **UFW:** default-deny; open only 22/80/443. fail2ban slows down brute force.
- **SSH hardening:** keys only, no root login, no password login.
- **Docker Engine (official apt repo, not snap):** what `apt` installs, why the Compose
  plugin is separate from the Engine.

## Checklist

### Session 1 — First contact & the system

- [ ] Update/upgrade the system; explain what `apt` does (sources, lists, upgrades)
- [ ] Users/groups/permissions: create an `app` user; explain `chmod`/`chown`
- [ ] Filesystem tour: `/etc`, `/var`, `/home` — what lives where (FHS)

### Session 2 — Firewall & SSH hardening

- [ ] UFW: default deny, allow 22/80/443; `ufw status` evidence
- [ ] fail2ban basics (ssh jail)
- [ ] SSH: disable root login + password auth; verify key-only login still works
- [ ] Reboot → reconnect → everything persists

### Session 3 — Docker Engine on the server

- [ ] Install Docker Engine from the official apt repo (not snap) + Compose plugin
- [ ] `docker run hello-world` as a smoke test; `docker version` evidence
- [ ] Understand what was installed (dockerd vs docker CLI vs compose plugin)

### Session 4 — The Ansible playbook

- [ ] `ansible/site.yml`: update system → users → UFW → SSH hardening → fail2ban →
      Docker Engine + Compose — all idempotent
- [ ] Run it twice: second run reports **0 changes** (evidence!)
- [ ] Destroy/recreate the server with Terraform → run the playbook → identical state

### Close-out

- [ ] Mentor Questions answered; evidence saved; session log; execution-plan updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. Why Ansible if cloud-init already configured first boot?
2. What does idempotency prove, and how did we demonstrate it?
3. Why must the firewall deny by default?
4. Why do we install Docker from the apt repo and not from snap?
5. What would happen if the playbook were deleted? Could you rebuild the server state?

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `apt update && apt upgrade` | Refresh + upgrade the system |
| `ufw allow 22/80/443` | Open only the needed ports |
| `ansible-playbook site.yml` | Apply the declared state |
| `ansible-playbook site.yml` (2nd run) | Prove idempotency (0 changes) |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> In your own words: what changes in your thinking once the server is a playbook and
> not a memory of commands.

### Evidence

- [ ] `ufw status`, `sshd_config` diffs, playbook output (2 runs)
- [ ] Terraform destroy → apply → playbook → identical state
- [ ] Session log + execution plan updated
- [ ] Memory folder synced to `C:\Repo2`

> 🚀 **Next:** Stage 12 — Deployment: immutable tag, CD over SSH, rollback.
