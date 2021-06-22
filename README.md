# ProgRail
The function of this README.md is to introduce the RailNL-case and to provide an explanation on the chosen approach and how to execute the algorithms given in this repository.

## Getting Started
### Assignment
This project concludes the Heuristics course ("*Programmeertheorie*") of the minor "*Programmeren*" at the University of Amsterdam. 
The goal of this course was to solve complex cases with the help of algorithms. Our team has chosen the RailNL case, specifically the assignment to optimize the quality of trajectories for InterCity trains. In order to do so, the case came with a few criteria that had to be incorporated into our solution. For instance, trajectories are not supposed to exceed a certain amount of time, and there is a constraint on the amount of trajectories that may be generated. With the help of a given target function (**K = p * 10000 - (T * 100 + Min)**), it is possible to calculate the quality *K* of the trajectories system. In said function, *p* represents the fraction of traveled connections (value between 0-1), *T* the amount of trajectories, and *Min* the total time of trajectories in minutes.

### Our approach
We wrote two different algorithms. The first algorithm is a hillclimber like algorithm that adds trajectories to a timetable one by one. The algorithm starts off with our baseline funtion. This funtion generates a random start station, and then performs like a greedy algorithm in selecting the next station to connect to and expand the trajectory. The trajectories are then used to build a timetable, by adding the trajectories one by one and checking the score. Trajectories are only added when this addition makes the overall timetable score higher -- this is the hillclimbing component. The new timetable is compared to the best scoring timetable, and the former replaces the latter if its score is higher. If no better scoring timetable is found after 10000 runs, the algorithm is cut off. 

The second algorithm is a breadth first algorithm that uses a beam to prune and reduce the amount of decision trees. Firstly, trajectories are generated quite like in the first algorithm. The only difference is in the length of these trajectories. In the first algorithm the trajecotries are generated to cover all connections, whereas in this algorithm the trajectories are generated to be as long as possible. Other than that, the trajectories are generated the same way - with a random start station and a greedy algorithm in order to choose the connections. When the trajectories are generated, a full timetable is made using combinations of these trajectories. A breath first algorithm makes a selection within each "row", based on the score the timetable has so far. Timetables are cut off when the addition of a new trajectory no longer increases the timetable score. In the end, all the scores of timetables that were cut off are compared. The timetable with the highest score constitutes the best timetable found.

Both of the algorithms are provided with a progress function. The purpose of these functions is to visualize how the algorithm improves the score over multiple rounds. The progress function of the first algorithm consists of a line plot that shows the value of the updated score, as well as the corresponding loop number. The second algorithm's progress function is a scatter plot containing all the scores that the beam selects after every row as a function of the row number. For this progress function, a scatterplot was chosen, since the beam picks more than one value per row.

### Prerequisites
To execute code and generate map, installation of *matplotlib* and *cartopy* is required. See **requirements.txt** for installation steps.

### Testing
To run the code:

    python3 main.py 

After running this command, the user will be prompted with several questions to decide which data file and which algorithm he/she wants to use. 