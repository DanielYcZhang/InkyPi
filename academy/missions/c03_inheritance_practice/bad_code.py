"""
Bad vs Good (C-03)

Rewrite this so the subclass calls super().draw(...) and only adds the badge.

You can run this file to see a text-only preview:
  python3 bad_code.py
"""

# Bad code (read it)
# class PetCard(BaseCard):
#     def draw(self, draw, w, h):
#         # Repeats the base drawing instead of reusing it
#         padding = 12
#         draw.rectangle((padding, padding, w - padding, h - padding), outline=(0, 0, 0), width=2)
#         draw.text((padding + 8, padding + 8), "Pet Profile", fill=(0, 0, 0))
#
#         # Badge
#         draw.rectangle((w - 76, 16, w - 16, 38), outline=(0, 0, 0), width=2)
#         draw.text((w - 70, 20), "LV 5", fill=(0, 0, 0))


class BaseCard:
    def __init__(self, title):
        self.title = title

    def draw(self, draw, w, h):
        draw.rectangle((12, 12, w - 12, h - 12), outline=(0, 0, 0), width=2)
        draw.text((20, 20), self.title, fill=(0, 0, 0))


# Your fix (write below)
class PetCard(BaseCard):
    # TODO: implement draw() using super()
    pass


class FakeDraw:
    def rectangle(self, box, outline=None, width=1):
        print(f"rectangle {box} outline={outline} width={width}")

    def text(self, pos, text, fill=None):
        print(f"text {pos} '{text}' fill={fill}")


if __name__ == "__main__":
    print("Running Bad vs Good (C-03) preview...")
    draw = FakeDraw()
    try:
        card = PetCard("Pet Profile", "LV 5")
        card.draw(draw, 200, 100)
    except Exception as exc:
        print(f"Error running your PetCard: {exc}")
