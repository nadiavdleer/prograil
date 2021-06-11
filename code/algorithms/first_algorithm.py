from code.algorithms.baseline import baseline
from code.classes.timetable import Timetable


def first_algorithm(connections, stations):
    best_timetable = None
    
    for connection in connections:
        connection.traveled = False
 
    for i in range(1000):
        print("voor baseline")
        trajectories = baseline(connections, stations)
        print(f"in ronde {i}")
        if len(trajectories) < 7:
            print("Lengte minder dan 7")
            new_timetable = Timetable([])

            for connection in connections:
                connection.traveled = False

            for trajectory in trajectories:
                # check new score with added trajectory
                new_timetable.trajectories.append(trajectory)
                for connection in trajectory.connections:
                    connection.traveled = True
                
                new_score = new_timetable.quality(connections)
                print("in tra loop")

                # keep in trajectory in time table and update score
                print(f"new_score:{new_score}")
                print(f"score in timetable: {new_timetable.score}")
                if new_score > new_timetable.score:
                    new_timetable.score = new_score
                    print("in if")
                else:
                    # remove trajectory from timetable
                    new_timetable.trajectories.remove(trajectory)
                    for connection in trajectory.connections:
                        connection.traveled = False
                    print("in else")

            if best_timetable == None or new_timetable.score > best_timetable.score:
                best_timetable = new_timetable

        print(f"einde loop {i}")
        for connection in connections:
                connection.traveled = False

    print(best_timetable)
    return best_timetable