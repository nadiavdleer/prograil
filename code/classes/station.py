# by Sarah
class Station:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.connections = []
        
    # return all connections from station
    def get_connection(self):
        return self.connections

    # check if there is connection between stations
    def has_connection(self, station):
        if station in self.connections:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}"

