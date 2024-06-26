#!/usr/local/bin/python3
# solve_fairies.py : Fairy puzzle solver
#
# Code by: Manikanta Kodandapani Naidu(k11), Vedika Sudhir Shinde(vsshinde)
#
# Based on skeleton code by B551 course staff, Fall 2023
#
# N fairies stand in a row on a wire, each adorned with a magical symbol from 1 to N.
# In a single step, two adjacent fairies can swap places. How can
# they rearrange themselves to be in order from 1 to N in the fewest
# possible steps?

# !/usr/bin/env python3
import sys
import heapq

N=5

#####
# THE ABSTRACTION:
#
# Initial state:

# Goal state:
# given a state, returns True or False to indicate if it is the goal state
def is_goal(state):
    return state == list(range(1, N+1))

# Successor function:
# given a state, return a list of successor states
def successors(state):
    return [ state[0:n] + [state[n+1],] + [state[n],] + state[n+2:] for n in range(0, N-1) ]

# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state
def h(state):
    return abs(state.index(1)-0) + abs(state.index(2)-1) + abs(state.index(3)-2) + abs(state.index(4)-3) + abs(state.index(5)-4)

#########
#
# THE ALGORITHM:
#
# This is a generic solver using BFS. 
#
def solve(initial_state):
    fringe = []
    reached = {"{}".format(initial_state):h(initial_state)}

    fringe += [(initial_state, [], 0),]
    while len(fringe) > 0:
        (state, path, cost) = heapq.heappop(fringe)
        
        if is_goal(state):
            return path+[state,], cost

        for s in successors(state):
            if "{}".format(s) not in reached.keys() or ((cost + h(s)) < reached["{}".format(s)]):
                reached["{}".format(s)] = cost + h(s)
                heapq.heappush(fringe, (s, path+[state,], cost+1))
                 
    return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a test case filename"))

    test_cases = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            test_cases.append([ int(i) for i in line.split() ])
    for initial_state in test_cases:
        	print('From state ' + str(initial_state) + " found goal state by taking path: " + str(solve(initial_state)))

