from code.classes.connection import Connection
from code.classes.station import Station
from code.classes.trajectory import Trajectory
from code.loaders.loader import load_holland

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
        
    K = p*10000 - (T*100 + Min)
    return K


if __name__ == "__main__":
    load_holland()

    