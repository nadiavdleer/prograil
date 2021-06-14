import matplotlib.pyplot as plt
import numpy as np

import cartopy.crs as crs
import cartopy.feature as cfeature


# Anne
def map(stations, connections, trajectories, size):
    station_names = []
    station_x = []
    station_y = []

    if size == "Holland":
        coordinates = [4.2,5.1, 53, 51.6]
    else:
        coordinates = [2.9, 7.2, 53.7, 50.7]

    # start map background
    figure = plt.figure(figsize=(7,6))
    ax = figure.add_subplot(1,1,1, projection=crs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.RIVERS)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.STATES)
    ax.set_extent(
        coordinates,
        crs=crs.PlateCarree()
    )
    

    # Sarah & Nadia
    # add stations info
    for station in stations.values():
        station_names.append(station.name)
        station_x.append(station.x)
        station_y.append(station.y)

    plt.scatter(station_x, station_y,transform=crs.PlateCarree())
    
    # give station points names
    for i, txt in enumerate(station_names):
        plt.annotate(txt, (station_x[i], station_y[i]), fontsize=5)

    for connection in connections:
        station1 = connection.station1
        x1 = station1.x
        y1 = station1.y

        station2 = connection.station2
        x2 = station2.x
        y2 = station2.y

        # check if traveled
        if connection.traveled == True:
            color = "b"
        else:
            color = "k"
      
        # create lines between connections
        plt.plot([x1,x2], [y1,y2], color=color, transform=crs.PlateCarree())

    colors = ["cornflowerblue", "tomato", "sienna", "deepskyblue", "firebrick", "palevioletred", "coral", "slategrey", "deeppink", "orange", "gold", "lightgreen", "olive", "darkkhaki", "seagreen", "burlywood", "saddlebrown", "darkslategrey", "slategrey", "grey"]
    c = 0

    for trajectory in trajectories:
        for connection in trajectory.connections:
            station1 = connection.station1
            x1 = station1.x
            y1 = station1.y

            station2 = connection.station2
            x2 = station2.x
            y2 = station2.y

            plt.plot([x1,x2], [y1,y2], color = colors[c], transform=crs.PlateCarree())
        c += 1
        
    # show map
    plt.show()