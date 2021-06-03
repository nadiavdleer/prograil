import matplotlib.pyplot as plt
import numpy as np

# Anne
def map(stations, connections, trajectories):
    station_names = []
    station_x = []
    station_y = []
    trajectories = []

    # Sarah & Nadia
    # add stations info
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

        # check if traveled
        if connection.traveled == True:
            color = "b"
        else:
            color = "k"
      
        # create lines between connections
        plt.plot([x1,x2], [y1,y2], color=color)

    colors = ["lime", "indigo", "coral", "orange", "saddlebrown", "burlywood", "palevioletred", "grey", "darkkhaki", "seagreen", "tomato", "darkslategrey", "deeppink", "slategrey", "olive", "lightgreen", "gold", "sienna", "wheat", "firebrick"]
    c = 0
    for trajectory in trajectories:
        for connection in trajectory.connections:
            station1 = stations[connection.station1]
            x1 = station1.x
            y1 = station1.y

            station2 = stations[connection.station2]
            x2 = station2.x
            y2 = station2.y

            plt.plot([x1,x2], [y1,y2], color = colors[c])
    c += 1
        
    # show map
    plt.show()