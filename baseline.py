# minste connectie station kiezen (random)
# kortste connectie kiezen (greedy)
# max 2 uur traject --> opnieuw starten boven als 2 uur overschreden

from code.classes.trajectory import Trajectory
from code.classes.connection import Connection
from code.classes.station import Station
from code.visualisation.map import map
import copy
import random

# Anne, Nadia, Sarah
def baseline(connections, stations):
    trajectories = []
    available_stations = copy.deepcopy(stations)

    while True:
        start_station = random.choice(list(available_stations.values()))
        if len(start_station.connections) >= 2:
            break
    # start trajectory
    trajectory = Trajectory(start_station)

    # add connections
    while True:
        new_connection = None
        for connection in trajectory.end.connections:
            if not connection.traveled:
                if new_connection == None or connection.time < new_connection.time:
                    new_connection = connection
        
        if new_connection == None:
            break

        # add new connection to trajectory and set traveled
        print(new_connection)
        print(new_connection.traveled)
        trajectory.add_connection(new_connection)
        new_connection.set_traveled()
        
        # ensure max 2h trajectory
        if trajectory.total_time > 120:
            trajectory.remove_connection(new_connection)
            break

    print(trajectory)
    print(trajectory.total_time)
    print(trajectory.connections)
    
    map(stations, connections, [trajectory])
   