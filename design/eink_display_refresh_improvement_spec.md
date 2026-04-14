# Spec: E-Ink Display Refresh Improvement

## Assumptions I'm Making

1. The first implementation target is the current Waveshare 7.5 inch black-and-white setup using `epd7in5_V2`.
2. Existing plugin APIs and the current `plugin -> PIL.Image -> DisplayManager` contract must remain unchanged.
3. We want a low-risk, evolutionary change in the display layer before considering any plugin rendering rewrite.
4. Development and most automated verification will run in `--dev` mode without real hardware, with hardware behavior validated manually on-device.
5. Partial refresh support can be introduced first for compatible monochrome Waveshare drivers, even if other display types continue using the current full-refresh behavior.

## Objective

Improve the perceived refresh speed of InkyPi on supported Waveshare e-ink displays by replacing the current always-full-refresh path with a measured, policy-driven refresh strategy.

Today the Waveshare path always performs:

`Init -> Clear -> Full display -> Sleep`

That is reliable but pessimistic. The goal is to preserve output correctness while making small or incremental updates materially faster through instrumentation, previous-frame tracking, and selective use of full, fast, and partial refresh modes.

Primary user outcomes:

- Small-screen changes refresh noticeably faster than the current 3 to 5 second full-screen path.
- Full-screen updates remain reliable and visually clean.
- Existing plugins keep working without code changes.
- The system can show where time is spent in rendering versus display transfer.

## Tech Stack

- Python 3
- Flask-based application runtime
- Pillow for final bitmap generation
- Waveshare Python EPD drivers under `src/display/waveshare_epd/`
- Pytest for automated tests
- Raspberry Pi hardware for final validation of panel behavior

## Commands

Setup:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r install/requirements-dev.txt
bash install/update_vendors.sh
```

Run development server:

```bash
python src/inkypi.py --dev
```

Run all tests:

```bash
pytest
```

Run a targeted test file:

```bash
pytest tests/test_model.py
```

## Project Structure

```text
design/                                   Feature design docs and implementation specs
src/display/display_manager.py            Top-level display orchestration after plugin rendering
src/display/abstract_display.py           Shared display interface
src/display/waveshare_display.py          Waveshare-specific wrapper and refresh policy entry point
src/display/waveshare_epd/                Vendor-style panel drivers and hardware primitives
src/utils/image_utils.py                  HTML screenshot and image transformation utilities
src/plugins/                              Plugins that render the source PIL images
tests/                                    Unit and integration-style automated tests
docs/development.md                       Local development workflow
```

## Code Style

Follow the existing Python style in this repository:

- Prefer small methods with one hardware or policy responsibility each.
- Use `logger.info(...)` for lifecycle events and `logger.debug(...)` for lower-level timings or diagnostics.
- Keep display-specific logic inside the Waveshare layer rather than leaking panel details into plugin code.
- Use explicit guard clauses for unsupported states and missing inputs.

Example style:

```python
def display_image(self, image, image_settings=[]):
    logger.info("Displaying image to Waveshare display.")
    if not image:
        raise ValueError("No image provided.")

    self.epd_display_init()
    self.epd_display.Clear()
    self.epd_display.display(self.epd_display.getbuffer(image))
    self.epd_display.sleep()
```

For this feature, prefer adding narrowly scoped helper methods such as:

- frame diff calculation
- refresh mode selection
- region alignment
- ghosting recovery checks
- timing instrumentation

## Testing Strategy

Automated tests:

- Add unit tests for diff bounding-box calculation and empty-diff detection.
- Add unit tests for region alignment to panel byte boundaries.
- Add unit tests for refresh mode selection policy using synthetic image-change scenarios.
- Add unit tests for ghosting recovery rules such as "force full refresh after N partial updates."
- Add tests that confirm unsupported displays continue to use the legacy full-refresh path.

Manual validation on hardware:

- Measure cold boot first refresh timing.
- Measure small-region update timing against the current baseline.
- Measure broad-but-not-total update timing for fast refresh candidates.
- Verify scheduled recovery full refresh resets visible ghosting acceptably.
- Verify the display still enters a safe low-power state when deferral is disabled or the refresh session ends.

Testing levels by concern:

- Pure policy logic: unit tests in `tests/`
- Display wrapper integration behavior: mockable tests around `WaveshareDisplay`
- Real waveform quality, ghosting, and timing: manual hardware validation on the target panel

## Boundaries

- Always:
  - Preserve the existing plugin rendering contract.
  - Keep a safe fallback path to full refresh when policy inputs are missing or unsupported.
  - Separate instrumentation so render time and display time can be observed independently.
  - Scope initial support to compatible Waveshare monochrome displays, starting with `epd7in5_V2`.

- Ask first:
  - Adding new third-party dependencies
  - Changing persistent device configuration schema
  - Broadening the first implementation to multiple panel families at once
  - Rewriting HTML-based plugins or replacing Chromium as part of this feature

- Never:
  - Break existing plugins by requiring plugin-level refresh annotations in the first iteration
  - Remove the ability to do a full clean refresh
  - Ship a partial-refresh-only mode with no ghosting recovery path
  - Tie core refresh correctness to Chromium-specific behavior

## Non-Goals

- Rewriting HTML-rendered plugins in Pillow
- Building a widget-level compositor or scene graph
- Generalizing partial refresh to every supported display in the first pass
- Perfectly eliminating all ghosting under every usage pattern

## Success Criteria

1. `WaveshareDisplay` can choose between at least full refresh and partial refresh for `epd7in5_V2`, with fast refresh added when the driver support is stable enough to use.
2. The display path no longer performs unconditional `Clear()` on every refresh for supported incremental-update cases.
3. The system stores or reconstructs the previous displayed frame well enough to compute a changed bounding box.
4. Small-region updates are observably faster than the current full-screen baseline on target hardware.
5. Existing plugins require no code changes to benefit from the new display policy.
6. Timing instrumentation can distinguish plugin/image generation time from display transfer and panel busy time.
7. The implementation includes a deterministic recovery rule that forces a full refresh after repeated partial updates or other ghosting-risk conditions.
8. Unsupported displays or unsupported scenarios fall back safely to the legacy full-refresh behavior.

## Open Questions

1. Should previous-frame state live only in memory for the current process, or should it be reconstructed from the last saved display image on startup?
2. What percentage-of-screen-change threshold should switch from partial refresh to fast or full refresh for `epd7in5_V2`?
3. Do we want sleep deferral in the first implementation, or should phase one still sleep after each update while improving refresh mode selection?
4. How should the refresh policy be configured: hard-coded for the initial target panel, device-config driven, or both?
5. Should the first milestone include `init_fast`, or should we ship full plus partial first and add fast-refresh after hardware measurements?
