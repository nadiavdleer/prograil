class Timetable:
    def __init__(self, trajectories):
        """
         this class is used to calculate the quality of our solution
        """
        self.trajectories = trajectories
        self.score = 0
        self.traveled_connections = []

    def quality(self, connections):
        """
         execute target function and return K as the quality of generated trajectories
        """
        used_connections = []
        T = 0
        Min = 0

        for trajectory in self.trajectories:
            T += 1
            Min += trajectory.total_time 
            for connection in trajectory.connections:
                used_connections.append(connection)
                
        p = 0
        total_connections = 0

        for connection in connections:
            total_connections += 1
            if connection in used_connections:
                p += 1

        p = p / total_connections
        K = p*10000 - (T*100 + Min)

        return K