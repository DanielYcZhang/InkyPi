"""
Bad vs Good (M-08)

Rewrite this using a loop and spacing variables.

You can run this file to see a text-only preview:
  python3 bad_code.py
"""

# Bad code (read it)
# Repeated dots without a loop
# draw.ellipse((10, 80, 22, 92), fill=(0, 0, 0))
# draw.ellipse((30, 80, 42, 92), fill=(0, 0, 0))
# draw.ellipse((50, 80, 62, 92), fill=(0, 0, 0))


# Your fix (write below)
def draw_dots(draw):
    # TODO: replace this with your improved version
    pass


class FakeDraw:
    def ellipse(self, box, fill=None):
        print(f"ellipse {box} fill={fill}")


if __name__ == "__main__":
    print("Running Bad vs Good (M-08) preview...")
    draw_dots(FakeDraw())
