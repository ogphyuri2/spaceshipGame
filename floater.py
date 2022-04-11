# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import random

class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 0, 5)
        self.randomize_angle()

    def update(self,model):
        a = random.uniform(0, 1)
        foo = [-0.5,0.5]
        if a <= 0.3:
            self._speed += random.choice(foo)
            self._angle += random.choice(foo)
            if self._speed < 3 or self._speed > 7:
                self._speed = 5
        self.move()

    def display(self,the_canvas):
        the_canvas.create_oval(self._x - Floater.radius, self._y - Floater.radius, self._x + Floater.radius, self._y + Floater.radius, fill='red')
    

    
