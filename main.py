from code.classes.connection import Connection
from code.classes.station import Station
from code.classes.trajectory import Trajectory
from code.classes.timetable import Timetable
from code.loaders.loader import load_holland
from code.algorithms.baseline import baseline
from code.algorithms.first_algorithm import first_algorithm
import csv

if __name__ == "__main__":
    stations, connections = load_holland()

    #trajectories = baseline(connections, stations)
    
    #new_timetable = Timetable(trajectories)
    #score = new_timetable.quality(connections)

    timetable = first_algorithm(connections, stations)
    score = timetable.score

    # for trajectory in trajectories:
    #     for connection in trajectory.connections:
    #         print(connection)

    header = ["train", "stations"]
    number = 1
    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for trajectory in timetable.trajectories:
            writer.writerow([f"train_{number}", trajectory.itinerary])
            number += 1
        writer.writerow(["score", score])

    print("   o O___ _________")
    print(" _][__|o| |O O O O|")
    print("<_______|-|_______|")
    print(" /O-O-O     o   o")
    print("----------------------")
    print(f"Aantal trajecten: { len(timetable.trajectories) }") 
    print("----------------------")
    print(f"Score: {score}")
    print("----------------------")
    print("   o O___ _________")
    print(" _][__|o| |O O O O|")
    print("<_______|-|_______|")
    print(" /O-O-O     o   o")
    print("----------------------")

    for trajectory in timetable.trajectories:
        print(trajectory.itinerary)