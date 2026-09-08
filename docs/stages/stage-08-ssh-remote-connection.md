# Stage 08 — SSH & Remote Connections

> **Phase:** Phase 8 — SSH & Remote Access
> **Estimated duration:** 1–2 sessions
> **Status:** 🔄 In progress
> **Prerequisites:** Phases 1–7 complete. This stage is **theory-first**: no VPS is
> created yet.

---

## Objective

Build a solid **mental model** of what it means to connect to a remote machine. Before we
create the Oracle VPS, the student must understand what actually happens when you run
`ssh usuario@servidor` — so that from Phase 9 onward, every command makes sense instead
of being copy-paste.

## Scenario (real world)

In every real job, the servers you will administer are **not** on your desk. They live in
a datacenter or a cloud provider, with no screen, no keyboard, and no mouse. The only
door into them is SSH. A DevOps Junior who cannot explain what SSH is doing cannot
diagnose why a deploy failed at 3 a.m.

## Concepts (why first)

- **Why remote access exists.** Servers are shared, remote, headless machines. You cannot
  plug a monitor into every one. We need a *protocol* to control them safely.
- **SSH = a secure channel over an untrusted network.** Everything between your computer
  and the server is encrypted (integrity + confidentiality). The name says it: Secure
  SHell.
- **Client–server.** `ssh` is a *client* program; the server runs `sshd` (the SSH
  daemon). Your command opens a connection to a daemon listening on port 22.
- **Authentication = who are you?** Two layers:
  1. The *server* proves its identity to you (host key) — so you are not talking to an
     impostor.
  2. You prove your identity to the server — with a password, or better, with a **key
     pair** (private key stays with you, public key goes to the server).
- **What you control.** When the channel is open, the server gives you a *shell*: a
  program that interprets the commands you type. You are not "moving your computer to
  the server" — you are sending text to a program running on the server.
- **Why no GUI.** A headless server has no graphics stack. A shell is enough to do
  everything: install software, move files, run containers. GUIs are a convenience, not a
  requirement.

## Pre-flight

- [ ] You can answer: "What problem does SSH solve?" in one sentence.
- [ ] You know the difference between a client and a server (we saw servers in the
  pipeline: GitHub Actions runners are servers too).
- [ ] Git Bash / a terminal is available on your machine.

> ⚠️ **Rule for this stage:** no VPS is created. If you have ever typed `ssh` before,
> that is fine — this stage is about understanding it, not about connecting yet.

---

## Part A — What the command does (mental model)

Before touching a keyboard, discuss with the mentor and then answer in the Report:

When you type `ssh erick@1.2.3.4`, a chain of events happens. Describe each link:

1. The client resolves where `1.2.3.4` is (the IP is the address of the machine).
2. The client opens a TCP connection to the server's port **22**.
3. The server presents its **host key**; your client checks it against its "known hosts"
   list (this is why the first connection shows the "authenticity of host … can't be
   established" warning).
4. The two sides negotiate encryption and verify the server's identity (protects against
   man-in-the-middle).
5. You authenticate: password OR key-based (Phase 10 will harden this to keys only).
6. On success, the server starts a **session** and attaches it to your shell — you get a
   prompt that *looks* like your local prompt but runs on the remote machine.

> 💡 **Key idea:** after connecting, the prompt shows the **remote** hostname, not your
> computer's. That hostname is your first clue that you are somewhere else.

---

## Part B — Keys: the modern way to authenticate

Authentication by password has a problem: passwords are sent/typed and can be guessed.
**Key pairs** fix this:

- Your computer holds a **private key** (never leaves your machine, never shared).
- The server holds the matching **public key** (safe to share; it is public).
- The server challenges you with a message that only your private key can answer. If the
  answer is valid, you are in — **without ever sending the private key**.

Create a local key pair (practice only, no server needed):

```bash
ssh-keygen -t ed25519 -C "tu-comentario@host"
```

- `-t ed25519` chooses the algorithm. `-C` adds a comment (usually your email).
- It will ask where to save it (default `~/.ssh/id_ed25519`) and a passphrase.
- Two files appear:
  - `id_ed25519` — your **private key** (this file must stay secret).
  - `id_ed25519.pub` — your **public key** (this one you can send anywhere).

Inspect them:

```bash
cat ~/.ssh/id_ed25519.pub    # the public key — safe to show
ls -la ~/.ssh                # verify permissions on the private key
```

> 🧠 Why does this matter for our project? In Phase 9, Oracle will give you a key pair to
> connect to the VPS, and in Phase 10 we will harden SSH to **keys only** (no passwords).
> Understanding keys now means those steps will make sense.

---

## Part C — Verify your understanding (questions before proceeding)

Answer these **in your own words** in the Report before marking this stage done:

1. What is SSH, and what problem does it solve?
2. What runs on the server to accept SSH connections? (name and port)
3. Walk through what happens between typing `ssh usuario@servidor` and getting a prompt.
4. Why does the *first* connection show a warning about the host's authenticity?
5. What is the difference between the private key and the public key? Which one can you
   share?
6. Why does a server usually have no graphical interface? What do you actually control
   when you type commands?
7. Who "authenticates" you, and how does key-based authentication avoid sending secrets?

---

## Checklist

- [ ] I can explain what SSH is and what problem it solves.
- [ ] I can explain what happens on a `ssh usuario@servidor` connection (client, server,
      port 22, host key, encryption, auth, shell).
- [ ] I can explain how key-based authentication works (private vs public key).
- [ ] I can explain why a server has no GUI and what I control over the shell.
- [ ] I generated a local key pair with `ssh-keygen` and inspected both files.
- [ ] I verified the private key permissions (it must be readable only by me).
- [ ] I answered the 7 questions above in the Report.
- [ ] I understand that **no VPS is created in this stage** — Phase 9 is next.

---

## Mentor Questions

The mentor will ask a subset of the questions above, **one at a time**, to confirm the
model is clear. If any answer shows memorization instead of understanding, we stop and
reinforce before moving to Phase 9.

---

## Report (student fills after the session)

### What I did

### How it works / why

(Your answers to the 7 questions in Part C.)

### Commands I used

| Command | Why I used it |
|---|---|
| `ssh-keygen -t ed25519 -C "…"` | Generate a practice key pair |
| `cat ~/.ssh/id_ed25519.pub` | Inspect the public key (safe to share) |
| `ls -la ~/.ssh` | Verify files and permissions |
| … | … |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> Write 5–10 sentences explaining what SSH is **now that you understand it**. If you can
> explain it to a friend, you understood the stage.

### Evidence

- [ ] Screenshots saved in `screenshots/stage-08/` (e.g., `01-keygen-output.png`, `02-pubkey.png`)
- [ ] No VPS created (verify: nothing was provisioned)
- [ ] Session log entry appended
- [ ] Execution plan Phase 8 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\Repo2`, committed and pushed to GitHub + GitLab

> 🚀 **Next:** Stage 09 — VPS Provisioning: create the Oracle Cloud Free Tier account and
> provision the first Ubuntu server, then connect to it with the key pair we understand.
