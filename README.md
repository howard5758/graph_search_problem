# Author: Ping-Jung Liu
# Date: September 17th 2017
# Acknowledgement: Professor Devin Balkom for providing the general structure 

***README***

Files in this directory:

- Missionaries_and_Cannibals.pdf

- cannibals.py

- CannibalProblem.py

- Lossy_cannibals.py

- Lossy_CannibalProblem.py

- Boat_cannibals.py

- Boat_CannibalProblem.py

- uninformed_search.py

- SearchSolution.py

****************************
To run the original problem:
****************************
- Run cannibals.py, the program will output the results of (3, 3, 1) (5, 5, 1) (5, 4, 1) using all BFS, DFS, and IDS

- To manually create a new problem, use command in cannibals.py: 
  problem_name = CannibalProblem(TotalM, TotalC, 1)
  print(searchalgorithm_search(problem_name))

- The program will solve the problem and print out the results.
*************************
To run the lossy version:
*************************
- Run Lossy_cannibals.py, the program will output the results of (3, 3, 1, 0) (5, 5, 1, 0) (5, 4, 1, 0) 
  using all BFS, DFS, and IDS with 2 as the number of missionaries allowed to be eaten.

- To manually create a new problem, use command in Lossy_cannibals.py:
  problem_name = Lossy_CannibalProblem((TotalM, TotalC, 1, 0), Eaten_Allowed)
  print(searchalgorithm_search(problem_name))

- The program will solve the problem and print out the results.
*********************************
To run the boat variable version:
*********************************
- Run Boat_cannibals.py, the program will output the results of (3, 3, 1) (5, 5, 1) (5, 4, 1) 
  using all BFS, DFS, and IDS with 3 as the size of boat.

- TO manually create a new problem, use command Boat_cannibals.py:
  problem_name = Boat_CannibalProblem((TotalM, TotalC, 1), Boat_Size)
  print(searchalgorithm_search(problem_name))

- The program will solve the problem and print out the results
