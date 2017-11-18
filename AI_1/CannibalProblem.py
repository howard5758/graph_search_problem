# Author: Ping-Jung Liu
# Date: September 17th 2017
# COSC 76 Assignment 1: Missionaries and Cannibals
# Acknowledgement: Professor Devin Balkom for providing the general structure 

class CannibalProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        # keep track of total number of missionaries and cannibals
        self.totalM = start_state[0]
        self.totalC = start_state[1]
        # capacity of boat
        self.boat = 2
        # you might want to add other things to the problem,
        #  like the total number of missionaries (which you can figure out
        #  based on start_state

    # get successor states for the given state
    def get_successors(self, state):
        # current numbers of missionaries and cannibals on the start side
        Mnum = state[0]
        Cnum = state[1]
        boat = self.boat
        # will be the list of legal successors
        stateList = []
        # loop through the possible actions
        for m in range(0, boat + 1):
            for c in range(0, boat - m + 1):
                
                # if boat at start side, move it to the end then subtract Mnum and Cnum
                if state[2] == 1 :
                    if m + c != 0:
                        Mnum = state[0] - m
                        Cnum = state[1] - c
                        if legalsafe((Mnum, Cnum, 0), self.totalM, self.totalC):
                            stateList.append((Mnum, Cnum, 0))

                    # else move it back to the start then add Mnum and Cnum
                else :
                    if m + c != 0:
                        Mnum = state[0] + m
                        Cnum = state[1] + c
                        if legalsafe((Mnum, Cnum, 1), self.totalM, self.totalC):
                            stateList.append((Mnum, Cnum, 1))
        return stateList
        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list

    # I also had a goal test method. You should write one.
    def goal_test(self, state):
        return state[0] == 0 and state[1] == 0 and state[2] == 0

    def __str__(self):
        string =  "Missionaries and cannibals problem: " + str(self.start_state)
        return string

# given state, total number of missionaries, total number of cannibals
# output whether the state is valid or not

# check whether a state is legal and safe
def legalsafe(state, totalM, totalC):
    if state[0] < 0 or state[1] < 0:
        result = False

    elif state[0] > totalM or state[1] > totalC:
        result = False

    # check whether missionaries at start side are safe
    elif state[0] > 0 and state[0] < state[1]:
        result = False

    # check whether missionaries at end side are safe
    elif state[0] < totalM and (totalM - state[0]) < (totalC - state[1]):
        result = False

    else:
        result = True

    return result



## A bit of test code

if __name__ == "__main__":
    test_cp = CannibalProblem((3, 3, 1))
    print(test_cp.get_successors((3, 3, 1)))
    print(test_cp)
