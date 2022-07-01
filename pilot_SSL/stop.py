import rsk
with rsk.Client(host='172.19.39.223', key='') as client:

    for r in ['green', 'green', 'blue', 'blue'] :
        for i in range(1,3) :
            client.robots[r][i].control(0, 0., 0.)
