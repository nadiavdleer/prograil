from code.loaders.loader import load_holland, load_nationaal
from code.algorithms.first_algorithm import first_algorithm
from code.algorithms.second_algorithm import Second_algorithm
from code.visualisation.map import map
import matplotlib.pyplot as plt
import csv
from sys import argv

if __name__ == "__main__":

    # check command line arguments
    if len(argv) is not 2:
        print("Usage: python3 main.py 2nd argument required: 'holland' or 'nationaal'")
        exit(1)
    else:
        print("Loading...")
        # load the requested files
        if argv[1] == "holland":
            stations, connections = load_holland()
            max_time = 120
            max_trajectories = 7
            size = "Holland"

        if argv[1] == "nationaal":
            stations, connections = load_nationaal()
            max_time = 180
            max_trajectories = 20
            size = "Nationaal"

    # make timetable and score
    # timetable, graph_moments = first_algorithm(connections, stations, max_time)
    # score = timetable.score

    # plt.hist(graph_moments)
    # plt.xlabel("Run numer")
    # plt.ylabel("Frequency")
    # plt.plot()

    # for trajectory in timetable.trajectories:
    #     print(trajectory.itinerary)

    # for connectie in connections:
    #     print(connectie)
    #     print(connectie.traveled)

    second_algorithm = Second_algorithm(stations, connections)
    best_timetable = second_algorithm.run(max_time, max_trajectories)
    print(best_timetable)
    print(best_timetable.score)
    print(len(best_timetable.trajectories))

    for trajectory in best_timetable.trajectories:
        print(trajectory.itinerary)

    # make map
    map(stations, connections, best_timetable.trajectories, size)

    # header = ["train", "stations"]
    # number = 1
    # with open('output.csv', 'w') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(header)
    #     for trajectory in timetable.trajectories:
    #         writer.writerow([f"train_{number}", trajectory.itinerary])
    #         number += 1
    #     writer.writerow(["score", score])

    # print("   o O___ _________")
    # print(" _][__|o| |O O O O|")
    # print("<_______|-|_______|")
    # print(" /O-O-O     o   o")
    # print("----------------------")
    # print(f"Aantal trajecten: { len(timetable.trajectories) }") 
    # print("----------------------")
    # print(f"Score: {score}")
    # print("----------------------")
    # print("   o O___ _________")
    # print(" _][__|o| |O O O O|")
    # print("<_______|-|_______|")
    # print(" /O-O-O     o   o")
    # print("----------------------")