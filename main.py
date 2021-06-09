from code.classes.connection import Connection
from code.classes.station import Station
from code.classes.trajectory import Trajectory
from code.loaders.loader import load_holland
from baseline import baseline
from code.algorithms.quality import quality
import csv

if __name__ == "__main__":
    stations, connections = load_holland()

    trajectories = baseline(connections, stations)

    score = quality(connections, trajectories)

    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow([f"Trajecten: {len(trajectories)}"])
        writer.writerow([f"Score: {score}"])

    print("   o O___ _________")
    print(" _][__|o| |O O O O|")
    print("<_______|-|_______|")
    print(" /O-O-O     o   o")
    print("----------------------")
    print(f"Aantal trajecten: {len(trajectories)}")
    print("----------------------")
    print(f"Score: {score}")
    print("----------------------")
    print("   o O___ _________")
    print(" _][__|o| |O O O O|")
    print("<_______|-|_______|")
    print(" /O-O-O     o   o")
    print("----------------------")