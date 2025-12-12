# Mission 01: The Commander
**Phase 1: The System Engineer**

> "A true Commander does not just sit in the cockpit; they know how the secure lines work."

## 1. The Concept: SSH (The Secure Tunnel)
You have been using `ssh pi@...` to enter your InkyPi. But what is actually happening?

Imagine your InkyPi is a **Bank Vault**.
- The **IP Address** is the street address of the bank.
- **SSH (Secure Shell)** is a magically constructed, armored tunnel that connects your laptop directly to the inside of the vault.
- **Encryption**: The tunnel is made of math. Even if a hacker intercepts the cable, all they see is unbreakable code.

## 2. The Concept: Permissions (The Gatekeeper)
Linux is paranoid. It assumes everyone is an intruder until proven otherwise. Every file has three security guards:
1.  **Owner**: The creator (Usually you, `pi`).
2.  **Group**: Your team.
3.  **Others**: Everyone else (The public).

Each guard checks for three badges:
- **Read (r)**: "You can look at it."
- **Write (w)**: "You can change it."
- **Execute (x)**: "You can run it (if it's a program)."

### The Magic Command: `chmod`
`chmod` (Change Mode) is how you tell the guards what to do. The most famous code is `777` (Everyone can do everything), but that is dangerous! It's like leaving the vault door open.

We prefer `600`:
- **Owner**: Read + Write (6)
- **Group**: None (0)
- **Others**: None (0)
*Only your eyes only.*

## 3. The Concept: The Network Interface
Your Pi has multiple faces (Interfaces):
- **lo (Loopback/Localhost)**: Talking to itself. (127.0.0.1)
- **wlan0 (Wi-Fi)**: Talking to the house. (192.168.x.x)

When `inkypi` says it runs on `0.0.0.0`, it means "I am listening on **ALL** faces."
