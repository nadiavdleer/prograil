import matplotlib.pyplot as plt
import numpy as np

# Anne
def map(stations, connections):
    station_names = []
    station_x = []
    station_y = []

    # Sarah & Nadia
    ## add stations info
    for station in stations.values():
        station_names.append(station.name)
        station_x.append(station.x)
        station_y.append(station.y)

    plt.scatter(station_x, station_y)
    
    # give station points names
    for i, txt in enumerate(station_names):
        plt.annotate(txt, (station_x[i], station_y[i]))

    for connection in connections:
        station1 = stations[connection.station1]
        x1 = station1.x
        y1 = station1.y

        station2 = stations[connection.station2]
        x2 = station2.x
        y2 = station2.y
       
        plt.axline((x1,y1), (x2,y2))
        
    # show map
    plt.show()