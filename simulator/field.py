'''Version avec la gestion du déplacement (jacobien) opérationnel'''


import pygame, sys, math, os
import numpy as np
from threading import Thread, Lock
from time import sleep
from utils import *

class field() :
    def __init__(self) :
        self.__rect = [((25, 25), (25+193, 25+2)), ((25, 25), (25+2, 25+132)), ((25+193-2, 25), (25+193, 25+132)), ((25, 25+132-2), (25+193, 25+132)), \
                      ((25, 126), (37,126+2)), ((25, 56), (37,56+2)), ((206, 126), (218,126+2)), ((206, 56), (218, 56+2)), ((50, 69), (50+2,113)), ((193, 69), (193+2,113))]
           
        self.size = (0, 0)
        
        
    def in_playing_zone(self, pos) :
        (x, y) = pos
        return (x > 25 and x < 25+193 and y > 25 and y < 25+132)
    
    def in_goal(self, pos) :
        (x, y) = pos
        return not(self.in_playing_zone(pos)) and 61+60 > y > 61
    
    def over_white_line(self, pos) :
        (x,y) = pos
        for rect in self.__rect :
            if rect[1][0] > x > rect[0][0] and rect[1][1] > y > rect[0][1] :
                return True
        return False



