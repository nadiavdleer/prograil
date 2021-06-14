from code.loaders.loader import load_holland, load_nationaal
from code.algorithms.first_algorithm import first_algorithm
from code.visualisation.map import map
import csv

if __name__ == "__main__":
    # stations, connections = load_holland()
    # max_time = 120
    # max_trajectories = 7
    # timetable = first_algorithm(connections, stations, max_time, max_trajectories)
    # score = timetable.score

    stations, connections = load_nationaal()
    max_time = 180
    max_trajectories = 20
    timetable = first_algorithm(connections, stations, max_time, max_trajectories)
    for trajectory in timetable.trajectories:
        print(trajectory.itinerary)


    score = timetable.score

    # make map
    size = "Nationaal"
    map(stations, connections, timetable.trajectories, size)

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