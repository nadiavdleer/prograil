from code.classes.trajectory import Trajectory
from code.classes.timetable import Timetable
import random
import copy
from multiprocessing import Queue

class Second_algorithm():
    
    def __init__(self, stations, connections): 
        self.stations = stations
        self.connections = connections

    def generate_random_trajectories(self, max_time):
        print("Generating random trajectories...")
        trajectories = []
        used_connections = []

        while True: 
            start_station = random.choice(list(self.stations.values()))
            trajectory = Trajectory(start_station)

            # add connections
            while True:
                new_connection = random.choice(trajectory.end.connections)
                
                # end trajectory if no possible route
                if new_connection == None:
                    if trajectory.total_time == 0:
                        break
                    trajectories.append(trajectory)
                    trajectory.score = trajectory.quality(self.connections)
                    break

                # add new connection to trajectory and set traveled
                trajectory.add_connection(new_connection)
                new_connection.set_traveled()
                used_connections.append(new_connection)
                
                # ensure max_time trajectory
                if trajectory.total_time > max_time:
                    trajectory.remove_connection(new_connection)
                    new_connection.traveled = False
                    used_connections.remove(new_connection)
                    trajectories.append(trajectory)
                    trajectory.score = trajectory.quality(self.connections)
                    break
            
            for connection in self.connections:
                connection.traveled = False
            
            if len(trajectories) == 100:
                break
                
        return trajectories
    
    def sort_score(self, objects):
        objects.sort(key=lambda x: x.score, reverse=True)
        return objects

    def breadth_beam(self, max_trajectories, trajectories): 
        print("searching for best combination...")
        all_timetables = []
        queue = []
        queue.append(Timetable([])) 

        while len(queue) != 0:
            state = queue.pop(0)
            new_row = []
        
            for trajectory in trajectories:
                new_timetable = copy.copy(state)
                new_timetable.trajectories = copy.copy(state.trajectories)
                
                new_timetable.trajectories.append(trajectory)
                old_score = new_timetable.score
                new_timetable.score = new_timetable.quality(self.connections)

                # check if score is better than previous score
                if old_score < new_timetable.score:
                    new_row.append(new_timetable)
                else:
                    new_timetable.trajectories.remove(trajectory)
                    new_timetable.score = new_timetable.quality(self.connections)
                    all_timetables.append(new_timetable)
            # beam search
            sorted_row = self.sort_score(new_row)
            if len(sorted_row) >= 2:
                for i in range(2):
                    queue.append(sorted_row[i])
            else:
                for i in range(len(sorted_row)):
                    queue.append(sorted_row[i])
                    
        return all_timetables

    def run(self, max_time, max_trajectories):
        trajectories = self.generate_random_trajectories(max_time)
        all_timetables = self.breadth_beam(max_trajectories, trajectories)
        best_timetable = self.sort_score(all_timetables)[0]
        
        return best_timetable