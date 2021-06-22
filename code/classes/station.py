class Station:
    def __init__(self, x, y, name):
        """
         create station object and save x and y coordinates, name and all connections from and to that station
        """
        self.x = x
        self.y = y
        self.name = name
        self.connections = []

    def __str__(self):
        return f"{self.name}"