''' Classe vec en cours de developpement'''

import math
import numpy as np

PI = math.pi
ROUGE = (255,0,0)
BLEU = (0,0,255)
GREEN = (0,150,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCALE = 5
FIELD_SIZE = (183*SCALE,122*SCALE)
BORDER = 15*SCALE
WINDOW_SIZE = (FIELD_SIZE[0]+2*BORDER, FIELD_SIZE[1]+2*BORDER)
GOAL_WIDTH = 60*SCALE
PI = math.pi
GEAR_RATIO = 210
   
    
def rad2deg(angle) :
    return angle * 180 / PI

def deg2rad(angle) :
    return angle * PI / 180

def angle_wrap(alpha):
    return ((alpha + PI) % (2 * PI)) - PI

def rot_matrix(theta) :
    cos, sin = np.cos(theta), np.sin(theta)
    return np.array([[cos, sin, 0],
                    [-sin, cos, 0],
                    [0,0,1]])

def kinematic(radius) :
    return np.array([[-np.sin(PI/3), np.cos(PI/3), radius],
                    [0, -1, radius],
                    [np.sin(PI/3), np.cos(PI/3), radius]])


def kinematic_inv(radius) :
    return np.linalg.inv(kinematic(radius))