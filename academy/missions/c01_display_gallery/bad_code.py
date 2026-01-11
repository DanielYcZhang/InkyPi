"""
Bad vs Good (C-01)

Rewrite the bad code using:
- variables for padding/spacing
- a loop

You can run this file to see a text-only preview:
  python3 bad_code.py
"""

# Bad code (read it)
# Draw three boxes without variables or loops
# draw.rectangle((10, 10, 70, 55), outline=(0, 0, 0), width=2)
# draw.text((16, 61), "Box 1", fill=(0, 0, 0))
#
# draw.rectangle((80, 10, 140, 55), outline=(0, 0, 0), width=2)
# draw.text((86, 61), "Box 2", fill=(0, 0, 0))
#
# draw.rectangle((150, 10, 210, 55), outline=(0, 0, 0), width=2)
# draw.text((156, 61), "Box 3", fill=(0, 0, 0))


# Your fix (write below)
def draw_boxes(draw):
    # TODO: replace this with your improved version
    pass


class FakeDraw:
    def rectangle(self, box, outline=None, width=1):
        print(f"rectangle {box} outline={outline} width={width}")

    def text(self, pos, text, fill=None):
        print(f"text {pos} '{text}' fill={fill}")


if __name__ == "__main__":
    print("Running Bad vs Good (C-01) preview...")
    draw_boxes(FakeDraw())
