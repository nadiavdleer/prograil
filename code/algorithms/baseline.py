from code.classes.trajectory import Trajectory
from code.classes.connection import Connection
from code.classes.station import Station
import copy
import random


def baseline(connections, stations, max_time):
    """
     algorithm based on random and greedy functions to generate trajectories
     choose a random station to start the trajectory, use a greedy algorithm to generate next connections 
     and add those to trajectory, while ensuring trajectory does not exceed maximum amount of time
    """
    trajectories = []
    used_connections = []

    while len(used_connections) != len(connections):
        # pick a random start station to start trajectory
        start_station = random.choice(list(stations.values()))
        trajectory = Trajectory(start_station)

        # add connections
        while True:
            new_connection = None
            for connection in trajectory.end.connections:
                if not connection.traveled:
                    # pick next connection based on greedy
                    if new_connection == None or connection.time < new_connection.time:
                        new_connection = connection
            
            # end trajectory if no possible route
            if new_connection == None:
                if trajectory.total_time == 0:
                    break
                trajectories.append(trajectory)
                break

            # add new connection to trajectory and set traveled
            trajectory.add_connection(new_connection)
            new_connection.set_traveled()
            used_connections.append(new_connection)
            
            # ensure max 2h trajectory
            if trajectory.total_time > max_time:
                trajectory.remove_connection(new_connection)
                new_connection.traveled = False
                used_connections.remove(new_connection)
                trajectories.append(trajectory)
                break
   
    return trajectories