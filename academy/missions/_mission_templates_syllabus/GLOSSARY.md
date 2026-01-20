# InkyPi Academy: Concept Glossary

This glossary defines all technical terms used throughout the curriculum, organized by category. Each term includes: definition, why it matters, real-world role, and which missions use it.

**Usage**: Reference specific terms when learning new concepts. Terms are introduced incrementally across missions to prevent overwhelm.

---

## 🌐 Web & Networking

### HTTP (HyperText Transfer Protocol)
**Definition**: The language browsers and servers use to communicate over the internet.

**Analogy**: Like a postal system - you send a letter (request), someone sends back a reply (response).
- **Minecraft**: Like sending chat messages to a server
- **Spotify**: When you click "play", your app sends an HTTP request to Spotify's server

**Why It Matters**: Every web interaction uses HTTP. Without it, browsers couldn't talk to websites.

**Real-World Role**:
- Instagram uploading photos
- Spotify fetching playlists
- InkyPi triggering plugin generation

**Used In**: C-04, M-09, M-10, M-18

**Prerequisites**: None (foundational)

---

### URL (Uniform Resource Locator)
**Definition**: The address of a resource on the internet (like a street address).

**Analogy**: Like writing an address on an envelope - tells the internet where to find something.

**Example**: `https://spotify.com/api/currently-playing`
- `https://` = How to get there (HTTP Secure)
- `spotify.com` = Which house (domain)
- `/api/currently-playing` = Which room (specific resource)

**Why It Matters**: URLs let you find specific pages, images, or API endpoints on the internet.

**Real-World Role**:
- Browser address bar
- API endpoints (M-09 Spotify)
- Image download links (M-10)

**Used In**: C-04, M-09, M-10

**Prerequisites**: HTTP

---

### API (Application Programming Interface)
**Definition**: A way for programs to talk to each other. Like a menu at a restaurant - it tells you what you can order (what data you can request).

**Analogy**: 
- **Restaurant**: API is the menu, you order (request), kitchen makes it (processes), waiter brings food (response)
- **Demon Slayer**: Like a messenger crow - you send a message, it delivers, brings back a reply

**Why It Matters**: APIs let your code use services (Spotify, weather, anime databases) without building them yourself.

**Real-World Role**:
- Spotify API: Get currently playing song
- Weather API: Get temperature  
- MyAnimeList API: Get anime recommendations

**Used In**: M-09, M-10, M-18

**Prerequisites**: HTTP, JSON

---

### Request & Response
**Definition**: 
- **Request**: Asking for something (data, action) from a server
- **Response**: The server's answer (data, confirmation, error)

**Analogy**: Like asking a question and getting an answer.
- **You**: "Hey Spotify, what song am I playing?" (REQUEST)
- **Spotify**: "You're playing 'Gurenge' by LiSA" (RESPONSE)

**Why It Matters**: All web interactions are requests and responses. Understanding this helps debug ("did my request work?").

**Used In**: C-04, M-09, M-10

---

### Endpoint
**Definition**: A specific URL that does one thing in an API.

**Example**:
- `/api/currently-playing` = Endpoint to get current song
- `/api/playlists` = Endpoint to get playlists

**Analogy**: Like different customer service phone numbers:
- Call 1-800-ORDERS for orders
- Call 1-800-SUPPORT for support  
Each number (endpoint) does a specific job.

**Used In**: C-04, M-09, M-18

**Prerequisites**: URL, API

---

### Web Server
**Definition**: A program that listens for HTTP requests and sends back responses.

**Analogy**: Like a receptionist - receives requests, figures out who can help, sends back answers.

**Why It Matters**: InkyPi's web UI runs on a web server. When you click "Generate Image", the server receives that request.

**Used In**: C-04

**Prerequisites**: HTTP, Request/Response

---

### Route
**Definition**: Code that maps a URL to a specific function.

**Example**:
```python
@app.route('/api/generate/<plugin_id>')
def generate_image(plugin_id):
    # This function runs when URL is visited
```

**Analogy**: Like a switchboard operator directing calls to the right department.

**Used In**: C-04

**Prerequisites**: Web Server, URL

---

## 🐍 Python Programming

### Variable
**Definition**: A name that stores a value (number, text, etc.).

**Example**:
```python
name = "Tanjiro"
age = 15
```

**Analogy**: Like labeled boxes - you put things in boxes and label them so you can find them later.

**Used In**: M-07, C-01, all missions

---

### Function
**Definition**: A reusable block of code that does a specific task.

**Example**:
```python
def greet(name):
    return f"Hello, {name}!"
```

**Analogy**: Like a recipe - you write it once, use it many times.

**Why It Matters**: Functions prevent copy-pasting code (DRY principle).

**Used In**: M-06, all missions

---

### Class
**Definition**: A blueprint for creating objects. Defines what data (properties) and actions (methods) an object can have.

**Example**:
```python
class CreatureCard:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
```

**Analogy**: 
- **Class** = Cookie cutter (blueprint)
- **Object** = The actual cookie

**Why It Matters**: Classes organize code into logical units. All InkyPi plugins are classes.

**Used In**: M-06, C-02, C-03, all plugins

---

### Object / Instance
**Definition**: A specific "thing" created from a class blueprint.

**Example**:
```python
tanjiro = CreatureCard("Tanjiro", 100)  # Object/instance
nezuko = CreatureCard("Nezuko", 90)     # Another instance
```

**Analogy**: If Class is a cookie cutter, Object is the actual cookie.

**Used In**: C-02, C-03

**Prerequisites**: Class

---

### Method
**Definition**: A function that belongs to a class.

**Example**:
```python
class Creature:
    def attack(self):  # Method
        print("Attack!")
```

**Analogy**: Like abilities in a game - each character (object) has abilities (methods).

**Used In**: M-06, C-02, all plugins

**Prerequisites**: Class

---

### Inheritance
**Definition**: When one class "extends" another, getting all its methods and properties.

**Example**:
```python
class BaseCard:  # Parent
    def draw(self):
        pass

class CreatureCard(BaseCard):  # Child inherits from BaseCard
    pass
```

**Analogy**: 
- **Genetics**: Kids inherit traits from parents
- **RPG**: Warrior class inherits from Character class

**Why It Matters**: Inheritance prevents code duplication. All InkyPi plugins inherit from `BasePlugin`.

**Used In**: M-06, C-02, C-03

**Prerequisites**: Class

---

### super()
**Definition**: Calls the parent class's method from a child class.

**Example**:
```python
class Child(Parent):
    def __init__(self, name):
        super().__init__()  # Call parent's __init__
        self.name = name
```

**Analogy**: Like asking your parent for help - "Hey parent, do your thing first, then I'll do mine."

**Why It Matters**: Ensures parent class setup runs before child adds its own behavior.

**Used In**: C-03

**Prerequisites**: Inheritance

---

### Module
**Definition**: A Python file containing functions, classes, or variables that you can import and use.

**Example**:
```python
import datetime  # datetime is a module
from PIL import Image  # PIL is a module
```

**Analogy**: Like a toolbox - instead of carrying all tools everywhere, you grab the toolbox (module) when needed.

**Used In**: M-06, all missions

---

### Import
**Definition**: Loading code from another file/module so you can use it.

**Example**:
```python
from datetime import datetime
from PIL import Image
```

**Why It Matters**: Imports let you reuse code written by others (libraries) or yourself.

**Used In**: M-06, all missions

---

## 🏗️ Architecture & System Design

### Architecture
**Definition**: The big-picture design of how a system's parts connect and work together.

**Analogy**: Like a building's blueprint - shows how rooms connect, where plumbing goes, structural support.

**Why It Matters**: Understanding architecture helps you:
- Know where to look when debugging
- Add features without breaking things
- See how your code fits in the bigger system

**Used In**: C-04

---

### Interface / Contract
**Definition**: A set of rules defining what methods a class MUST have (but not how they work).

**Example**: `BasePlugin` is an interface - it says "all plugins MUST have `generate_image()` method" but doesn't care HOW you implement it.

**Analogy**: 
- **Job description**: Lists required skills, but each person does the job their own way
- **Game mod API**: Mods must have `onLoad()`, `onUpdate()` - the game doesn't care what they do inside

**Used In**: C-04, C-03

**Prerequisites**: Class, Inheritance

---

### Client-Server
**Definition**: A model where one program (client) requests services from another program (server).

**Example**:
- **Client**: Your web browser
- **Server**: InkyPi running on Raspberry Pi
- Browser requests, server responds

**Analogy**: 
- **Restaurant**: Customer (client) orders, kitchen (server) prepares food
- **Minecraft**: Your game (client) connects to server

**Used In**: C-04

**Prerequisites**: HTTP, Request/Response

---

### Separation of Concerns
**Definition**: Organizing code so each part does ONE job (not mixing responsibilities).

**Example**:
- **PluginManager**: Finds and loads plugins (one job)
- **YourPlugin**: Generates images (different job)
- **DisplayModule**: Shows images on hardware (another job)

**Why Better Than**: One giant function that does everything (hard to debug, modify)

**Used In**: C-04, throughout

---

## 💾 Data Structures

### List
**Definition**: An ordered collection of items.

**Example**:
```python
quotes = ["Never give up!", "I can do this!", "Stay strong!"]
```

**Analogy**: Like a shopping list - items in order, numbered.

**Used In**: M-11, C-05

---

### Dictionary
**Definition**: A collection of key-value pairs (like a real dictionary: word → definition).

**Example**:
```python
settings = {
    "volume": 80,
    "theme": "dark",
    "language": "en"
}
```

**Analogy**: 
- **Phone contacts**: Name → Phone number
- **Locker**: Locker number → Contents

**Why It Matters**: Dictionaries organize related data. JSON is basically a dictionary.

**Used In**: M-09, M-12

---

### JSON (JavaScript Object Notation)
**Definition**: A text format for storing/sending structured data (looks like Python dictionaries).

**Example**:
```json
{
  "name": "Tanjiro",
  "rank": "Demon Slayer",
  "breathing": "Water"
}
```

**Why It Matters**: APIs send data as JSON. You'll parse JSON from Spotify, anime APIs, etc.

**Used In**: M-09, M-10, M-18

**Prerequisites**: Dictionary

---

## 🖼️ Images & Graphics

### PIL (Pillow)
**Definition**: Python library for creating and editing images.

**Example**:
```python
from PIL import Image
img = Image.new("RGB", (250, 122), "white")
```

**Why It Matters**: InkyPi uses PIL to create all images before sending to display.

**Used In**: M-06, M-08, all plugins

---

### Image.open()
**Definition**: Load an existing image file from disk.

**Example**:
```python
img = Image.open("tanjiro.png")
```

**Used In**: M-08

**Prerequisites**: PIL, File I/O

---

### Resize
**Definition**: Change an image's dimensions.

**Example**:
```python
img = img.resize((100, 100))
```

**Why It Matters**: Display has fixed size (250x122). Images must be resized to fit.

**Used In**: M-08, M-10

---

### Composite / Paste
**Definition**: Layering images (putting one image on top of another).

**Example**:
```python
background.paste(character_img, (10, 20))
```

**Analogy**: Like layering transparencies in art class - background layer, then character layer.

**Used In**: M-08, M-10

---

## 🔧 InkyPi-Specific

### BasePlugin
**Definition**: The parent class all InkyPi plugins inherit from. Defines the contract (must have `generate_image()`).

**Why It Matters**: Inheriting from `BasePlugin` makes your plugin compatible with InkyPi system.

**Used In**: M-06, all plugins

**Prerequisites**: Class, Inheritance, Interface

---

### generate_image()
**Definition**: The method every plugin MUST implement. Takes settings + device_config, returns PIL Image.

**Example**:
```python
def generate_image(self, settings, device_config):
    # Your code here
    return img
```

**Why It Matters**: This is THE method InkyPi calls to get your plugin's output.

**Used In**: All plugins

**Prerequisites**: BasePlugin, Method

---

### device_config
**Definition**: Dictionary containing display hardware info (resolution, color mode).

**Example**:
```python
device_config = {
    "width": 250,
    "height": 122,
    "color": "black"
}
```

**Why It Matters**: Tells your plugin what size image to create.

**Used In**: All plugins

---

### PluginManager
**Definition**: InkyPi system component that discovers, loads, and calls plugins.

**Why It Matters**: Understanding PluginManager helps debug "why isn't my plugin showing up?"

**Used In**: C-04

**Prerequisites**: Class, Module

---

### plugin-info.json
**Definition**: JSON file that describes your plugin (ID, name, description, class).

**Example**:
```json
{
  "id": "creature_card",
  "name": "Creature Card",
  "class": "CreatureCard"
}
```

**Why It Matters**: PluginManager reads this to discover your plugin.

**Used In**: M-06, all plugins

---

## ⚙️ Error Handling & Debugging

### Exception
**Definition**: An error that occurs during program execution (like division by zero, missing file).

**Example**:
```python
try:
    result = 10 / 0  # Causes exception
except ZeroDivisionError:
    print("Can't divide by zero!")
```

**Used In**: M-09, M-10, M-15

---

### try/except
**Definition**: Catch errors and handle them gracefully instead of crashing.

**Why It Matters**: APIs fail, files go missing - your code should handle this.

**Used In**: M-09, M-10, M-15

---

### Logging
**Definition**: Recording what your program does (for debugging).

**Example**:
```python
logger.info("Starting plugin generation")
logger.error("Failed to load image")
```

**Why It Matters**: Logs help you debug issues ("what happened before it crashed?").

**Used In**: M-15

---

### Stack Trace
**Definition**: The error message showing which line caused a crash and the sequence of function calls leading to it.

**Why It Matters**: Learning to read stack traces is essential for debugging.

**Used In**: C-04, M-15

---

## 📊 Advanced Concepts (Phase 3-4)

### Caching
**Definition**: Saving data locally to avoid re-fetching it.

**Example**: Download album cover once, save to disk, reuse instead of downloading again.

**Why It Matters**: Faster, uses less bandwidth, works offline.

**Used In**: M-10

---

### OAuth
**Definition**: A way to let apps access your account without giving them your password.

**Example**: "Spotify login" button - grants access without sharing password.

**Used In**: M-09

**Prerequisites**: API, HTTP

---

### Conditionals (if/elif/else)
**Definition**: Making decisions in code based on conditions.

**Example**:
```python
if hour < 12:
    greet = "Good morning"
elif hour < 18:
    greet = "Good afternoon"
else:
    greet = "Good evening"
```

**Used In**: M-13

---

### Loops (for/while)
**Definition**: Repeating code multiple times.

**Example**:
```python
for i in range(10):
    print(i)
```

**Used In**: M-13, C-05

---

## 🗺️ Usage Guide

### How to Use This Glossary

**When starting a mission**:
1. Check "New Concepts" section in briefing
2. Look up unfamiliar terms here
3. Read definition + analogy
4. Note which missions use it (context)

**When stuck**:
1. Find the confusing term
2. Read "Prerequisites" - did you learn those?
3. Check "Real-World Role" - see concrete examples

**Building mental models**:
- Don't memorize definitions
- Focus on analogies (connect to what you know)
- Revisit terms after using them in missions

---

## 📚 Related Resources

- **Knowledge Map**: Visual representation of how concepts connect (see `/academy/map/`)
- **Mission Templates**: See how new concepts are introduced (`_mission_templates_syllabus/`)
- **Syllabus**: Full curriculum showing progressive concept introduction

---

**Last Updated**: 2026-01-21  
**Terms**: 50+ (covers M-01 through M-20)
