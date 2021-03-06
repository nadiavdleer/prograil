class Trajectory:
    def __init__(self, start):
        """
         trajectory object is a collection of connections
        """             
        self.start = start
        self.end = start
        self.connections = []
        self.itinerary = [start.name]
        self.total_time = 0
        self.score = 0

    def add_connection(self, connection):
        """
         add a connection to a trajectory
        """
        self.connections.append(connection)
        self.total_time += connection.time

        if self.end == connection.station1:
            self.end = connection.station2
            self.itinerary.append(self.end.name)
        elif self.end == connection.station2:
            self.end = connection.station1
            self.itinerary.append(self.end.name)

    def remove_connection(self, connection):
        """
         remove a connection from a trajectory
        """
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

    def quality(self, connections):
        """
         return quality score of a trajectory
        """
        p = 0
        total_connections = 0 

        for connection in connections:
            total_connections += 1
            if connection in self.connections:
                p += 1
                
        p = p / total_connections
        T = 1
        Min = self.total_time
        K = p*10000 - (T*100 + Min)

        return K

    def __str__(self):
        return f"start: {self.start} end: {self.end}"