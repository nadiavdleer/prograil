# Anne, Nadia, Sarah
def quality(connections, trajectories):
    p = 0
    total_connections = 0
    total_trajectories = 0

    for connection in connections:
        total_connections += 1
        if connection.traveled == True:
            p += 1
    p = p / total_connections

    T = 0
    Min = 0
    for trajectory in trajectories:
        T += 1
        Min += trajectory.total_time 

    print(p)
    print(T)
    print(Min)       
        
    K = p*10000 - (T*100 + Min)
    return K