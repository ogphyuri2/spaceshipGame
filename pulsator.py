# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
from prey import Prey

class Pulsator(Black_Hole):
    count = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.counter = 0
        
    def update(self,model):
        emp_set = Black_Hole.update(self,model)
        if len(emp_set) == 0:
            self.counter += 1
            if self.counter == Pulsator.count:
                self.counter = 0
                self.change_dimension(-1,-1)
            if self.get_dimension() == (0,0):
                model.remove(self)
        else:
            self.counter = 0
            self.change_dimension(1,1)
        return emp_set
