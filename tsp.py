
'''
tsp STATESPACE
'''


from search import *
from random import randint
from copy import deepcopy

##################################################
# The search space class 'tsp'             #
# This class is a sub-class of 'StateSpace'      #
##################################################


class tsp(StateSpace):
    def __init__(self, action, gval, parent=None):
        """Initialize a tsp search state object."""
        StateSpace.__init__(self, action, gval, parent)
        pass


    def successors(self):
        '''Return list of tsp objects that are the successors of the current object'''
        pass
        
        
    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
        pass


    def print_state(self):

        pass



def tsp_goal_fn(state):
    '''Have we reached a goal state'''
    pass


def make_init_state():
    '''Input the following items which specify a state and return a tsp object
       representing this initial state.
    '''
    pass


#############################################
# heuristics                                #
#############################################


def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0


def heur_distance_to_nearest_neighbour(state):
	pass


def heur_MST(state):
	pass


def heur_nearest_distance_from_an_unvisited_city_to_the_start_city(state):
	pass	


########################################################
#   Functions provided so that you can more easily     #
#   Test your implementation                           #
########################################################


def get_tsp_status():
	pass


def make_rand_init_state():
    '''Generate a random initial state containing'''
    pass
