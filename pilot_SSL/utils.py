''' Classe vec en cours de developpement'''

import math, time
import numpy as np


# Global variables
BUT = (0.83,0)
COLOR = 'green'
position, state = {}, {}

def command(client, player) :
    if player == 'player1' :
        return client.robots[COLOR][1]
    elif player == 'player2' :
        return client.robots[COLOR][2]
    else : raise Exception('Unknown player')

def nada() :
    pass

def goal_pos() :
    return (state['direction'] * BUT[0], BUT[1])

def goal_opp_pos() :
    return (-state['direction'] * BUT[0], BUT[1])

def update_direction(client) :
    if client.referee['teams'][COLOR]['x_positive'] :
        return 1
    else :
        return -1

def sign(a) :
    '''return sign of a '''
    if a < 0 :
        return -1
    else :
        return 1

def stop(timer) :
    timer.stop()
    
    
def update(client, dt) :
    global position, state
    opponent_color = {'green' : 'blue', 'blue' : 'green'}
    
    ## Update position
    key = ['ball', 'player1', 'player2', 'opponent1', 'opponent2']
    value = [client.ball, client.robots[COLOR][1].pose, client.robots[COLOR][2].pose,
             client.robots[opponent_color[COLOR]][1].pose, client.robots[opponent_color[COLOR]][2].pose]
    for i in range(len(key)) :
        if value[i] is not None :
            position[key[i]] = value[i]
    
    ## Update state
    key = ['direction']
    value = [update_direction(client)]        
    for i in range(len(key)) :
        if value[i] is not None :
            state[key[i]] = value[i]
    
    return position, state
   
class timer() :
    def __init__(self) :
        self.__flag = False
        self.__t_start = 0
        self.__delta_t = 0
    
    def start(self, val) :
        if not self.__flag :
            self.__flag = True
            self.__t_start = time.time()
            self.__delta_t = val
    
    def state(self) :
        return time.time() - self.__t_start >= self.__delta_t
    
    def stop(self) :
        self.__flag = False    