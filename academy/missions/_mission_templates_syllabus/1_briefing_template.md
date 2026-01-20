# Template: How to Write briefing.md (Enhanced)

Use this template to create the `briefing.md` file for any mission.

**NEW FEATURES** (2026-01-21):
- 📚 New Concepts Primer (explain terms BEFORE the mission)
- Glossary integration
- Age-appropriate analogies (Minecraft, Spotify, Gaming, Demon Slayer)
- Incremental terminology introduction

---

## Structure Overview

Every briefing.md should follow this exact structure:

1. **Title & Introduction** (1 paragraph)
2. **📚 New Concepts Primer** (NEW! Explain prerequisite concepts BEFORE the problem)
3. **The Problem: [Pain Without Concepts]** (3-4 paragraphs with code)
4. **The Solution: [Concepts to the Rescue]** (2-3 paragraphs with code)
5. **Breaking It Down** (One section per concept)
6. **Key Principle** (Summary)
7. **What "Success" Looks Like** (Outcomes)

---

## 1. Title & Introduction

```markdown
# Briefing: [Mission ID] — [Mission Name]

[One paragraph describing what students will build and what core concept they'll learn]

Example:
"You will build a base card and then a special card that **inherits** from it. 
This mission teaches why inheritance exists and when to use `super()`."
```

---

## 2. NEW CONCEPTS PRIMER ⭐ (Add this BEFORE "The Problem")

**Purpose**: Explain unfamiliar terminology BEFORE diving into the mission. Prevents "Wait, what's HTTP?" moments.

**When to include**: Add this section if mission introduces 3+ new technical terms (especially web, system, or advanced concepts).

**Template**:

```markdown
## 📚 Before We Begin: Understanding [Category of Concepts]

> **Note**: This mission uses some new terminology. Don't worry - we'll explain everything here before diving in! For detailed definitions, see [GLOSSARY.md](../../../_mission_templates_syllabus/GLOSSARY.md).

### Quick Primer: [Core Concept Group Name]

[Brief overview paragraph explaining the new domain - e.g., "The Web Stack", "System Architecture", "API Communication"]

**Visual Overview**:

```
[ASCII diagram showing how concepts relate]

Example for web concepts:
You (Browser) ──── HTTP Request ────→ Web Server (Raspberry Pi)
                                          ↓
                                    Runs Python code
                                          ↓
                              ← HTTP Response ──── Returns result
```

### Key Terms You'll Encounter

**[Term 1] (e.g., HTTP)**:
- **Simple definition**: [One sentence in plain language]
- **Analogy**: [Choose 1-2 from student's world]
  - **Minecraft**: "Like sending chat messages to a server"
  - **Spotify**: "When you click play, your app sends an HTTP request"
  - **Gaming**: "Client-server communication in online multiplayer"
  - **Demon Slayer**: "Like a crow carrying messages between demon slayers"
  - **Real life**: "Like sending a letter and getting a reply"
- **In this mission**: [Where/how they'll use it - 1 sentence]

**[Term 2] (e.g., URL)**:
- **Simple definition**: [One sentence]
- **Analogy**: 
  - **Real life**: "Like a street address for the internet"
  - **Gaming**: "Like a server IP address"
- **In this mission**: [Context]

**[Term 3]**:
- [Same structure - only include 3-5 most important new terms]

### How These Connect

[One paragraph explaining how all the new terms work together in this mission's context]

Example:
"When you click 'Generate Image' in the browser (HTTP Request), it sends a message to the Raspberry Pi's Web Server. The server finds the right Python code (Route), runs it, and sends back the result (HTTP Response). Each step has a specific job!"

### Don't Worry About

You **don't** need to know:
- [Advanced details not needed - e.g., "How HTTP works under the hood"]
- [Related but out-of-scope concepts - e.g., "TCP/IP protocols"]
- [Future topics - e.g., "Advanced server frameworks"]

We only cover what you need for THIS mission.

---
**Ready?** Now that you understand [concepts], let's see why they matter!

---
```

### Analogy Guidelines (Age-Appropriate)

**Minecraft** (for system concepts):
- Server/client architecture
- Command blocks (functions)
- Redstone systems (logic)
- Multiplayer servers (networking)

**Spotify** (for data & APIs):
- Playlists (lists)
- Playing songs (API calls)
- User accounts (objects/classes)
- Recommendations (algorithms)

**Gaming** (for general programming):
- Character classes (OOP inheritance)
- Inventory systems (lists/dictionaries)
- Online multiplayer (client-server)
- Save files (data persistence)

**Demon Slayer** (for communication/flow):
- Crow messages (requests/responses)
- Breathing techniques (methods)
- Corps rank hierarchy (inheritance)
- Training arcs (progressive learning)

**Real Life** (fallback):
- Recipes (functions)
- Blueprints (classes)
- Postal mail (HTTP)
- Phone books (dictionaries)

**When NOT to include Primer**:
- Mission only uses previously learned concepts
- Terms are Python basics covered in earlier missions
- Concepts are self-explanatory from context

---

## 3. The Problem: [Show the Pain]

**Purpose**: Make students FEEL the pain of not using the concept

**Structure**:
```markdown
## The Problem: [Catchy Title]

Imagine you're building [real scenario]. You need [task that requires concept].

Without [concept], your code looks like this:

```python
# Show messy code with duplications/problems
[Bad code example - 15-20 lines]
```

**The Pain Points:**
- **Lines X-Y** are copy-pasted in all N classes (Z duplicated lines!)
- Your designer says: "[change request]" → You need to change N places
- You add a Nth item → Copy-paste the shared code AGAIN
- You forget to update one → [specific bug example]

**When [designer/manager] makes M changes, you're changing N places. One missed update = broken [app/game].**
```

**Tips**:
- Use concrete numbers (3 classes, 9 duplicated lines)
- Show real change scenarios ("Make border thicker")
- Calculate the pain (3 places → 30 places with 10 items)

---

## 4. The Solution: [Concepts to the Rescue]

**Purpose**: Introduce concepts as the hero that solves the mess

**Structure**:
```markdown
## The Solution: [Concept Name] to the Rescue

**[Concept]** is like [powerful analogy]. [Explain analogy in 2-3 sentences]

Think of it like [Manufacturing/Game example]:
- **Base Class** = [platform/foundation that all share]
- **Subclasses** = [specialized versions that inherit + add unique parts]

Each [subclass] **inherits** the [shared parts], then adds its specialty. 
If [base] improves [shared feature], ALL [subclasses] get it automatically!

Here's the same [task] with [concept]:

```python
# Show clean code using concepts
[Good code example - should be significantly shorter]
```

**Benefits:**
- [Shared code] written ONCE (in [BaseClass])
- Designer says "[same change request]"? → Change ONE place
- Add M more types? → Each only writes N lines (their unique part)
- Shared behavior stays consistent across ALL [items]
- No copy-paste = no bugs from forgetting to update one

**When [designer] makes M changes to shared elements, you change 1 place instead of N.**
```

**Tips**:
- Strong analogy (Car manufacturing, building blueprints, game character classes)
- Side-by-side comparison with Problem section
- Quantify benefits (1 change vs 30 changes)

---

## 5. Breaking It Down

**Purpose**: Detailed explanation of each concept with before/after

**Structure** (Repeat for each concept):

```markdown
## Breaking It Down

### 1) [Concept Name] = "[One-Liner Description]"

**Analogy**: Like [relatable metaphor]. [Expand in 1-2 sentences]

**Definition**: [Technical but clear explanation in 1-2 sentences]

**Before/After:**

```python
# Before (no [concept]): [Show the pain]
[Code showing the problem - 8-12 lines]

# After (with [concept]): [Show the solution]
[Code showing the fix - 4-6 lines]
```

**Why Better**: [Explain the improvement with numbers]. 
Before = edit N classes. After = edit 1 class.

**Common Mistakes**:
- [Mistake 1]: [What it is + how to fix]
- [Mistake 2]: [What it is + how to fix]

**Where Used**: [Specific line range] in `[mission_file].py`

**Scalability Context**: 
With N items, before = X duplicated lines. After = Y lines (Z% reduction!).
When M people work on this, [explain how concept helps collaboration].
```

**Tips**:
- Each concept gets its own subsection
- Always include before/after code
- Quantify the improvement
- Connect to where it's used in mission
- Add scalability perspective

---

## 6. Key Principle

```markdown
## Key Principle: [DRY / Encapsulation / Abstraction / etc.]

[Concept] is the answer to: "[The specific problem it solves]"

**Rule of Thumb**:
- 2-3 items with similar code? → Consider [concept]
- 3+ items with similar code? → Time to [apply concept]
- Changing shared code requires updating N places? → DEFINITELY need [concept]
```

---

## 7. What "Success" Looks Like

```markdown
## What "Success" Looks Like

- [Technical outcome 1]: [Specific code behavior]
- [Technical outcome 2]: [Specific code structure]
- [Understanding outcome]: Changing [base] affects all [subclasses] (intentionally!)
- [Maintainability outcome]: Code is shorter, clearer, and easier to maintain

Use/avoid guidance is practiced in `bad_code.py`.
```

---

## Real-World Connection Examples

Always include 2-3 apps/games students know:

**For Classes/Objects**:
- Pokemon: 1000+ creatures, each is an object
- Contact app: Each contact is an object
- Fortnite inventory: Each item is an object

**For Inheritance**:
- Hearthstone cards: Base card + specialized types
- Mobile RPG: Base character → Warrior/Mage/Rogue
- Pokemon TCG: All cards have HP → Each type adds unique

**For Lists**:
- Leaderboards: High scores list
- Shopping cart: Items list
- Spotify: Playlist is a list

**For Loops**:
- Instagram grid: Loop through photos
- Game inventory: Loop through items
- Settings menu: Loop through options

---

## Checklist: Is My Briefing Complete?

### Core Structure
- [ ] Title with mission ID and name
- [ ] Introduction (1 paragraph, what + why)
- [ ] **NEW**: Concepts Primer (if 3+ new terms)
  - [ ] Visual diagram showing how concepts relate
  - [ ] 3-5 key terms with definitions
  - [ ] Age-appropriate analogies (Minecraft, Spotify, etc.)
  - [ ] "Don't worry about" section
  - [ ] Link to GLOSSARY.md
- [ ] Problem section showing messy code
- [ ] Pain points with concrete numbers
- [ ] Solution section with clean code
- [ ] Benefits with metrics (1 change vs 30)

### Breaking It Down (Each Concept)
Each concept section has:
  - [ ] Analogy (student-appropriate)
  - [ ] Definition
  - [ ] Before/After code
  - [ ] Why Better (with numbers)
  - [ ] Common Mistakes
  - [ ] Where Used in mission
  - [ ] Scalability Context

### Final Sections
- [ ] Key Principle (rule of thumb)
- [ ] What Success Looks Like
- [ ] 2-3 Real-world examples students know
- [ ] Team/collaboration perspective
- [ ] Metrics throughout (line counts, ratios)

---

## Example: Concepts Primer for C-04

```markdown
## 📚 Before We Begin: Understanding the Web Stack

> **Note**: This mission explores how InkyPi's web interface works. We'll use some web development terms. For detailed definitions, see [GLOSSARY.md](../../../_mission_templates_syllabus/GLOSSARY.md).

### Quick Primer: Client-Server Architecture

When you use InkyPi's web interface, you're interacting with a **client-server system**. Your browser (client) talks to the Raspberry Pi (server) to make things happen.

**Visual Overview**:

```
    You (Browser)
         ↓
    Click "Generate Image"
         ↓
    HTTP Request sent
         ↓
Web Server (Raspberry Pi)
         ↓
    Runs your plugin code
         ↓
    HTTP Response with image
         ↓
    Browser shows result
```

### Key Terms You'll Encounter

**HTTP (HyperText Transfer Protocol)**:
- **Simple definition**: The language browsers and servers use to communicate
- **Analogy**:
  - **Minecraft**: Like sending chat messages to a server
  - **Real life**: Like sending a letter and getting a reply
- **In this mission**: You'll trace HTTP requests from browser to your Python code

**URL (Web Address)**:
- **Simple definition**: The address of a resource on the internet (like a street address)
- **Analogy**:
  - **Real life**: Like writing an address on an envelope
- **In this mission**: You'll see URLs like `/api/generate/<plugin_id>`

**Endpoint**:
- **Simple definition**: A specific URL that does one job
- **Analogy**:
  - **Gaming**: Like different menu options (Play Game, Settings, Quit)
- **In this mission**: Each endpoint triggers different Python functions

**Web Server**:
- **Simple definition**: A program that listens for requests and sends back answers
- **Analogy**:
  - **Real life**: Like a receptionist directing visitors to the right office
- **In this mission**: InkyPi runs a web server that handles all button clicks

### How These Connect

When you click "Generate Image" in the browser, it sends an HTTP request to a specific URL (endpoint). The web server receives this, finds the right Python code to run (your plugin), and sends back an HTTP response (the generated image). It's like a conversation between your browser and the Raspberry Pi!

### Don't Worry About

You **don't** need to know:
- How HTTP works at the network level (TCP/IP, packets, etc.)
- Advanced web frameworks (we'll just show you the basics)
- Security details (authentication, encryption)

We only cover what you need to understand InkyPi's architecture.

---
**Ready?** Now let's see WHY understanding this architecture matters!

---
```

---

## Common Pitfalls to Avoid

❌ **Don't**:
- Start with definitions (boring!)
- Show only syntax (not WHY)
- Use abstract examples (not relatable)
- Skip the pain section (students won't appreciate solution)
- Forget metrics (make improvements concrete)
- Omit real-world examples
- **NEW**: Assume students know web/system terms
- **NEW**: Use technical jargon without explanation

✅ **Do**:
- **NEW**: Add Concepts Primer for unfamiliar domains (web, APIs, architecture)
- **NEW**: Use age-appropriate analogies (Minecraft, Spotify, Gaming, Demon Slayer)
- Start with the problem/pain
- Show concrete code (before/after)
- Use apps students know
- Quantify improvements (3:1 ratio, 50% reduction)
- Include team/scalability thinking
- Make it a story (problem → solution → success)
- Reference GLOSSARY.md for detailed definitions

---

**Last Updated**: 2026-01-21 (Enhanced with knowledge scaffolding)
