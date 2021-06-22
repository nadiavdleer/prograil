from code.classes.trajectory import Trajectory
from code.classes.timetable import Timetable
import matplotlib.pyplot as plt
import random
import copy

class Second_algorithm():
    
    def __init__(self, stations, connections): 
        self.stations = stations
        self.connections = connections

    def generate_random_trajectories(self, max_time):
        """
         create trajectories by choosing a random start_station and random trajectories 
         and ensure trajectory total time is not bigger than given max_time
        """
        print("Generating random trajectories...")
        trajectories = []
        used_connections = []
        AMOUNT_TRAJECTORIES = 100

        while True: 
            # random starting station for new trajectory
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
            
            # reset conditions
            for connection in self.connections:
                connection.traveled = False
            
            # break after 100 trajectories
            if len(trajectories) == AMOUNT_TRAJECTORIES:
                break
                
        return trajectories
    
    def sort_score(self, objects):
        """
         sort objects based on score from best to worst  
        """
        objects.sort(key=lambda x: x.score, reverse=True)
        return objects

    def breadth_beam(self, max_trajectories, trajectories): 
        """
         breadth first algorithm that uses a beam to prune and reduce the amount of decision trees
         loop through trajectories, add to a timetable and calculate the quality score, update if higher
         beam to search through critical decision trees only to find best solution
        """
        print("Searching for best combination...")
        all_timetables = []
        queue = []
        x_breadthbeam_progres = []
        y_breadthbeam_progres = []
        depth_counter = 0
        BEAM_WIDTH = 2
        queue.append(Timetable([])) 

        while len(queue) != 0:
            state = queue.pop(0)
            new_row = []
        
            for trajectory in trajectories:
                # create new timetable containing info of ancestor timetable
                new_timetable = copy.copy(state)
                new_timetable.trajectories = copy.copy(state.trajectories)
                
                # add new trajectory to timetable 
                new_timetable.trajectories.append(trajectory)
                old_score = new_timetable.score
                new_timetable.score = new_timetable.quality(self.connections)

                # check if score is better than previous score
                if old_score < new_timetable.score:
                    new_row.append(new_timetable)
                else:
                    # remove last added trajectory and end timetable 
                    new_timetable.trajectories.remove(trajectory)
                    new_timetable.score = new_timetable.quality(self.connections)
                    all_timetables.append(new_timetable)
            
            # beam selection best scores
            sorted_row = self.sort_score(new_row)
            if len(sorted_row) >= BEAM_WIDTH:
                for i in range(BEAM_WIDTH):
                    queue.append(sorted_row[i])

                    # add data to visualisation list
                    x_breadthbeam_progres.append(depth_counter)
                    y_breadthbeam_progres.append(sorted_row[i].score)
            else:
                for i in range(len(sorted_row)):
                    queue.append(sorted_row[i])

                    # add data to visualisation list
                    x_breadthbeam_progres.append(depth_counter)
                    y_breadthbeam_progres(sorted_row[i].score)

            depth_counter += 1
                    
        return all_timetables, x_breadthbeam_progres, y_breadthbeam_progres

    def breadthbeam_progress(self, x, y):
        """
         show scatterplot of all data seleced by the beam as a funtion of the tree depth
        """
        plt.xlabel("Depth in tree")
        plt.ylabel("Best scores by beam")
        plt.scatter(x,y)
        plt.show()
        return 0

    def run(self, max_time, max_trajectories):
        """
         create a number of randomly genorated trajectories
         find best combination by calling on breadth first with beam algorithm
        """
        trajectories = self.generate_random_trajectories(max_time)
        all_timetables, x, y = self.breadth_beam(max_trajectories, trajectories)
        
        # show progress plot
        self.breadthbeam_progress(x,y)

        # find best timetable
        best_timetable = self.sort_score(all_timetables)[0]
        return best_timetable