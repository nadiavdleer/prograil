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
        all_timetables = []
        depth = max_trajectories

        queue = []
        queue.append(Timetable([])) 

        while len(queue) != 0:
            state = queue.pop(0)
            # print(f"state:{state}")
            new_row = []
        
            for trajectory in trajectories:
                print("begin for loop")
                print(trajectory.itinerary)

                new_timetable = copy.copy(state)
                new_timetable.trajectories = copy.copy(state.trajectories)
                print("state")
                for i in state.trajectories:
                    print(i.itinerary)
                
                new_timetable.trajectories.append(trajectory)
                old_score = new_timetable.score
                print("NORMALE TOEVOEGING")
                new_timetable.score = new_timetable.quality(self.connections)

                # score controleren op nog beter worden
                print(f"old score{old_score}")
                print(f"new score {new_timetable.score}")
                if old_score < new_timetable.score:
                    new_row.append(new_timetable)
                else:
                    new_timetable.trajectories.remove(trajectory)
                    print("SCORE NA ERAF HALEN")
                    new_timetable.score = new_timetable.quality(self.connections)
                    print(f"score: {new_timetable.score}")
                    all_timetables.append(new_timetable)
            print("uit for loop")
            # beam 
            sorted_row = self.sort_score(new_row)
            if len(sorted_row) >= 2:
                for i in range(2):
                    queue.append(sorted_row[i])
                    print(f"BEAM WAARDE!")
                    print(sorted_row[i].score)
            else:
                for i in range(len(sorted_row)):
                    queue.append(sorted_row[i])
                    
            


            # print(f"Queue: {queue}")    

        return all_timetables

    def run(self, max_time, max_trajectories):
        trajectories = self.generate_random_trajectories(max_time)
        # print("generate done")
        trajectories = self.sort_score(trajectories)
        # print("sort done")
        
        all_timetables = self.breadth_beam(max_trajectories, trajectories)

        print("alle eindwaarden")
        for timetable in all_timetables:
            print(timetable.score)

        best_timetable = self.sort_score(all_timetables)[0]
        
        return best_timetable