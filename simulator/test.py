from rsk_simu import *
from sys import exit
from time import sleep



def test(f) :
    client = Rsk_simu()
    client.add_robot('blue')
    client.add_ball()
    client.ball.goto(0, 0)
    client.run()
    while True :
        f(client)
        sleep(0.01)
        if not client.simu.is_running() :
            exit()
            break

         
