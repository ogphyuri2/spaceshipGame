#This function call population controller
#The function start create balls and 
#However if the carrier produce more than 20, it will send out hunter to control the population
#I brought this idea from my biology class in high school, that U.S government use wolves to control the population of YellowStone
#The special object will be remove after 1000 cycles.

from ball  import Ball
from floater import Floater
from prey  import Prey
from blackhole import Black_Hole
from pulsator import Pulsator
from hunter import Hunter
from simulton import Simulton
from mobilesimulton import Mobile_Simulton

class Special(Black_Hole):
    countz = 20
    send_the_ball = 10
    radius = 20
    population = 1000
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Special.radius*2,Special.radius*2)
        self.counter = 0
        self.hunter_on = 0
        self.total_count = 0
    
    def update(self, model):
        self.counter += 1
        self.total_count += 1
        if self.counter == Special.send_the_ball:
            model.add(Ball(self._x, self._y))
            model.add(Floater(self._x, self._y))
            self.counter = 0
            self.hunter_on += 2

        if self.hunter_on == Special.countz:
            self.hunter_on = 0
            model.add(Hunter(self._x, self._y))
        if self.total_count == Special.population:
            model.remove(self)

    def display(self, canvas):
        canvas.create_oval(self._x - Special.radius, self._y - Special.radius, self._x + Special.radius, self._y + Special.radius, fill='Pink')
    