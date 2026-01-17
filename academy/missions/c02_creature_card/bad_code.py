"""
Bad vs Good (C-02)

Rewrite the bad code using a Creature class with properties and a draw() method.

You can run this file to see a text-only preview:
  python3 bad_code.py
"""

# Bad code (read it)
# Lots of separate variables, no class
# name = "Pip"
# species = "Cat"
# level = 5
#
# draw.text((20, 20), "Name: " + name, fill=(0, 0, 0))
# draw.text((20, 40), "Species: " + species, fill=(0, 0, 0))
# draw.text((20, 60), "Level: " + str(level), fill=(0, 0, 0))


# Your fix (write below)
class Creature:
    def __init__(self, name, species, level):
        # putting self makes it remember it forever
        # def starts a new command
        # __init__ tells the code to run the stuff automatically
        self.name = name
        self.species = species
        self.level = level

    def draw(self, draw_tool, x, y):
        draw_tool.text((x, y), f"Name: {self.name}", fill=(0))
        draw_tool.text((x, y + 20), f"Species: {self.species}", fill=(0))
        draw_tool.text((x, y + 40), f"Level: {self.level}", fill=(0))


class FakeDraw:
    def text(self, pos, text, fill=None):
        print(f"text {pos} '{text}' fill={fill}")


if __name__ == "__main__":
    print("Running Bad vs Good (C-02) preview...")
    draw = FakeDraw()
    try:
        creature = Creature("Pip", "Cat", 5)
        creature.draw(draw, 200, 100)
    except Exception as exc:
        print(f"Error running your Creature: {exc}")
