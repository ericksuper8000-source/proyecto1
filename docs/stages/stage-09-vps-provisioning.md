# Stage 09 — VPS Provisioning (Oracle Cloud Always Free)

> **Phase:** Phase 9 — VPS Provisioning
> **Estimated duration:** 2–3 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 08 complete (SSH mental model validated). This is the first
> stage with **real, billable-or-free infrastructure** — the zero-cost rule applies
> (ADR-0005).

---

## Objective

Provision the **first real server**: an Ubuntu instance on Oracle Cloud **Always Free**
(no cost), connect to it over SSH, and verify it responds — while understanding each
choice we make (why Oracle, why Ubuntu, what an "instance" really is, what the free-tier
limits are).

## Scenario (real world)

The company just gave you a cloud account and said: *"spin up the server we will deploy
to."* You must choose the provider, the OS, the size, the network, and the access method —
and you must do it **without generating a surprise bill**. This stage is where the
delivery pipeline finally gets a home.

## Concepts (why first)

- **Cloud vs local.** Your Docker Desktop runs containers on your own PC. A VPS is a
  virtual machine living in someone else's datacenter, reachable over the internet,
  always on.
- **Why Oracle Cloud Free Tier.** $0 is a hard requirement (ADR-0005). Oracle's "Always
  Free" tier offers permanent VMs with usable resources. Free tiers from other providers
  are time-bounded or resource-thin. **Re-verify availability at this stage** — free tiers
  change.
- **What an "instance" is.** Oracle provisions a VM inside their hypervisor. You choose
  the *shape* (CPU/RAM/disk) within the Always Free limits (e.g., 4 OCPU ARM / 24 GB RAM
  total, 200 GB block storage — exact limits are re-verified at this stage).
- **Why Ubuntu.** Ubuntu is a Debian-based Linux distribution, hugely common in the
  industry, with LTS releases and huge community support. Our Docker images already use
  Debian-style bases, so the mental model transfers.
- **The SSH key is the door.** Oracle generates a **key pair** for the instance. You keep
  the private key (`.pem`/`.key`), Oracle keeps the public part inside the instance. This
  is Stage 08 in action.
- **First contact is read-only.** Log in and observe: who are you? what OS? what
  resources? **Do not change anything yet.**

## Pre-flight

- [ ] Stage 08 validated (you can explain SSH).
- [ ] You have an email for a new Oracle Cloud account.
- [ ] You understand the zero-cost rule: **nothing that can generate a bill** (ADR-0005).
- [ ] You know your GitHub/GitLab identities (not needed here, but good context).

> ⚠️ **Rule for this stage:** stay strictly inside the **Always Free** tier. If a screen
> shows a price, stop and ask the mentor. Nothing gets created outside the free limits.

---

## Checklist

### Session 1 — Account & quotas

- [ ] Create the Oracle Cloud account (Always Free / Free Tier option)
- [ ] Complete identity verification as Oracle requests it
- [ ] Understand the difference between "Always Free" resources and "trial" credits
- [ ] Explore the free-tier limits in the console and note them in the Report
- [ ] Write down what would generate cost (so we can avoid it)

### Session 2 — Provision the instance

- [ ] Create the instance (Compute → Instances → Create)
- [ ] Choose the **Always Free** eligible shape (record CPU/RAM)
- [ ] Choose **Ubuntu** as the image
- [ ] Generate (or upload) the SSH key pair and **download/save the private key securely**
- [ ] Review network settings: default VCN, public IP, SSH (port 22) ingress
- [ ] Launch and wait for "Running"
- [ ] Note the public IP address in the Report

### Session 3 — First connection

- [ ] Fix the private key permissions (Linux/macOS: `chmod 600 key.pem`; Windows:
      ensure the key is not world-readable — ask the mentor for the Git Bash/Windows way)
- [ ] Connect: `ssh -i ~/.ssh/<key.pem> ubuntu@<ip>`
- [ ] Verify the host key prompt appears on **first** connection (Stage 08!)
- [ ] Observe (read-only):
  - [ ] `whoami` / `id` — who are you on this machine?
  - [ ] `cat /etc/os-release` — which Ubuntu version?
  - [ ] `free -h`, `nproc`, `df -h` — what resources does the free tier give you?
  - [ ] `ip a` — what is the machine's identity on the network?
- [ ] Exit cleanly (`exit`) and reconnect once to confirm stability

### Close-out

- [ ] Answer the Mentor Questions in the Report
- [ ] Save evidence (screenshots) in `screenshots/stage-09/`
- [ ] Write an ADR if we changed anything about the provider/OS decision
- [ ] Session log entry appended
- [ ] Execution plan Phase 9 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\Repo2`, committed and pushed to GitHub + GitLab

---

## Mentor Questions

1. Why did we choose Oracle Cloud Free Tier over the alternatives?
2. What is an instance, really? What is the "shape" and why does it matter?
3. Why Ubuntu instead of another distribution?
4. Where does the private key live, and why must it never be shared or committed?
5. What does the "authenticity of host can't be established" warning mean now?
6. What resources does the free tier give you (from `free -h`, `nproc`, `df -h`)?
7. How can we guarantee this server never generates a bill?

---

## Report (student fills after the session)

### What I did

### How it works / why

(Your answers to the Mentor Questions.)

### Commands I used

| Command | Why I used it |
|---|---|
| `ssh -i ~/.ssh/<key.pem> ubuntu@<ip>` | First connection to the instance |
| `cat /etc/os-release` | Verify the OS version |
| `free -h` | Check available RAM |
| `nproc` | Check CPU count |
| `df -h` | Check disk |
| `ip a` | Inspect network identity |
| … | … |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> Write 5–10 sentences explaining what a VPS is now that you have one, and why "first
> contact read-only" matters.

### Evidence

- [ ] Screenshots saved in `screenshots/stage-09/` (e.g., `01-instance-created.png`, `02-ssh-first-connect.png`, `03-os-resources.png`)
- [ ] Only Always Free resources created (verify: nothing outside free tier)
- [ ] Private key stored securely, **not** committed anywhere
- [ ] Session log entry appended
- [ ] Execution plan updated
- [ ] Memory folder synced to `C:\Repo2`, committed and pushed to GitHub + GitLab

> 🚀 **Next:** Stage 10 — Linux Server Administration: update/upgrade, users, permissions,
> firewall, SSH hardening, and installing Docker Engine + Compose on the VPS.
