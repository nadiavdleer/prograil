from code.classes.station import Station
from code.classes.connection import Connection
from code.classes.trajectory import Trajectory
import csv

def load_holland():
    """
      open data files for Holland and create station and connection objects 
    """
    stations = {}
    connections = []
    
    # open stations file and create station objects
    stations_file = csv.DictReader(open("./data/noord-zuid-holland/StationsHolland.csv"))

    for row in stations_file:
        name = row["station"]
        x = float(row["x"])
        y = float(row["y"])
        
        station = Station(x, y, name)
        stations[station.name] = station

    # open connections file and create connection objects
    connections_file = csv.DictReader(open("./data/noord-zuid-holland/ConnectiesHolland.csv"))

    for row in connections_file:
        station1 = stations[row["station1"]]
        station2 = stations[row["station2"]]
        time = int(row["distance"])

        connection = Connection(time, station1, station2)
        connections.append(connection)

        # add connection to station object
        stations[station1.name].connections.append(connection)
        stations[station2.name].connections.append(connection)

    return stations, connections

def load_nationaal():
    """
     open data files for entire Netherlands and create station and connection objects 
    """
    stations = {}
    connections = []
    
    # open stations file and create station objects
    stations_file = csv.DictReader(open("./data/nederland/StationsNationaal.csv"))

    for row in stations_file:
        name = row["station"]
        x = float(row["x"])
        y = float(row["y"])
        
        station = Station(x, y, name)
        stations[station.name] = station

    # open connections file and create connection objects
    connections_file = csv.DictReader(open("./data/nederland/ConnectiesNationaal.csv"))

    for row in connections_file:
        station1 = stations[row["station1"]]
        station2 = stations[row["station2"]]
        time = float(row["distance"])

        connection = Connection(time, station1, station2)
        connections.append(connection)

        # add connection to station object
        stations[station1.name].connections.append(connection)
        stations[station2.name].connections.append(connection)

    return stations, connections