# Mission 02: The Detective
**Phase 1: The System Engineer**

> "A machine never forgets. It just whispers so quietly that only a Detective can hear it."

## 1. The Concept: The Black Box (Journalctl)
Every time a program crashes, a USB is plugged in, or a user logs in, the System writes it down in a giant, never-ending diary called the **Journal**.
Your InkyPi has been writing thousands of lines while you sleep.

To read this diary, we use the command `journalctl` (Journal Control).
- `journalctl`: Shows *everything* (Too much!).
- `journalctl -f`: Follows the diary in real-time (Like watching a live feed).
- `journalctl -u inkypi`: Shows only entries from the specific user/service "inkypi".

## 2. The Concept: The Pipe `|`
Linux has a superpower called "Piping". It connects the output of one command to the input of another.
Think of it like plumbing.
- **Command A** produces water (Text).
- **The Pipe `|`** catches that water.
- **Command B** receives the water and does something with it.

## 3. The Concept: The Filter (Grep)
`grep` stands for "Global Regular Expression Print", but let's call it **The Filter**.
It takes a stream of text and throws away *everything* except the lines that match your search word.

### The Combo Move
The most powerful move in a System Engineer's toolkit is combining all three:
```bash
journalctl | grep "error"
```
*"Take the massive diary -> Pipe it to the Filter -> Show me only lines containing 'error'."*

This is how you find the needle in the haystack.
