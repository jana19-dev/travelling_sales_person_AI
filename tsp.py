from search import *
from random import randint
from copy import deepcopy
import math


'''
a Node Class to represent a city
'''

class Node():
    def __init__(self, name, position, is_start=False):
        self.name = name
        self.position = position    # position = (x, y) coordinates 
        self.is_start = is_start
        self.is_visited = False
        
    
########################################################
#   Additional functions to work with Nodes     #
########################################################


def dist_Euclidean(node1, node2):
    '''Compute the Euclidean distance between two nodes.'''

    # The two points are located on coordinates (x1,y1) and (x2,y2)
    (x1,y1) = node1.position
    (x2,y2) = node2.position
    
    xdiff = x2 - x1
    ydiff = y2 - y1
    
    return int(math.sqrt(xdiff*xdiff + ydiff*ydiff))


def dist_Manhattan(node1, node2):
    '''Compute the Manhattan distance between two nodes.'''

    # The two points are located on coordinates (x1,y1) and (x2,y2)
    (x1,y1) = node1.position
    (x2,y2) = node2.position
    
    return int(abs(x2-x1) + abs(y2-y1))




'''
tsp STATESPACE
'''

##################################################
# The search space class 'tsp'             #
# This class is a sub-class of 'StateSpace'      #
##################################################


class tsp(StateSpace):
    def __init__(self, cities, action, gval, parent=None):
        """Initialize a tsp search state object."""
        StateSpace.__init__(self, action, gval, parent)
        self.cities = cities    # cities = [node1, node2, ... nodek]
        

    def successors(self):
        '''Return list of tsp objects that are the successors of the current object'''
        pass
        
        
    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
        pass


    def print_state(self):
        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))
            
        print ('')
        
        for city in self.cities:
            print ('Name={}\tPosition={}\tVisited={}\tStart={}'.format(city.name, city.position, city.is_visited, city.is_start))        



def tsp_goal_fn(state):
    '''Have we reached a goal state'''
    pass


def make_init_state(cities, start_city):
    '''Input the following items which specify a state and return a tsp object
       representing this initial state.
       Input : cities = [(name, x, y), (name, x ,y) ... ]
               where name is the city's name and x,y are its coordinates
    '''
    i = 1
    all_cities = []
    for city in cities:
        name = city[0]
        x = city[1]
        y = city[2]
        
        new_city = Node(name, (x, y))
        
        # append the start city at the front of the list
        if i == start_city:
            new_city.is_start = True
            all_cities.insert(0,new_city)
        else:
            all_cities.append(new_city)
        
        i += 1
    
    return tsp(all_cities, "START", 0)


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


def make_rand_init_state(n, x_max, y_max):
    '''Generate a random initial state containing 'n' number of cities, all 
       within the range from (0,0) to (x_max, y_max) coordinates.
       start = the number of the city in the range which we start the TSP'''
    
    cities_list = []
    coordinates_taken = []
    
    for i in range(n):
        name = 'City{}'.format(i+1)
        conflict = True
        
        while conflict:  
            x = randint(0, x_max - 1)
            y = randint(0, y_max - 1)
            conflict = False
            if (x,y) in coordinates_taken:
                conflict = True
                
        coordinates_taken.append((x,y))
        new_city = (name, x, y)
        cities_list.append(new_city)
    
    start_city = randint(1, n)
    
    return make_init_state(cities_list, start_city)
