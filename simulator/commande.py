import vecteur
import test, math

def drive(client) :
    but = (78,0)
    ball = client.ball.position
    robot = client.blue1.position
    v1 = vecteur.soust_vect(ball, but)
    theta = vecteur.angle(v1)
    v2 = vecteur.coord_vect(7, theta)
    x, y = vecteur.add_vect(ball, v2)
#     print('ball : {0} / dest : {1}'.format(ball, (x, y)))
    client.blue1.goto((x, y, theta + math.pi), wait = False)

test.test(drive)