# by Nadia
class Trajectory:
    # start = station object
    def __init__(self, start):              
        self.start = start.name
        self.end = start.name
        self.connections = []
        self.total_time = 0

    # add a connection to the trajectory
    def add_connection(self, connection):
        self.connections.append(connection)
        self.total_time += connection.time

        if self.end == connection.station1:
            self.end = connection.station2
        else:
            self.end = connection.station1

    # remove connections
    def remove_connection(self, connection):
        self.connections.remove(connection)
        self.total_time -= connection.time

        # end remove
        if self.end == connection.station1:
            self.end = connection.station2
        elif self.end == connection.station2:
            self.end = connection.station1

        # remove from start
        elif self.start == connection.station1:
            self.start = connection.station2
        elif self.start == connection.station2:
            self.start = connection.station1
    
    def __str__(self):
        return f"start: {self.start} end: {self.end}"
    
