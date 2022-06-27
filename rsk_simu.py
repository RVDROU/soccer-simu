'''Version avec la gestion du déplacement (jacobien) opérationnel'''


import pygame, math
import numpy as np
from threading import Thread, Lock
from time import sleep
from utils import *
from simulator import *
from ball import *
from field import *
from robot import *


class Rsk_simu() :
    ROBOT_SIZE = (2, 7)
    INIT_POSE = {'blue' : [(-40, 25, 0), (-40, -25, 0)],
                 'green' : [(40, 25, 90), (40, -25, 90)]}    
    def __init__(self) :
        self.robots = {'green' : {}, 'blue' : {}}
        self.ball = None
        self.simu = Simulator(40)
        
    def add_robot(self, color) :
        robot = Robot(color)
        robot.set_size(Rsk_simu.ROBOT_SIZE)
        n = len(self.robots[color])
        robot.set_pos(Rsk_simu.INIT_POSE[color][n])
        self.simu.add(robot)
        self.robots[color][n+1] = robot
        self.green1 = self.robots['green'].get(1)
        self.green2 = self.robots['green'].get(2)
        self.blue1 = self.robots['blue'].get(1)
        self.blue2 = self.robots['blue'].get(2)
        
    
    def add_ball(self) :
        self.ball = Ball() 
        self.simu.add(self.ball)    
       
        
    def run(self) :
        self.simu.run()

###### Programme de test ##########
# client = Rsk_simu()
# client.add_robot('blue')
# client.add_ball()
# client.run()
# while True :
#     client.blue1.goto((-40, -25, 0))
#     client.blue1.goto((40, -25, 0))
#     client.blue1.goto((40, 25, 0))
#     client.blue1.goto((-40, 25, 0))
#     client.blue1.goto((0, 0, 0))
 




