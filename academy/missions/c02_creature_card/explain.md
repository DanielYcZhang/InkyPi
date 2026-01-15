# Explain-Back (C-02)

1. In one sentence, explain what this file does overall.
   bro can we remove this question its so shit

2. Pick one line from `c02_creature_card.py` and explain it in your own words.
   img = Image.new('1', (w, h), 255)
   this lines goal is to create a white canvas that can be drawn on. Image.new is the function that makes the image and takes 3 different arguements. The '1' means that it is black and white pixels and the (w,h) gets the width and height of the canvas, the (255) makes the background white so you can draw black text and stuff on the sreen.

3. Concept checkpoints:

   - Explain the difference between a class and an object.
     the difference between a class and an object is that, a class is code that defines what something is, it tells you what properties and methods it has. you only need to write the class once and then it can be used multiple times after that, it is a template. An object is the actual thing, and its based on the class but it uses actual real values for the properties instead of variables/placeholders. You can create multiple objects from one class, it just uses the same template but can have different names and values.
   - Explain why `self.name` is a property.
     self.name is a property because it is needed to make the objects unique from each other. without it, each object would have the same name or no name at all.
   - Explain why `draw` belongs inside the class.
     draw belongs inside the class because it is something that all the creature objects can do by themselves. It uses its own properties to draw the card on the screen, if the method was outside the class you would have to tell it to draw it by yourself every time, but if its inside the class the ceature can draw it automatically.

4. Reflection: What makes a property different from a normal variable?
   A property is different from a normal variable because a property is from an object and stores data which is from that object, normal variables don't belong to an object or class and they just store stuff.
