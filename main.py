from code.loaders.loader import load_holland, load_nationaal
from code.algorithms.first_algorithm import first_algorithm
from code.algorithms.second_algorithm import Second_algorithm
from code.visualisation.map import map
import matplotlib.pyplot as plt
import csv
from sys import argv

if __name__ == "__main__":

    # ask user to choose data file 
    print("For North- and South-Holland, type 'holland'")
    print("For the entire Netherlands, type 'nationaal'")
    data_file = input("Choice: ")
    
    # load either holland or national file
    if data_file == "holland" or data_file == "Holland" or data_file == "H":
        stations, connections = load_holland()
        max_time = 120
        max_trajectories = 7
        size = "Holland"    
    elif data_file == "nationaal" or data_file == "Nationaal" or data_file == "N":
        stations, connections = load_nationaal()
        max_time = 180
        max_trajectories = 20
        size = "Nationaal"
    else:
        print("Please select 'Holland' or 'Nationaal'")
        exit(1)

    # ask user to choose algorithm
    print("Which algorithm would you like to run? For Hill Climber type '1', for Breadth First type '2'")
    algorithm = input("Choice: ")
    
    if algorithm == "1":
        print("Loading...")
        # run hill climber algorithm
        best_timetable, graph_moments = first_algorithm(connections, stations, max_time)
        
        # give plot of change in best algorithm
        plt.hist(graph_moments)
        plt.xlabel("Run numer")
        plt.ylabel("Frequency")
        plt.plot()
    elif algorithm == "2":
        print("Loading...")
        # run constructive algorithm
        second_algorithm = Second_algorithm(stations, connections)
        best_timetable = second_algorithm.run(max_time, max_trajectories)
    else:
        print("Please select an algorithm to run")
        exit(1)
        
    # make output csv file
    header = ["train", "stations"]
    number = 1
    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for trajectory in best_timetable.trajectories:
            writer.writerow([f"train_{number}", "["+', '.join(trajectory.itinerary)+"]"])
            number += 1
        writer.writerow(["score", best_timetable.score])

    # give terminal output
    print("   o O___ _________")
    print(" _][__|o| |O O O O|")
    print("<_______|-|_______|")
    print(" /O-O-O     o   o")
    print("----------------------")
    print(f"Amount of trajectories: { len(best_timetable.trajectories) }") 
    print("----------------------")
    print(f"Score: {best_timetable.score}")
    print("----------------------")
    print("   o O___ _________")
    print(" _][__|o| |O O O O|")
    print("<_______|-|_______|")
    print(" /O-O-O     o   o")
    print("----------------------")
    print("Loading map...")
    
    # make map
    map(stations, connections, best_timetable.trajectories, size)