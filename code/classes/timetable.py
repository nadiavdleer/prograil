class Timetable:
    def __init__(self, trajectories):
        self.trajectories = trajectories
        self.score = 0
        self.traveled_connections = []

    def quality(self, connections):
        used_connections = []
        T = 0
        Min = 0

        for trajectory in self.trajectories:
            T += 1
            Min += trajectory.total_time 
            print(trajectory.itinerary)
            for connection in trajectory.connections:
                used_connections.append(connection)
                

        p = 0
        total_connections = 0
        # print("used_connections")
        # print(used_connections)
        for connection in connections:
            total_connections += 1
            if connection in used_connections:
                p += 1
        p = p / total_connections
        
        print("qualiteit")
        print(f'p{p}')
        print(f"T{T}")

        K = p*10000 - (T*100 + Min)
        return K

    