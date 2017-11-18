
# Author: Ping-Jung Liu
# Date: September 17th 2017
# COSC 76 Assignment 1: Missionaries and Cannibals
# Acknowledgement: Professor Devin Balkom for providing the general structure 

class Lossy_CannibalProblem:
    def __init__(self, start_state=(3, 3, 1, 0), eat=0):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        # keep track of total number of missionaries and cannibals
        self.totalM = start_state[0]
        self.totalC = start_state[1]

        # capacity of boat
        self.boat = 2

        # number of missionaries allowed to be eaten
        self.eat = eat
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
                        # obtain new_state and new_totalM ( because some might get eaten o: )
                        # if a state is neither safe nor legal, the function will set new_state[3] to -1 for identification
                        (new_state, new_totalM) = legalsafe((Mnum, Cnum, 0, state[3]), self.totalM, self.totalC, self.eat)

                        # if the eaten missionaries exceed the number allowed to be eaten, count as illegal
                        if (not new_state[3] == -1) and (new_state[3] <= self.eat):
                            stateList.append(new_state)

                # else move it back to the start then add Mnum and Cnum
                else :
                    if m + c != 0:
                        Mnum = state[0] + m
                        Cnum = state[1] + c
                        # obtain new_state and new_totalM ( because some might get eaten o: )
                        # if a state is neither safe nor legal, the function will set new_state[3] to -1 for identification
                        (new_state, new_totalM) = legalsafe((Mnum, Cnum, 1, state[3]), self.totalM, self.totalC, self.eat)
                        if (not new_state[3] == -1) and (new_state[3] <= self.eat):
                            stateList.append(new_state)

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
def legalsafe(state, totalM, totalC, eat):
    if state[0] < 0 or state[1] < 0:
        result = ((state[0], state[1], state[2], -1), totalM)

    elif state[0] > totalM or state[1] > totalC:
        result = ((state[0], state[1], state[2], -1), totalM)

    # let them get eaten, then modify total number of missionaries, how sad
    elif state[0] > 0 and state[0] < state[1]:
        result = ((0, state[1], state[2], state[3] + state[0]), totalM - state[0]) 

    elif state[0] < totalM and (totalM - state[0]) < (totalC - state[1]):
        result = ((state[0], state[1], state[2], eat + (totalM - state[0])), state[0])

    else:
        result = (state, totalM)

    return result



## A bit of test code

if __name__ == "__main__":
    test_cp = Lossy_CannibalProblem((3, 3, 1, 0), 1)
    print(test_cp.get_successors((3, 3, 1, 0)))
    print(test_cp)
