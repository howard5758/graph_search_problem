# Author: Ping-Jung Liu
# Date: September 17th 2017
# COSC 76 Assignment 1: Missionaries and Cannibals
# Acknowledgement: Professor Devin Balkom for providing the general structure 

from Lossy_CannibalProblem import Lossy_CannibalProblem
from uninformed_search import bfs_search, dfs_search, ids_search

# Create a few test problems:
# the forth element of states indicates the number of eaten missionaries
# which should definitely be 0 at the start_state

# the second parameter indicates the number of missionaries allowed to be eaten
# if set to 0, the results should be the same as the original problems
problem331 = Lossy_CannibalProblem((3, 3, 1, 0), 2)
problem541 = Lossy_CannibalProblem((5, 4, 1, 0), 2)
problem551 = Lossy_CannibalProblem((5, 5, 1, 0), 2)

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
