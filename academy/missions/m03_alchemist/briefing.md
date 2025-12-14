# Mission 03: The Alchemist
**Phase 1: The System Engineer**

> "The Sorcerer uses a wand (Output). The Alchemist touches the raw elements (Files)."

## 1. The Concept: Everything is a File
In most operating systems, hardware is hidden behind "Drivers" and "APIs". You need special software to talk to it.

**Linux is different.** In Linux, **Hardware is a File**.
- The Hard Drive? That's a file at `/dev/sda`.
- The Screen? That's a file at `/dev/fb0`.
- The CPU Temperature? That's a text file you can read.
- The Green LED? That's a file you can write "0" or "1" into.

This means you can separate the "Physics" from the "Code". You don't need Python to turn on a light. You just need to write to a file.

## 2. The Location: `/sys/class`
This is your Laboratory.
Navigate to `/sys/class` and look around. You will see folders for `leds`, `thermal`, `net`, `graphics`.
These aren't real files on the disk; they are **Illusion Files** created by the Kernel to let you talk to the machine.

## 3. The Transmutation: `echo` and `cat`
Since hardware is just a text file:
- **To Read a Sensor**: Use `cat` (Concatenate/Display).
    *   `cat /sys/class/thermal/thermal_zone0/temp` -> `42000` (42.000°C)
- **To Control a Device**: Use `echo` (Write).
    *   `echo 1 > brightness` (Turn ON)
    *   `echo 0 > brightness` (Turn OFF)

*(Note: Because hardware is powerful, you usually need `root` powers (sudo) to write to these files).*
