# by Nadia
class Trajectory:
    # start = station object
    def __init__(self, start):              
        self.start = start
        self.end = None
        self.connections = []

    # add a connection to the trajectory
    def add_connection(self, connection):
        self.connections.append(connection)
        
        if self.end == connection.station1:
            self.end = connection.station2
        else:
            self.end = connection.station1

        self.total_time += connection.time

    def __str__(self):
        return f"start: {self.start} end: {self.end}"
    
