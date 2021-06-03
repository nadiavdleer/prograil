from code.classes.station import Station
from code.classes.connection import Connection
from code.classes.trajectory import Trajectory
import csv
from ..visualisation.map import map

# Nadia, Anne, Sarah
def load_holland():
    stations = {}
    connections = []
    
    # open stations file
    stations_file = csv.DictReader(open("./data/noord-zuid-holland/StationsHolland.csv"))

    for row in stations_file:
        name = row["station"]
        x = float(row["x"])
        y = float(row["y"])
        
        station = Station(x, y, name)
        stations[station.name] = station
        print(station)


    # open connections file
    connections_file = csv.DictReader(open("./data/noord-zuid-holland/ConnectiesHolland.csv"))

    for row in connections_file:
        station1 = row["station1"]
        station2 = row["station2"]
        time = int(row["distance"])

        connection = Connection(time, station1, station2)
        connections.append(connection)
        print(connection)
    
    # test trajectory
    test_trajectory = Trajectory(stations['Alkmaar'])
    test_trajectory.add_connection(Connection(station1="Alkmaar", station2="Hoorn"))

    print(test_trajectory)

    # show map of stations and connections 
    map(stations, connections, test_trajectory)