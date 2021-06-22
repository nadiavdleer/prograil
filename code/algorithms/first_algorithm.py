from code.algorithms.baseline import baseline
from code.classes.timetable import Timetable
import matplotlib.pyplot as plt

class First_algorithm():
    
    def __init__(self, stations, connections, max_time):
        self.stations = stations
        self.connections = connections
        self.max_time = max_time
    
    def hillclimber(self):
        """
         hillclimber like algorithm that adds trajectories to a timetable one by one
         checks after each addition if score rises, only then the trajectory is added
         best found trajectory after 1000 times no better one found is returned
        """
        x_hillclimber = []
        y_hillclimber = []
        loop_number = 0
        best_timetable = None
        no_change_counter = 0
        NO_CHANGE_LIMIT = 10000
        
        while True:
            # create a list of trajectories
            trajectories = baseline(self.connections, self.stations, self.max_time)
            new_timetable = Timetable([])
            
            # set connections to not traveled
            for connection in self.connections:
                connection.traveled = False

            for trajectory in trajectories:
                # check new score with added trajectory
                new_timetable.trajectories.append(trajectory)
                for connection in trajectory.connections:
                    connection.traveled = True
                    
                new_score = new_timetable.quality(self.connections)
            
                if new_score > new_timetable.score:
                    # keep in trajectory in time table and update score
                    new_timetable.score = new_score
                    
                else:
                    # remove trajectory from timetable
                    new_timetable.trajectories.remove(trajectory)
                    for connection in trajectory.connections:
                        connection.traveled = False   
                
            if best_timetable == None or new_timetable.score > best_timetable.score:
                best_timetable = new_timetable
                # graph data
                x_hillclimber.append(loop_number)
                y_hillclimber.append(best_timetable.score)
                no_change_counter = 0
                

            # end while if no change for certain amount of ronds
            if no_change_counter == NO_CHANGE_LIMIT:
                break
            no_change_counter += 1

            # reset conditions
            for connection in self.connections:
                connection.traveled = False

            loop_number += 1

        return best_timetable, x_hillclimber, y_hillclimber
    
    def hillclimber_progress(self, x, y):
        """
         give a plot of the progress of the hillclimber run
        """
        plt.xlabel("Run number")
        plt.ylabel("Best timetable value")
        plt.scatter(x,y)
        plt.show()
        return 0

    def run(self):
        """
         run the algorithm and return the best found timetable 
        """
        best_timetable, x_hillclimber, y_hillclimber = self.hillclimber()
        
        # show progress plot of hillclimber
        self.hillclimber_progress(x_hillclimber, y_hillclimber)
        return best_timetable