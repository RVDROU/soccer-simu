import rsk, time, utils, conditions
import strategy



class State_graph() :
    def __init__(self, client, strategy, init_state = 'f0') :
        self.graph = strategy
        self.state = init_state
        self.last = init_state


strategy_p1 = {'f0' : {'job' : strategy.stop , 'successors' : {'f1' : conditions.f0_1, 'f2' : conditions.f0_2, 'f5' : conditions.f0_5}, 'entry' : None, 'exit' : None},
                'f1' : {'job' : strategy.go_back  , 'successors' : {'f2' : conditions.f1_2}, 'entry' : None, 'exit' : None},
                'f2' : {'job' : strategy.go_to_trajectory , 'successors' : {'f3' : conditions.f2_3}, 'entry' : None, 'exit' : None},
                'f3' : {'job' : strategy.go_to_goal , 'successors' : {'f2' : conditions.f3_2, 'f4' : conditions.f3_4}, 'entry' : None, 'exit' : None},
                'f4' : {'job' : strategy.goalkeeper , 'successors' : {'f0' : conditions.f4_0}, 'entry' : None, 'exit' : None},
                'f5' : {'job' : strategy.go_to_ball , 'successors' : {'f0' : conditions.f5_0, 'f6' : conditions.f5_6}, 'entry' : None, 'exit' : None},
                'f6' : {'job' : strategy.kick , 'successors' : {'f0' : conditions.f6_0}, 'entry' : None, 'exit' : utils.stop(strategy.t1)}
                }

strategy_p2 = {'f0' : {'job' : strategy.defense , 'successors' : {}, 'entry' : None, 'exit' : None},
              }
player = ['player1', 'player2']

with rsk.Client(host='172.19.39.223', key='') as client :
    utils.update_direction(client)
    client.on_update = utils.update
    time.sleep(0.2)
    controler  = [State_graph(client, strategy_p1), State_graph(client, strategy_p2)]
    while True :
        for i in [0] :
            state = controler[i].state
            print(state, end = ' ')
            if  controler[i].state != controler[i].last and controler[i].graph[state]['entry'] is not None :
                controler[i].graph[state]['entry']
            res = controler[i].graph[state]['job'](client, player[i])
            controler[i].last = controler[i].state
            
            for next_state in controler[i].graph[state]['successors'] :
                if controler[i].graph[state]['successors'][next_state](res) :
                    controler[i].state = next_state
                    break
            
            if  controler[i].state != controler[i].last and controler[i].graph[state]['exit'] is not None :
                controler[i].graph[state]['exit']
        print(' ')
        
            
                    
            