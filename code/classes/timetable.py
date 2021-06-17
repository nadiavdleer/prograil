class Timetable:
    def __init__(self, trajectories):
        self.trajectories = trajectories
        self.score = 0
        self.traveled_connections = []

    def quality(self, connections):
        p = 0
        total_connections = 0
        
        time = 0 

        for connection in connections:
            total_connections += 1
            if connection.traveled == True:
                p += 1
                time += connection.time
        p = p / total_connections

        T = 0
        Min = 0
        for trajectory in self.trajectories:
            T += 1
            Min += trajectory.total_time 
            # print(trajectory)
            # print(trajectory.total_time)
    
        
        #print(f"p{p}")
        #print(f"T{T}")
        K = p*10000 - (T*100 + Min)
        return K

    