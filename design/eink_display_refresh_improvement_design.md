# E-Ink Display Refresh Improvement Design

## Status

Draft

## Context

InkyPi renders plugin output as a `PIL.Image` and then sends that image to the configured display driver.

There are two broad rendering paths today:

1. Direct image generation with Pillow.
2. HTML/CSS rendering through `chromium-headless-shell`, followed by a screenshot back into a `PIL.Image`.

For the current Waveshare 7.5 inch black and white setup, the configured display type is `epd7in5_V2`.

Relevant code paths:

- Display orchestration: [src/display/display_manager.py](/Users/fredzhang/dev/fred/InkyPi/src/display/display_manager.py)
- Waveshare wrapper: [src/display/waveshare_display.py](/Users/fredzhang/dev/fred/InkyPi/src/display/waveshare_display.py)
- Waveshare driver: [src/display/waveshare_epd/epd7in5_V2.py](/Users/fredzhang/dev/fred/InkyPi/src/display/waveshare_epd/epd7in5_V2.py)
- HTML screenshot path: [src/utils/image_utils.py](/Users/fredzhang/dev/fred/InkyPi/src/utils/image_utils.py)
- HTML plugin base: [src/plugins/base_plugin/base_plugin.py](/Users/fredzhang/dev/fred/InkyPi/src/plugins/base_plugin/base_plugin.py)

The observed user experience is that refreshing the e-ink display normally takes about 3 to 5 seconds.

## Problem Statement

The current refresh pipeline is slower than it needs to be for common update cases.

The key issue is not just that some plugins use Chromium for HTML rendering. The larger issue is that the Waveshare display path currently forces the slowest possible panel update strategy on every refresh:

1. Re-initialize the display.
2. Clear the full panel.
3. Push a full-frame update.
4. Put the panel back to sleep.

That path is correct but pessimistic. It treats every update as a full-screen refresh, even when only a small part of the screen changed.

## What Is Slow Today

There are two distinct sources of latency.

### 1. Software-side render latency

HTML-based plugins launch `chromium-headless-shell`, render the page, save a screenshot, and re-open that screenshot as an image.

This adds startup and rendering overhead, especially on Raspberry Pi class hardware.

This cost matters for:

- Weather with charts
- Calendar
- RSS
- Other plugins using `BasePlugin.render_image()`

This cost does not matter for plugins drawn directly with Pillow.

### 2. Hardware-side panel refresh latency

The Waveshare wrapper currently does a full clear and full display for every image update.

For the 7.5 inch black and white Waveshare panel, that is inherently slow. The panel waveform and busy-wait time dominate the end-to-end experience for full-screen updates.

This means:

- Even if image rendering were instantaneous, the display would still feel slow.
- Chromium is only part of the problem.
- For many refreshes, the display driver strategy is the primary bottleneck.

## Current Architecture

Current flow:

```text
Plugin settings
    |
    v
Plugin generates PIL image
    |
    +--> Pillow-native rendering
    |
    +--> HTML -> Chromium headless -> screenshot -> PIL image
    |
    v
DisplayManager post-processing
orientation -> resize -> enhancement
    |
    v
WaveshareDisplay.display_image()
    |
    v
Init -> Clear -> Full display -> Sleep
```

## Standard Refresh Characteristics for Waveshare 7.5" Black/White

For the Waveshare 7.5 inch black and white family, the expected refresh behavior is roughly:

- Full refresh: about 3 to 5 seconds
- Fast refresh: about 1 to 2 seconds
- Partial refresh: sub-second for small regions, commonly around a few hundred milliseconds

Exact timing varies by panel revision and ambient conditions, but the important point is that the current observed full-refresh time is normal for this class of hardware.

This means the goal should not be "make full refresh instant." The goal should be:

1. Avoid unnecessary full refreshes.
2. Use faster panel modes for incremental changes.
3. Keep full refresh only when needed for image quality and ghosting control.

## How Partial Refresh Works

Partial refresh does not mean the system stops rendering images.

It means the system still produces a bitmap, but instead of refreshing the entire display, it refreshes only the changed region.

Conceptually:

```text
Previous frame
    +
New frame
    |
    v
Compare frames
    |
    v
Find bounding box of changed pixels
    |
    v
Align region to panel byte/grid rules
    |
    v
Use panel partial-update mode for that region only
```

The bundled Waveshare driver for `epd7in5_V2` already exposes the primitives needed for this:

- `init_fast`
- `init_part`
- `display_Partial`

So the panel-level capability already exists in the codebase. The missing piece is integration in InkyPi's higher-level display wrapper and refresh policy.

## Important Constraints of Partial Refresh

Partial refresh is not free and not universal.

### Ghosting

Repeated partial updates accumulate visual artifacts. The system will need periodic full refreshes to reset the panel.

### Region alignment

Partial refresh windows usually need alignment to byte or controller boundaries. The code must expand the changed box to valid panel coordinates.

### Change detection

The system needs access to both the previous displayed frame and the new frame. That means storing or reconstructing the last panel image in a comparable format.

### Plugin characteristics

Some plugins change only a small area between refreshes.

Examples:

- Clock digits
- Timestamp text
- Small metric panels

Other plugins change the entire layout every time.

Examples:

- Full weather dashboard with graph shifts
- Calendar with many moving event positions
- Full-screen image plugins

For the second category, partial refresh may provide little benefit.

## Premise Challenge

The tempting premise is: "The system is slow because it uses Chromium headless shell."

That premise is incomplete.

A better framing is:

"The system is slow because it combines a potentially expensive render stage with an always-full-display hardware update strategy."

That distinction matters because it changes the order of operations:

- If the display path is fixed first, many refreshes get meaningfully faster without replacing the render architecture.
- If Chromium is rewritten first but the display still does full clear/full refresh/sleep, much of the perceived latency remains.

## Options Considered

### Option A: Keep current rendering architecture and improve display update strategy

Summary:

Keep producing a final bitmap the same way as today, but change how that bitmap is sent to the Waveshare panel.

What changes:

- Stop unconditional full clear on every refresh.
- Stop deep-sleeping the panel after every update when near-term refreshes are expected.
- Add previous-frame tracking.
- Add diff-based region detection.
- Choose between full, fast, and partial refresh based on how much of the screen changed.

Pros:

- Highest impact for the least architectural risk.
- Reuses existing rendering pipeline.
- Helps both Pillow and HTML plugins.
- Minimal disruption to plugin API.

Cons:

- Requires careful ghosting policy.
- Requires display-specific logic.
- Needs testing against real hardware behavior.

Assessment:

This is the recommended first step.

### Option B: Keep full refresh behavior but replace Chromium for HTML plugins

Summary:

Reimplement HTML-driven plugins using direct Pillow drawing or a different rendering mechanism.

What changes:

- Migrate some or all HTML plugins away from `chromium-headless-shell`.
- Rebuild charts, layout, and typography directly in Python or with a different raster pipeline.

Pros:

- Reduces CPU and process startup overhead.
- Can improve responsiveness for HTML-heavy plugins.
- May reduce memory pressure on smaller Pi devices.

Cons:

- Large rewrite cost.
- Harder to maintain rich layouts and charts.
- Does not solve the display-side full-refresh bottleneck.
- Risks replacing a flexible layout system with more custom drawing code.

Assessment:

Useful only after measurement proves Chromium is a major share of the refresh time for the target plugins.

### Option C: Re-architect the entire rendering pipeline around incremental composition

Summary:

Move from "render one final bitmap each time" to a persistent composition system that tracks individual regions or widgets and refreshes them independently.

What changes:

- Persistent scene graph or layered compositor
- Widget-level dirty-region tracking
- More advanced scheduling and display policies

Pros:

- Best possible long-term control.
- Makes partial refresh a first-class concept.
- Could support highly dynamic widgets efficiently.

Cons:

- Highest complexity.
- Significant architectural risk.
- Hard to justify for a dashboard-style e-ink product unless near-real-time updates become a product goal.

Assessment:

This is an overreach for the current problem. It is an ocean, not a lake.

## Recommendation

Recommend Option A.

Do not reimplement the whole rendering process first.

Instead:

1. Preserve the existing "plugin -> PIL image" contract.
2. Improve the Waveshare display wrapper so it can choose smarter refresh modes.
3. Add measurement so rendering time and display time are visible separately.
4. Only revisit Chromium replacement if profiling shows it remains a large bottleneck after the display path is fixed.

## Proposed Refresh Policy

Suggested policy:

### Full refresh

Use when:

- First display after boot
- Layout changed substantially
- A large percentage of pixels changed
- Too many partial refreshes have accumulated
- Visual artifacts are detected or expected

### Fast refresh

Use when:

- The image changed broadly but not enough to justify a full clear
- The panel supports a faster full-frame update waveform

### Partial refresh

Use when:

- Only a small region changed
- The panel revision and content type are suitable
- The changed bounding box is materially smaller than the screen

### Scheduled recovery full refresh

Use periodically after N partial updates or after a timeout interval to reduce ghosting.

## Proposed Implementation Direction

### Phase 1: Instrumentation

Measure:

- Plugin generation time
- HTML screenshot time
- Display transfer time
- Panel busy time

This separates:

- Render bottlenecks
- Display bottlenecks

Without this, optimization discussions remain speculative.

### Phase 2: Smarter Waveshare output path

Add:

- Previous-frame tracking
- Diff bounding box calculation
- Refresh mode selection policy
- Optional sleep deferral

This phase should preserve plugin behavior and focus only on display output.

### Phase 3: Plugin classification

Group plugins into:

- Mostly static
- Regionally dynamic
- Fully dynamic

This helps determine where partial refresh actually pays off.

### Phase 4: Targeted rendering improvements

Only after measurement:

- Convert specific hot plugins away from Chromium if needed
- Consider persistent browser process or alternate raster path if HTML rendering is still too expensive

## What We Should Not Do First

Do not start by rewriting all HTML plugins in Pillow.

Reasons:

- High implementation cost
- Risks losing layout flexibility
- Does not address the existing full-refresh hardware path
- Likely solves the wrong bottleneck first

## Risks

### Hardware variability

Different Waveshare panel revisions can behave differently for fast and partial modes.

### Ghosting quality tradeoff

A more aggressive partial-refresh strategy may improve speed but degrade image cleanliness.

### Policy complexity

The system will need a clear and testable policy for when to switch between partial, fast, and full refresh.

### Operational ambiguity

Without instrumentation, it will be hard to know whether a given improvement actually helped.

## Success Criteria

The improvement should be considered successful if:

1. Small-region updates become visibly faster than current full refreshes.
2. Full-screen updates remain reliable and visually clean.
3. Ghosting stays within acceptable bounds through scheduled recovery refreshes.
4. The plugin API remains unchanged for existing plugins.
5. Profiling can clearly show where time is spent in the refresh pipeline.

## Final Recommendation

The right strategy is evolutionary, not revolutionary.

Keep the current render-to-bitmap model.

Improve the display output layer first by introducing diff-aware fast and partial refresh behavior for Waveshare.

Treat Chromium replacement as a later, targeted optimization only if measurements still show it to be a major cost after the display path is improved.
