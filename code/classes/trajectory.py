# by Nadia
class Trajectory:
    # start = station object
    def __init__(self, start):              
        self.start = start
        self.end = start
        self.connections = []
        self.itinerary = [start.name]
        self.total_time = 0

    # add a connection to the trajectory
    def add_connection(self, connection):
        self.connections.append(connection)
        self.total_time += connection.time

        if self.end == connection.station1:
            self.end = connection.station2
            self.itinerary.append(self.end.name)
            # print(f"{self.itinerary}")
        elif self.end == connection.station2:
            self.end = connection.station1
            self.itinerary.append(self.end.name)
            # print(f"{self.itinerary}")

    # remove connections
    def remove_connection(self, connection):
        self.connections.remove(connection)
        self.total_time -= connection.time

        # end remove
        if self.end == connection.station1:
            self.end = connection.station2
            del self.itinerary[-1]
        elif self.end == connection.station2:
            self.end = connection.station1
            del self.itinerary[-1]

        # remove from start
        elif self.start == connection.station1:
            self.start = connection.station2
            self.itinerary.remove(connection.station1.name)
        elif self.start == connection.station2:
            self.start = connection.station1
            self.itinerary.remove(connection.station2.name)
    
    def __str__(self):
        return f"start: {self.start} end: {self.end}"
    
