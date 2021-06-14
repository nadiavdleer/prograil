# minste connectie station kiezen (random)
# kortste connectie kiezen (greedy)
# max 2 uur traject --> opnieuw starten boven als 2 uur overschreden

from code.classes.trajectory import Trajectory
from code.classes.connection import Connection
from code.classes.station import Station
# from code.visualisation.map import map
import copy
import random

# Anne, Nadia, Sarah
def baseline(connections, stations, max_time):
    trajectories = []
    used_connections = []
    # available_stations = copy.deepcopy(stations)
    # available_connections = connections

    while len(used_connections) != len(connections):
        start_station = random.choice(list(stations.values()))

        # start trajectory
        trajectory = Trajectory(start_station)

        # add connections
        while True:
            new_connection = None
            for connection in trajectory.end.connections:
                if not connection.traveled:
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