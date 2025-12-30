# Mission 05: The Ghost
**Phase 1: The System Engineer**

> "A Program dies when you close the window. A Service haunts the machine forever."

## 1. The Concept: The Daemon
When you run a Python script, it lives inside your terminal window. If you close the window (or SSH disconnects), the process dies. This is called running in the **Foreground**.

To make a program run automatically on boot, run in the background, and restart if it crashes, we turn it into a **Daemon** (or Service).

## 2. The Puppet Master: Systemd
Linux has a Master Control Program called **systemd**. It is the first thing that wakes up when you plug in the power (PID 1).
It reads "Service Files" to know what to launch.

## 3. The Service File (`.service`)
This is the recipe card for your ghost. It lives in `/etc/systemd/system/` and looks like this:

```ini
[Unit]
Description=My Ghost Script

[Service]
ExecStart=/usr/bin/python3 /home/pi/script.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

## 4. The Spells: `systemctl`
You control the spirits using `systemctl`:
- `systemctl start [name]`: Wake it up now.
- `systemctl stop [name]`: Banish it.
- `systemctl enable [name]`: "Wake up every time the machine boots."
- `systemctl status [name]`: "Are you alive?"
