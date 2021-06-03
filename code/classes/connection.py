# Anne
class Connection:

    def __init__(self, time, station1, station2): 
        self.time = time 
        self.station1 = station1
        self.station2 = station2
        self.traveled = False

    def set_traveled(self):
        self.traveled = True

    def is_traveled(self):
        return self.traveled

    def __str__(self):
        return f"from: {self.station1} to: {self.station2}"