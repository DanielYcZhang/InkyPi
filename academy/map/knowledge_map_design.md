# InkyPi Academy: Interactive Knowledge Map Design

**Vision**: An RPG-style interactive skill tree that visualizes the entire learning journey, showing how concepts connect from foundational (Python, Linux) through advanced (APIs, Architecture) with mission-specific context.

---

## 1. Core Concept

### The Vision: "Skill Tree for Software Learning"

Like a **game skill tree** (e.g., Minecraft mod progression, RPG talent trees), students see:
- **Where they are** in the learning journey
- **What they've unlocked** (completed concepts)
- **What's next** (available to learn)
- **What's locked** (requires prerequisites)
- **How concepts connect** (dependencies)

### Key Metaphor: "The Tech Universe Map"

```
         [The Internet Cloud] ← Macro level (zoom out)
               ↓
        [Client-Server]
          ↙         ↘
    [Browser]    [Web Server]
        ↓            ↓
     [HTTP]      [Python]
        ↓            ↓
     [URL]       [Flask]
                     ↓
               [BasePlugin] ← Micro level (zoom in)
```

Students can **zoom between levels** to see big picture or granular details.

---

## 2. User Experience Flow

### Initial View (Macro - "The Big Picture")

```
🌍 THE SOFTWARE & HARDWARE UNIVERSE

┌─────────────────────────────────────────────────────────┐
│                                                         │
│     [Internet] ──────┐                                 │
│         │            │                                  │
│         ↓            ↓                                  │
│    [Browser]    [Server/Cloud]                         │
│         │            │                                  │
│         ↓            ↓                                  │
│    [Your Mac]   [Raspberry Pi] ──→ [E-Ink Display]    │
│                      │                                  │
│                      ↓                                  │
│                 [InkyPi System]                         │
│                      │                                  │
│                      ↓                                  │
│                 [Your Plugins]                          │
│                                                         │
└─────────────────────────────────────────────────────────┘

Legend:
✅ Unlocked (learned)
🔓 Available (can learn now)
🔒 Locked (needs prerequisites)
👉 Current focus
```

### Zoom Level 2 ("Web Stack")

Click on `[Browser] → [Server]` expands to:

```
CLIENT-SERVER ARCHITECTURE

┌──────────────┐                    ┌──────────────┐
│   Browser    │                    │ Web Server   │
│   (Client)   │                    │  (Backend)   │
└──────┬───────┘                    └──────┬───────┘
       │                                   │
       │  1. HTTP Request →                │
       │     (URL + data)                  │
       │                                   │
       │                ← 2. HTTP Response │
       │                    (HTML/Image)   │
       │                                   │
    Concepts:                          Concepts:
    - HTTP                             - Routes
    - URL                              - Endpoints
    - Request/Response                 - API
    - Browser DevTools                 - Python server
```

### Zoom Level 3 ("InkyPi System")

Click on `[InkyPi System]` expands to:

```
INKYPI ARCHITECTURE

                [Web UI]
                    ↓
    [HTTP Route] /api/generate/<id>
                    ↓
            [PluginManager]
                    ↓
              [BasePlugin] ← Interface/Contract
               ↙    ↓    ↘
    [Clock]  [Card]  [Gallery] ← Your plugins
                    ↓
              [PIL Image]
                    ↓
           [Display Module]
                    ↓
          [E-Ink Hardware]

Concepts:
- Architecture
- Interface (BasePlugin)
- Plugin Discovery
- Generate Image Method
- PIL Library
```

### Zoom Level 4 ("Individual Concept")

Click on any concept node (e.g., `[HTTP]`) shows **concept card**:

```
╔═══════════════════════════════════════════════════╗
║  📦 HTTP (HyperText Transfer Protocol)           ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║  DEFINITION:                                      ║
║  The language browsers and servers use to         ║
║  talk to each other. Like a postal system        ║
║  for the internet.                                ║
║                                                   ║
║  WHY IT MATTERS:                                  ║
║  Every time you click a link, play a song,       ║
║  or load an image, HTTP is working. It's the     ║
║  foundation of the web.                           ║
║                                                   ║
║  REAL-WORLD ROLE:                                 ║
║  • Spotify: HTTP fetches your playlists          ║
║  • Instagram: HTTP uploads your photos           ║
║  • InkyPi: HTTP triggers plugin generation       ║
║                                                   ║
║  USED IN MISSIONS:                                ║
║  • C-04: Tracing HTTP requests                   ║
║  • M-09: API calls to Spotify                    ║
║  • M-10: Downloading album covers                ║
║                                                   ║
║  PREREQUISITES:                                   ║
║  ✅ None (foundational concept)                   ║
║                                                   ║
║  UNLOCKS:                                         ║
║  • API (needs HTTP)                              ║
║  • Web Routes (needs HTTP)                       ║
║                                                   ║
║  ANALOGY:                                         ║
║  "Like sending letters: You write a letter       ║
║  (REQUEST), mail it to someone, they read it     ║
║  and send back a reply (RESPONSE)."              ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

---

## 3. Data Structure

### Concept Node Schema

```json
{
  "id": "http",
  "name": "HTTP",
  "fullName": "HyperText Transfer Protocol",
  "category": "web",
  "tier": "foundational",
  "definition": "The language browsers and servers use to communicate...",
  "whyItMatters": "Every web interaction uses HTTP...",
  "realWorldRole": [
    "Spotify uses HTTP to fetch playlists",
    "Instagram uses HTTP to upload photos",
    "InkyPi uses HTTP to trigger plugins"
  ],
  "usedInMissions": ["C-04", "M-09", "M-10"],
  "prerequisites": [],
  "unlocks": ["api", "web_routes", "endpoints"],
  "analogies": [
    {
      "context": "Minecraft",
      "text": "Like sending chat messages to server"
    },
    {
      "context": "Mail system",
      "text": "Sending letters and getting replies"
    }
  ],
  "visualPosition": {
    "x": 250,
    "y": 150,
    "zoomLevel": 2
  },
  "status": "unlocked" // or "available" or "locked"
}
```

### Category Tree

```
categories:
  - id: "foundational"
    name: "Foundational Concepts"
    concepts: ["http", "variable", "function", "class"]
  
  - id: "web"
    name: "Web & Networking"
    parent: "foundational"
    concepts: ["http", "url", "api", "request", "response", "endpoint"]
  
  - id: "python"
    name: "Python Programming"
    concepts: ["class", "inheritance", "method", "module", "import"]
  
  - id: "architecture"
    name: "System Architecture"
    parent: ["web", "python"]
    concepts: ["client_server", "interface", "contract", "module", "separation_of_concerns"]
  
  - id: "hardware"
    name: "Hardware & Linux"
    concepts: ["raspberry_pi", "e_ink", "gpio", "systemd", "linux"]
  
  - id: "inkypi"
    name: "InkyPi Specific"
    parent: ["python", "hardware"]
    concepts: ["base_plugin", "plugin_manager", "device_config", "generate_image"]
```

---

## 4. Visual Design Mockup

### Node States (Visual Indicators)

```
✅ UNLOCKED (Completed/Learned)
   - Full color
   - Bright glow
   - Checkmark badge
   - Clickable (shows detail card)

🔓 AVAILABLE (Ready to Learn)
   - Muted color
   - Gentle pulse animation
   - "Next!" badge
   - Clickable (shows preview + missions to unlock)

🔒 LOCKED (Prerequisites Not Met)
   - Grayscale
   - Lock icon
   - Clickable (shows "Need to complete: X, Y, Z first")

👉 CURRENT (In Progress)
   - Highlighted border
   - Distinct color (e.g., gold)
   - "You are here" indicator
```

### Connection Lines (Dependencies)

```
    [HTTP] ────────→ [API]
      │
      └─────→ [URL]
      │
      └─────→ [Endpoint]

Line styles:
─────→  Learned (solid green)
- - -→  Available (dashed yellow)
· · ·→  Locked (dotted gray)
```

---

## 5. Navigation & Interaction

### Zoom Levels

**Level 0: Universe View** (Entire tech stack)
- Internet, Hardware, Software, Your Projects
- Ultra-high level

**Level 1: Domain View** (Major categories)
- Web, Python, Architecture, Hardware, APIs
- Category clusters

**Level 2: Concept Cluster** (Related concepts)
- Client-Server architecture expanded
- InkyPi system architecture
- Python OOP concepts

**Level 3: Individual Concepts** (Single nodes)
- HTTP node
- BasePlugin node
- With connections to related nodes

**Level 4: Detail Card** (Full explanation)
- Definition, examples, missions, analogies
- Modal overlay

### Search & Filter

```
🔍 Search: [type concept name...]

Filters:
☐ Unlocked only
☐ Available only
☐ Show all

Categories:
☑ Web & Network
☑ Python
☑ Architecture
☐ Hardware
☑ InkyPi
```

### Progress Sidebar

```
┌─────────────────────┐
│  YOUR PROGRESS      │
├─────────────────────┤
│ Phase 1: ████████  │
│ Linux & OS    100% │
│                     │
│ Phase 2: ██████▒▒  │
│ Python Core    75% │
│ 👉 C-04 (current)  │
│                     │
│ Phase 2.5: ▒▒▒▒▒▒  │
│ Real Projects   0% │
│ 🔒 Locked          │
│                     │
│ Total: 89/245      │
│ Concepts unlocked  │
└─────────────────────┘
```

---

## 6. Technical Implementation

### Technology Stack Options

**Option A: Web-Based (Recommended)**
- **Frontend**: React + D3.js (for graph visualization)
- **Zoom**: D3 zoom behaviors
- **Cards**: Modal components
- **Data**: JSON file (concepts.json)
- **Hosting**: Static site on Raspberry Pi or GitHub Pages

**Option B: Desktop App**
- **Electron** app (uses web tech)
- Offline-first
- Can integrate with InkyPi system

**Option C: Web Component**
- Embedded in existing InkyPi web UI
- No separate navigation

### Data Flow

```
1. Student completes mission (e.g., C-04)
2. check.py marks mission complete
3. Updates progress.json:
   {
     "completed_missions": ["M-06", "M-07", "C-01", "C-02", "C-03", "C-04"],
     "unlocked_concepts": ["http", "url", "api", "base_plugin"],
     "current_mission": "M-08"
   }
4. Knowledge map reads progress.json
5. Updates node states (unlocked/available/locked)
6. Highlights current concept cluster
```

### File Structure

```
academy/map/
├── knowledge_map_design.md (this file)
├── concepts.json (all concept nodes)
├── progress.json (student's progress)
├── index.html (knowledge map UI)
├── js/
│   ├── knowledge_graph.js (D3 visualization)
│   ├── concept_card.js (detail modals)
│   └── progress_tracker.js
├── css/
│   └── map_styles.css
└── assets/
    └── icons/ (category icons)
```

---

## 7. Concept List (Full Curriculum)

### Tier 1: Foundational (M-01 to M-07)
```
Linux & OS:
- command_line, mkdir, cd, ls, chmod
- systemd, service, journalctl
- file_paths, permissions

Python Basics:
- variable, string, int, function
- import, module, print
- datetime, f_string
```

### Tier 2: Object-Oriented (C-01 to C-03)
```
OOP Core:
- class, object, instance
- method, property, self
- inheritance, super(), base_class
- encapsulation, polymorphism
```

### Tier 3: Architecture (C-04)
```
System Design:
- architecture, system_diagram
- interface, contract
- client_server, request_response
- code_reading, tracing

Web Fundamentals:
- http, url, endpoint
- web_server, route
- browser, devtools
```

### Tier 4: Integration (M-08 to M-12)
```
File & Images:
- file_io, image_loading
- pil_library, resize, composite
- image_modes, rgb_rgba

APIs & Data:
- api, json, oauth
- requests_library, http_get
- caching, error_handling

Data Structures:
- list, dictionary
- random_selection, iteration
- psutil, system_stats
```

### Tier 5: Engineering (M-13 to M-20)
```
Control Flow:
- conditionals, if_elif_else
- loops, for_while
- booleans, state_machine

Data Persistence:
- json_files, file_append
- aggregation, sorting

Quality & Collaboration:
- exception_handling, logging
- graceful_degradation, debugging
- code_review, documentation
- testing, edge_cases
```

---

## 8. Mission Integration

### Concept-to-Mission Mapping

```json
{
  "http": {
    "introduced": "C-04",
    "practiced": ["M-09", "M-10"],
    "mastered": "M-18"
  },
  "inheritance": {
    "introduced": "M-06",
    "practiced": ["C-02", "C-03"],
    "mastered": "C-03"
  },
  "api": {
    "introduced": "M-09",
    "practiced": ["M-10", "M-18"],
    "mastered": "M-19"
  }
}
```

### Mission Cards (When Clicking "Used in M-09")

```
╔═══════════════════════════════════════╗
║  M-09: The Spotify Connector          ║
╠═══════════════════════════════════════╣
║  Status: 🔒 Locked                    ║
║  Prerequisites:                        ║
║  ✅ C-04 (architecture)               ║
║  ✅ M-08 (image loading)              ║
║                                        ║
║  Introduces:                           ║
║  • API                                 ║
║  • JSON                                ║
║  • OAuth                               ║
║                                        ║
║  Uses concepts from:                   ║
║  • HTTP (C-04)                        ║
║  • BasePlugin (C-02)                  ║
║  • Error Handling (M-15)              ║
║                                        ║
║  [View Mission Details →]              ║
╚═══════════════════════════════════════╝
```

---

## 9. Success Metrics

### Student Engagement Indicators

```
1. Time spent exploring map (engagement)
2. Concepts clicked (curiosity)
3. Forward-looking (clicks on locked nodes)
4. Backward reference (re-visits unlocked nodes)
5. Search usage (seeking understanding)
```

### Learning Outcomes

```
IF student regularly uses map THEN:
  - Better context for "why am I learning this?"
  - Understanding of concept dependencies
  - Motivation (see progress visually)
  - Less "I'm lost" moments
```

---

## 10. Future Enhancements

### Phase 2 Features

1. **Concept Relationships**: Not just prerequisites, but "uses", "builds on", "related to"
2. **Alternative Paths**: Multiple ways to unlock concepts
3. **Achievement Badges**: "API Master", "Architecture Guru"
4. **Time Estimates**: "2 hours to unlock HTTP"
5. **Recommendations**: "Based on your interests (anime, music), try M-11 next!"

### Phase 3 Features

1. **Compare with Peers**: "Students who completed C-04 often found M-09 challenging"
2. **Resource Links**: External articles, videos for each concept
3. **Quiz Integration**: "Test your HTTP knowledge"
4. **Custom Paths**: Hide/show concepts based on goals (web focus vs hardware focus)

---

## 11. Implementation Phases

### Phase 1: MVP (4-8 hours work)
- [ ] Create concepts.json with all ~100 concepts
- [ ] Build basic D3 graph (zoom + pan)
- [ ] Concept cards (modal on click)
- [ ] Manual progress tracking (edit progress.json)

### Phase 2: Integration (4-8 hours)
- [ ] Auto-update progress from check.py
- [ ] Mission integration (click concept → shows missions)
- [ ] Search & filter
- [ ] Progress sidebar

### Phase 3: Polish (8+ hours)
- [ ] Animations (unlock effects)
- [ ] Responsive design (mobile-friendly)
- [ ] Category color themes
- [ ] Export progress (screenshot/PDF)

---

## 12. Example User Journey

### Week 1 (Starting C-04)
1. Student opens knowledge map
2. Sees C-01, C-02, C-03 nodes glowing **✅ UNLOCKED**
3. Sees C-04 node highlighted **👉 CURRENT**
4. Clicks C-04 node → sees concepts: HTTP, Architecture, Code Reading
5. Clicks HTTP → sees "This concept is NEW in C-04!"
6. Reads card: "HTTP is like sending letters..."
7. Sees "Used in: C-04, M-09, M-10"
8. Clicks M-09 → "Locked. Complete C-04 and M-08 first."
9. **Motivation**: "Ah! HTTP unlocks Spotify mission!"

### Week 3 (Completed C-04, starting M-08)
1. Opens map
2. C-04 now shows ✅ (satisfying!)
3. New concepts lit up: HTTP, Architecture nodes glowing full color
4. M-08 now **👉 CURRENT**
5. Can see path: M-08 → M-09 → M-10 (Spotify journey)
6. Zooms out → sees "I'm 30% through Phase 2!"

### Week 8 (Mid-curriculum)
1. Opens map
2. Huge cluster of unlocked nodes (dopamine!)
3. Sees future: M-18 (Anime API) uses concepts from M-09 + M-11
4. Clicks "Architecture" category → filters just architecture concepts
5. Sees progression: Class → Inheritance → Interface → Architecture
6. **Insight**: "Oh that's why we learned this order!"

---

## 13. Design Inspiration

### Visual References
- **Skill trees**: Path of Exile, World of Warcraft talent trees
- **Knowledge graphs**: Obsidian.md, Roam Research
- **Game maps**: Hollow Knight (interconnected areas), Metroid (unlocking paths)

### Color Palette
```
- Unlocked: Green (#4CAF50)
- Current: Gold (#FFD700)
- Available: Blue (#2196F3)
- Locked: Gray (#9E9E9E)

Categories:
- Web: Orange (#FF9800)
- Python: Blue (#2196F3)
- Architecture: Purple (#9C27B0)
- Hardware: Red (#F44336)
- InkyPi: Teal (#009688)
```

---

## Next Steps

1. **Review this design** with student/coach
2. **Prioritize features** (MVP vs nice-to-have)
3. **Create concepts.json** (data entry for all terms)
4. **Build prototype** (simple HTML + D3 version)
5. **Test with student** (usability feedback)
6. **Iterate** based on usage patterns

**Estimated MVP Timeline**: 2-3 days of focused development work

This knowledge map will transform the learning experience from "What's next?" to "I can see my entire journey!"
