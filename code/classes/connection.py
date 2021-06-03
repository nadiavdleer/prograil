# Anne
class Connection:

    def __init__(self, time, station1, station2): 
        self.time = time 
        self.station1 = station1
        self.station2 = station2
        self.traveled = False

    def set_traveled(self):
        self.traveled = True

    def __str__(self):
        return f"{self.station1} - {self.station2} : {self.time} minutes"