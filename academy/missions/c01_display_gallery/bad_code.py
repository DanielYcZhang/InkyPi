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
    
    #variables
    start_x = 10 #where first box starts vertically
    starty_y = 10 #where the boxes start horizontally
    box_width = 60
    box_height = 45
    gap = 10

    for i in range(3):
        
        #i=0, first box -> 10+(0x70)=10
        #i=1, second box -> 10+(1x70)=70
        #i=2, third box -> 10+(2x70)=150
        current_x = start_x + i * (box_width + gap)

        #box postitions
        x1 = current_x #horizontal position of the left of the box
        y1 = starty_y #vertical position of the top of the box(always 10)
        x2 = current_x + box_width #x1 + width of box
        y2 = starty_y + box_height #y1 + height of box

        #actually drawing
        draw.rectangle((x1, y1, x2, y2), outline=(0, 0, 0), width=2) #0,0,0 means black colour
        draw.text((x1 + 6, y2 + 6), f"Box {i+1}", fill=(0, 0, 0)) #+6 give space from edge, fstring, just types "Box (what number box it is)" 0,0,0 means black colour

class FakeDraw:
    def rectangle(self, box, outline=None, width=1):
        print(f"rectangle {box} outline={outline} width={width}")

    def text(self, pos, text, fill=None):
        print(f"text {pos} '{text}' fill={fill}")


if __name__ == "__main__":
    print("Running Bad vs Good (C-01) preview...")
    draw_boxes(FakeDraw())
