from utils import position, state
import vecteur, utils


def f0_1(action_completed) :
    return state['direction'] * position['ball'][0] > 0 and state['direction'] * position['player1'][0] < state['direction'] * position['ball'][0]

def f0_2(action_completed) :
    return state['direction'] * position['ball'][0] > 0 and state['direction'] * position['player1'][0] > state['direction'] * position['ball'][0]

def f1_2(action_completed) :
    return action_completed

def f2_3(action_completed) :
    return action_completed

def f3_2(action_completed) :
    ref = vecteur.angle(vecteur.soust_vect(utils.goal_pos(), position['ball'])) 
    return 0.8 * ref > vecteur.angle(vecteur.soust_vect(utils.goal_pos(), position['player1'][:2])) > 1.2 * ref

def f3_4(action_completed) :
    return action_completed

def f4_0(action_completed) :
    return state['direction'] * position['ball'][0] < 0

def f0_5(action_completed) :
    return state['direction'] * position['ball'][0] < 0

def f5_0(action_completed) :
    return state['direction'] * position['ball'][0] > 0

def f5_6(action_completed) :
    return action_completed

def f6_0(action_completed) :
    return action_completed