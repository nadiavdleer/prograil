import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as crs
import cartopy.feature as cfeature

def map(stations, connections, trajectories, size):
    """
     make a map of North- and South-Holland or the entire Netherlands
     plot all the stations and connections
     give each trajectory a different color
    """
    station_names = []
    station_x = []
    station_y = []
    
    # if map exists, determine map size, else return no map
    if size == "Holland":
        coordinates = [4.2,5.1, 53, 51.6]
    elif size == "Nationaal":
        coordinates = [2.9, 7.2, 53.7, 50.7]
    else:
        return 1 

    # start map background
    figure = plt.figure(figsize=(7,6))
    ax = figure.add_subplot(1,1,1, projection=crs.PlateCarree())

    # add desired map features
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
        # plot all connections
        station1 = connection.station1
        x1 = station1.x
        y1 = station1.y

        station2 = connection.station2
        x2 = station2.x
        y2 = station2.y

        # create lines between connections
        plt.plot([x1,x2], [y1,y2], color='k', transform=crs.PlateCarree())

    # make colors list used in plotting trajectories
    colors = ["purple", "tomato", "sienna", "rosybrown", "firebrick", "palevioletred", "coral", "slategrey", "deeppink", "orange", "gold", "lightgreen", "olive", "darkkhaki", "seagreen", "burlywood", "saddlebrown", "plum", "slategrey", "grey"]
    c = 0

    # plot all trajectories
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
    return 0