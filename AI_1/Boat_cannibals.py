# Author: Ping-Jung Liu
# Date: September 17th 2017
# COSC 76 Assignment 1: Missionaries and Cannibals
# Acknowledgement: Professor Devin Balkom for providing the general structure 

from Boat_CannibalProblem import Boat_CannibalProblem
from uninformed_search import bfs_search, dfs_search, ids_search

# Create a few test problems:
# the second parameter indicates the size of boat
# a boat cannot carry more cannibals than missionaries
problem331 = Boat_CannibalProblem((3, 3, 1,), 3)
problem541 = Boat_CannibalProblem((5, 4, 1), 3)
problem551 = Boat_CannibalProblem((5, 5, 1), 3)

# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.

print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))

print(bfs_search(problem551))
print(dfs_search(problem551))
print(ids_search(problem551))

print(bfs_search(problem541))
print(dfs_search(problem541))
print(ids_search(problem541))

#print(dfs_search(problemtest)) 