from code.algorithms.baseline import baseline
from code.classes.timetable import Timetable

def first_algorithm(connections, stations, max_time):
    graph_moments = []
    loop_number = 0
    best_timetable = None
    no_change = 0
 
    while True:
        trajectories = baseline(connections, stations, max_time)
        new_timetable = Timetable([])
        
        # set connections to not traveled
        for connection in connections:
            connection.traveled = False

        for trajectory in trajectories:
            # check new score with added trajectory
            new_timetable.trajectories.append(trajectory)
            for connection in trajectory.connections:
                connection.traveled = True
                
            new_score = new_timetable.quality(connections)
           
            if new_score > new_timetable.score:
                # keep in trajectory in time table and update score
                new_timetable.score = new_score
                
            else:
                # remove trajectory from timetable
                new_timetable.trajectories.remove(trajectory)
                for connection in trajectory.connections:
                    connection.traveled = False   
            
        #print(new_timetable.score)
        if best_timetable == None or new_timetable.score > best_timetable.score:
            best_timetable = new_timetable
            graph_moments.append(loop_number)
            no_change = 0
            # graph data

            # print("NEW BEST SCORE")

        # end while if no change for certain amount of ronds
        if no_change == 10000:
            break
        no_change += 1

        #reset conditions
        for connection in connections:
            connection.traveled = False

        loop_number += 1

    return best_timetable, graph_moments