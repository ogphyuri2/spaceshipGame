# The Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class derived from Prey) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radius*2,Black_Hole.radius*2)
        
    def contain(self, xy):
        if xy.distance((self._x, self._y)) < Black_Hole.radius:
            return True
        else:
            return False
    def update(self, model):
        eaten = model.find(lambda k: isinstance(k,Prey))
        new_set = set()
        for i in eaten:
            if self.contain(i) == True:
                new_set.add(i)
        for e in new_set:
            model.remove(e)
        return new_set

    def display(self, canvas):
        canvas.create_oval(self._x - self._width/2, self._y - self._height/2, self._x + self._width/2, self._y + self._height/2, fill='black')