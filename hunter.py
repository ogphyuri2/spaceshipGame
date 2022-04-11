# The Hunter class is derived (in order) from both Pulsator and Mobile_Simulton.
#   It updates/displays like its Pulsator base, but is also mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2

class Hunter(Pulsator, Mobile_Simulton):  
    distance_for_target = 200
    
    def __init__(self,x,y):

        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,20,20,0,5)
        Mobile_Simulton.randomize_angle(self)
        
    def update(self, model):
        eaten_set = Pulsator.update(self, model)
        new_set1 = model.find(lambda k: isinstance(k, Prey))
        new_set2 = set()
        for i in new_set1:
            if self.distance(i.get_location()) <= self.distance_for_target:
                new_set2.add(i)
        final_list = []
        if len(new_set2) != 0:
            for k in new_set2:
                final_list.append((k.get_location(),self.distance(k.get_location())))
            new_list = sorted(final_list, key=lambda x:x[1])
            new_x,new_y  = new_list[0][0]
            self.set_angle(atan2(new_y-self.get_location()[1] , new_x - self.get_location()[0]))
        Mobile_Simulton.move(self)
        return eaten_set
