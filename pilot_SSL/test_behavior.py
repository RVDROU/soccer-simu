import rsk, time, utils, strategy


player = 'player1'
with rsk.Client(host='172.19.39.223', key='') as client :
    client.on_update = utils.update
    time.sleep(1)
    end = False
    while True :
        strategy.goalkeeper(client, player)
            

        
