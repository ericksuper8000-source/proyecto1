# Stage 09 — VPS Provisioning with Terraform + cloud-init

> **Phase:** Phase 9 — VPS Provisioning (route v2)
> **Estimated duration:** 3–4 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 08 complete (SSH mental model). ADR-0009 (IaC), ADR-0005
> (zero cost), ADR-0010 (multi-arch consequence).
> **Changed by audit 2026-10-29:** the server is now created **from code** — no manual
> console provisioning.

---

## Objective

Provision the **first real server with Terraform + cloud-init** — reproducible,
reviewable, free — and connect over SSH, understanding every choice (provider, shape,
ARM vs x86, state, plan/apply).

## Scenario (real world)

The company gave you a cloud account and said: *"create the server we will deploy to —
and do it in a way anyone on the team can review and recreate."* Clicking through a
console is not an answer: the server must exist as code in Git.

## Concepts (why first)

- **Infrastructure as Code.** The server is a set of versioned files (`infra/`). Anyone
  can see what exists, and recreate it with one command. The console becomes read-only.
- **Terraform:** provider (talks to the cloud API), resources (VM, network, firewall),
  state (remembers what it created), `plan` (shows changes), `apply` (makes them),
  `destroy` (removes everything).
- **cloud-init:** the industry-standard first-boot hook built into Ubuntu images. It
  creates the user, installs the SSH public key, disables password login, and enables
  unattended upgrades — before you ever log in.
- **Why Oracle Always Free (ADR-0005/0009):** permanent free VMs (ARM A1.Flex: up to
  4 OCPU / 24 GB RAM, 200 GB storage — re-verify live). ⚠️ Oracle requires a credit card
  for **identity verification only**; nothing is charged if we stay inside Always Free.
  **If a Hetzner VPS is already owned, prefer it** (no incremental cost, simpler
  provider) — this is a Session 0 decision gate.
- **ARM vs x86:** the free shape with real resources (A1.Flex) is **ARM64**. Our images
  must be multi-arch (ADR-0010) or the server cannot run them (`exec format error`).
- **The budget alert:** Oracle lets you configure a $0 threshold alert for free. It is
  the guarantee that "nothing generates a bill" is watched, not just hoped for.

## Pre-flight

- [ ] Stage 08 validated (you can explain SSH).
- [ ] ADR-0009 read. Provider decision made (Oracle vs owned Hetzner) and logged.
- [ ] A credit card available for Oracle identity verification (no charge) — or the
      Hetzner path chosen.
- [ ] Terraform CLI installed locally (free).
- [ ] You understand the zero-cost rule: **nothing that can generate a bill** (ADR-0005).

## Checklist

### Session 0 — Decision gate & Terraform

- [ ] Read ADR-0009 + ADR-0005; decide the provider; record the decision + reason
- [ ] Install Terraform CLI; verify `terraform -version`
- [ ] Explain: provider / state / resource / plan / apply / destroy (mentor check)

### Session 1 — Account & quotas

- [ ] Create the cloud account (Oracle Always Free — or log into owned Hetzner)
- [ ] Understand "Always Free" vs trial credits; record the live limits
- [ ] Configure a **budget alert** (Oracle: $0 threshold; Hetzner: project spending
      limit if available) — evidence screenshot

### Session 2 — The `infra/` module

- [ ] `infra/main.tf`: provider configuration
- [ ] Network: VCN/subnet (Oracle) or network/firewall rules (Hetzner): ingress 22/80/443
- [ ] Instance: Ubuntu LTS; shape per provider (A1.Flex ARM on Oracle)
- [ ] **cloud-init** user-data: `ubuntu` user, `id_ed25519_vps.pub`, disable password
      auth, unattended-upgrades, SSH key only
- [ ] Outputs: public IP
- [ ] `terraform plan` (review what will be created) → `terraform apply`
- [ ] Server shows Running; note the public IP

### Session 3 — First contact (read-only) + reproducibility drill

- [ ] `ssh mi-vps` works (alias in `~/.ssh/config`)
- [ ] Observe: `whoami`, `cat /etc/os-release`, `free -h`, `nproc`, `df -h`, `ip a`
- [ ] Reproducibility drill: `terraform destroy` → `terraform apply` (server is code)
- [ ] Verify `unattended-upgrades` is active (cloud-init did its job)

### Close-out

- [ ] Answer the Mentor Questions in the Report
- [ ] Evidence in `screenshots/stage-09/` (plan/apply output, budget alert, ssh login)
- [ ] Session log entry; execution-plan Phase 9 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. Why Terraform instead of clicking the console?
2. What does `terraform state` remember, and why is it stored?
3. What does cloud-init do before you ever log in?
4. Why did we choose this provider under the zero-cost rule? What would generate a bill?
5. Why does the ARM shape force multi-arch images (ADR-0010)?
6. What proves that our server is "code" and not a manual artifact?

---

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `terraform init` | Download the provider plugin |
| `terraform plan` | Preview changes before applying |
| `terraform apply` | Create the real infrastructure |
| `terraform destroy` | Prove the server is disposable code |
| `ssh mi-vps` | First real connection (Stage 08 in action) |
| `free -h` / `nproc` / `df -h` | Observe the free-tier resources |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> 5–10 sentences: what a VPS is now that you have one *created from code*, and why the
> reproducibility drill matters.

### Evidence

- [ ] `terraform plan/apply/destroy` outputs saved
- [ ] Budget alert configured (screenshot)
- [ ] SSH first connection screenshot
- [ ] Private key stored securely, **not** committed
- [ ] Session log + execution plan updated
- [ ] Memory folder synced to `C:\Repo2`

> 🚀 **Next:** Stage 10 — FastAPI + MySQL Evolution (the app becomes a real service
> *before* any deployment work — ADR-0008).
