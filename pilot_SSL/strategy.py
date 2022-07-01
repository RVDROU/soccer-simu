
import vecteur, math, time, utils
from utils import COLOR, BUT, position, state


t1 = utils.timer()
t2 = utils.timer()


def stop(client, player) :
    utils.command(client, player).control(0, 0, 0)
    return True
    
def go_to_ball(client, player) :
    but_opp = utils.goal_opp_pos()
    ball = position['ball']
    robot = position[player]
    v1 = vecteur.soust_vect(ball, but_opp)
    theta = vecteur.angle(v1)
    v2 = vecteur.coord_vect(0.1, theta)
    x, y = vecteur.add_vect(ball, v2)
    return utils.command(client, player).goto((x, y, theta + math.pi/2 + state['direction'] * math.pi/2), wait = False)


def kick(client, player, p = 1 ) :
    global t1
    t1.start(0.7)
    v1 = vecteur.soust_vect(position['ball'], position[player][0:2])
    angle = vecteur.angle(v1)    
    utils.command(client, player).control(2, 0, 0)
    if t1.state() :
        utils.command(client, player).kick(p)
        utils.command(client, player).control(0, 0, 0)
        t1.stop()
        return True
    else :
        return False
    
def go_to_goal(client, player, offset = 0.1) :
    target = state['direction'] * (BUT[0] - offset)
    return utils.command(client, player).goto((target, 0, math.pi/2 + state['direction'] * math.pi/2 ), wait = False)
    
def go_back(client, player, offset = 0.2) :
    theta = position[player][2]
    y = position[player][1]
    x = state['direction'] * (math.fabs(position['ball'][0]) + offset)
    return utils.command(client, player).goto((x, y, theta), wait = False)
    
def go_to_trajectory(client, player) :
    target = utils.goal_pos()
    v1 = vecteur.soust_vect(position['ball'], target)
    theta = vecteur.angle(v1)
    v2 = vecteur.ortho(v1)
    m1 = v1[1] / v1[0]
    m2 = v2[1] / v2[0]
    x = (m1 * position['ball'][0] - m2 * position[player][0] + position[player][1] - position['ball'][1]) / (m1 - m2)
    y = m2 * (x - position[player][0]) + position[player][1]    
    return utils.command(client, player).goto((x, y, theta + math.pi/2 -state['direction'] * math.pi/2), wait = False)
    
def defense(client, player) :
    target = utils.goal_pos(state['direction'])
    v1 = vecteur.soust_vect(position['ball'], target)
    theta = vecteur.angle(v1)
    v2 = vecteur.coord_vect(0.3, theta)
    x, y = vecteur.soust_vect(position['ball'], v2)
#     print('ball : {0} / dest : {1}'.format(ball, (x, y)))
    return utils.command(client, player).goto((x, y, theta + math.pi/2 -state['direction'] * math.pi/2), wait = False)

def goalkeeper(client, player, offset = 0.1) :
    y = max(min(position['ball'][1], 0.3), -0.3)
    x = state['direction'] * (BUT[0] - offset)
    return utils.command(client, player).goto((x, y, math.pi/2 + state['direction'] * math.pi/2), wait = False)

def eject(client, player) :
    global t1
    t1.start(0.7)       
    utils.command(client, player).control(1000, 0, 0)
    if t1.state() :
        utils.command(client, player).control(0, 0, 0)
        t1.stop()
        return True
    else :
        return False
    
    
    
    