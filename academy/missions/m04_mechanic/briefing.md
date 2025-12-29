# Mission 04: The Mechanic
**Phase 1: The System Engineer**

> "A bad mechanic keeps adding parts until the engine breaks. A good mechanic knows exactly which bolt to remove."

## 1. The Concept: The Factory Floor (RAM)
Imagine your Raspberry Pi is a factory.
- **The CPU** is the Worker (The one actually doing things).
- **The RAM** is the Workbench.

Every time you run a program (like Python, or the Screen Manager), it takes up space on the Workbench.
If the Workbench gets full, the Worker has to start putting things on the floor (SD Card). This is called **Swapping**, and it is incredibly slow. If the floor gets full... the factory explodes (Freezes).

## 2. The Concept: The Job Ticket (PID)
Every program running is called a **Process**.
To keep track of them, Linux gives every process a unique ID number called a **PID** (Process ID).
- `Inkypi` might be PID `501`.
- `SSH` might be PID `882`.

You can see every job running in the factory using the command `top` or `ps aux`.

## 3. The Concept: The Red Button (Signals)
Sometimes, a program goes crazy. It stops listening to you. It starts eating all the RAM.
You need to force it to stop.
We send it a **Signal** using the `kill` command.

- **Signal 15 (SIGTERM)**: "Please stop nicely when you are done." (Polite).
- **Signal 9 (SIGKILL)**: "Security! Escort this process out of the building IMMEDIATELY." (Forceful).

```bash
kill -9 [PID]
```
*This is the ultimate power of the System Engineer. You decide what lives and what dies.*
