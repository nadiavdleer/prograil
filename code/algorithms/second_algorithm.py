from hashlib import new
from code.classes.trajectory import Trajectory
from code.classes.connection import Connection
from code.classes.station import Station
from code.classes.timetable import Timetable
import random
import copy
from multiprocessing import Queue

class Second_algorithm():
    
    def __init__(self, stations, connections): 
        self.stations = stations
        self.connections = connections
        

    def generate_random_trajectories(self, max_time):
        trajectories = []
        used_connections = []

        while True: 
            start_station = random.choice(list(self.stations.values()))
            trajectory = Trajectory(start_station)

            # add connections
            while True:
                new_connection = None
                for connection in trajectory.end.connections:
                    if not connection.traveled:
                        if new_connection == None or connection.time < new_connection.time:
                            new_connection = connection
                
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
        
    
    def sort_trajectories(self, trajectories):
        trajectories.sort(key=lambda x: x.score, reverse=True)
        return trajectories

    def breadth_beam(self, max_trajectories, trajectories): 
        all_timetables = []
        depth = max_trajectories

        queue = []
        queue.append(Timetable([]))

        while len(queue) != 0:
            state = queue.pop(0)
            print(f"state:{state}")
            if len(state.trajectories) < depth:
                for trajectory in trajectories:
                    new_timetable = copy.deepcopy(state)
                    new_timetable.trajectories.append(trajectory)
                    queue.append(new_timetable)
                    # groot probeem met traveled boolian --> kijken of we met trajectory connections lijst kunnen werken
                    new_timetable.score = new_timetable.quality(self.connections)
                # beam maken
                # score controleren op nog beter worden

            print(f"Queue: {queue}")    

        return all_timetables

    def run(self, max_time, max_trajectories):
        trajectories = self.generate_random_trajectories(max_time)
        print("generate done")
        trajectories = self.sort_trajectories(trajectories)
        print("sort done")
        
        all_timetables = self.breadth_beam(max_trajectories, trajectories)

        best_timetable = None

        return best_timetable