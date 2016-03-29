from search import *
from random import randint
from copy import deepcopy
import math
import turtle
import itertools


'''
a Node Class to represent a city
'''

class Node():
    def __init__(self, name, position):
        self.name = name
        self.position = position    # position = (x, y) coordinates 
        self.is_start = False
        self.is_visited = False
        
    def get_city_details(self):
        ''' Return a tuple representing the city with all its properties'''
        return (self.name, self.position, self.is_start, self.is_visited)
    
    
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
    
    
    def __init__(self, current_city, cities, action, gval, parent=None):
        """Initialize a tsp search state object."""
        StateSpace.__init__(self, action, gval, parent)
        self.cities = cities    # cities = [node1, node2, ... nodek]
        self.current_city = current_city
        

    def successors(self):
        '''Return list of tsp objects that are the successors of the current object'''
        States = []
        current_city = self.current_city
        for city in self.cities:
            if current_city != city and not city.is_visited:
                new_gval = self.gval + dist_Euclidean(current_city, city)
                new_cities = deepcopy(self.cities)
                current_index = self.cities.index(city)
                new_cities[current_index].is_visited = True
                States.append(tsp(new_cities[current_index], new_cities, 'Move to {}'.format(city.name), new_gval, self))
            
        return States        
        
        
    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
        hash_list = []
        for city in self.cities:
            hash_list.append(city.get_city_details())
            
        hash_list.insert(0, (self.current_city).get_city_details())
        
        return tuple(sorted(hash_list))
        

    def print_state(self):
        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))
                   
        for city in self.cities:
            print ('Name={}\tPosition={}\tVisited={}\tStart={}\tCurrent={}'.format(city.name, city.position, city.is_visited, city.is_start,city == self.current_city))        

        print ('')


    
#############################################
# Goal Function and Initialization          #
#############################################


def tsp_goal_fn(state):
    '''Have we reached a goal state. Make sure its atleast close to optimal
       by comparing the cost with the upper bound cost.'''
    
    for city in state.cities:
        if city.is_start and not (city == state.current_city):
            return False
        if not city.is_visited:
            return False
    return True


def make_init_state(cities, start_city=1):
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
    
    current_city = all_cities[0]  # set the current city as the start_city
    
    return tsp(current_city, all_cities, "START", 0)
    


#############################################
# heuristics                                #
#############################################

def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0


def heur_Euclidean(state, DW=False):
    '''The euclidean distance to the nearest unvisited neighbour from the 
        current city + The minimum euclidean distance from an unvisited 
        city (not the current city) to the start city.
        If DW=True, multiply the result by dynamic_weight(state).'''
    return 0


def heur_Manhattan(state, DW=False):
    '''The manhattan distance to the nearest unvisited neighbour from the 
       current city + The minimum manhattan distance from an unvisited 
       city (not the current city) to the start city.
       If DW=True, multiply the result by dynamic_weight(state).'''
    return 0


def heur_MST_Euclidean(state, DW=False):
    '''Estimated Euclidean distance to travel all the unvisited nodes
       starting from the current city + heur_Euclidean.
       If DW=True, multiply the result by dynamic_weight(state).'''
    return 0


def heur_MST_Manhattan(state, DW=False):
    '''Estimated Manhattan distance to travel all the unvisited nodes 
       starting from the current city + heur_Manhattan.
       If DW=True, multiply the result by dynamic_weight(state).'''
    return 0


#############################################
# Helper functions for heuristics           #
#############################################

def MST(state):
    ''' Kruskal's algorithm.
        1. mst_distance (the final spanning tree cost) is defined to be the 0
        2. Sort the edges of G in ascending (non-decreasing) order
        3. For each edge (u, v) from the sorted list of step 3.
           If u and v belong to different sets
               Add the cost of the edge to mst_distance
               Get together u and v in one single set
        4. Return mst_distance
    '''
    mst_distance = 0
    
    current_city = state.current_city
    unvisited_cities = [city for city in state.cities if not city.is_visited]
    city_pairs = itertools.combinations(unvisited_cities, 2)
    
    edges = []
    for x,y in city_pairs:
        edges.append((dist_Euclidean(x, y), (x,y)))
    edges = sorted(edges, key=lambda x: x[0])
    
    nodes_visited = []
    for e in edges:
        if not ((e[1][0] in nodes_visited) and (e[1][1] in nodes_visited)):
            mst_distance += e[0]
            nodes_visited.append(e[1][0])
            nodes_visited.append(e[1][1])
            
    return mst_distance
            
            
def dynamic_weight(state):
    '''Return the number of unvisited cities in the current state'''
    return 0




########################################################
#   Functions provided so that you can more easily     #
#   Test your implementation                           #
########################################################


def make_rand_init_state(n):
    '''Generate a random initial state containing 'n' number of cities'''
    
    # set the max width and height of the 2d space
    x_max = 420
    y_max = 380
    
    cities_list = []
    coordinates_taken = []
    
    for i in range(n):
        name = '{}'.format(i+1)
        conflict = True
        
        while conflict:  
            x = randint(1 - x_max , x_max - 1)
            y = randint(1 - y_max , y_max - 1)
            conflict = False
            if (x,y) in coordinates_taken:
                conflict = True
                
        coordinates_taken.append((x,y))
        new_city = (name, x, y)
        cities_list.append(new_city)
    
    # choose a starting point at random 
    start_city = randint(1, n)
    
    return make_init_state(cities_list, start_city)



def draw_canvas(state):
    '''Draw all the cities in the current state in a canvas. Indicate the start
       city with a description and the current city by the turtle pointer head
    '''
    turtle.clear()
    turtle.hideturtle()
    turtle.up()
    turtle.pencolor("blue")
    current_city = state.current_city
    for city in state.cities:
        x = city.position[0]
        y = city.position[1]
        turtle.goto(x, y)
             
        if city.is_start:
            turtle.write('{}, Start'.format(city.name), align="center", font=("Arial", 12, "bold"))
        elif city == current_city:
            turtle.write('{}, Current'.format(city.name), align="center", font=("Arial", 12, "bold"))            
        else:
            turtle.write('{}'.format(city.name), align="center", font=("Arial", 12, "bold"))
 
    turtle.goto(current_city.position[0], current_city.position[1])
    
    
    
    
def draw_final_path(state):
    '''Draw the TSP path given the cities in the correct order'''
    if not state:
        return None
    
    states = []
    while state:
        states.append(state)
        state = state.parent    

    cities = [state.current_city for state in states]
    rest = deepcopy(cities)
    rest = rest[1:]
    rest.reverse()
    cities = [cities[0]] + rest
    
    turtle.clear()
    turtle.hideturtle()
    turtle.up()
    turtle.pensize(1)
    
    for city in cities:
        x = city.position[0]
        y = city.position[1]
        turtle.pencolor("red")
        turtle.goto(x, y)
        turtle.pencolor("black")
        
        if city.is_start:
            turtle.write('{}-Start'.format(city.name), align="center", font=("Arial", 11, "bold"))
        else:
            turtle.write('{}'.format(city.name), align="center",  font=("Arial", 11, "bold"))
        
        turtle.down()
        
    turtle.pencolor("red")
    turtle.goto(cities[0].position[0], cities[0].position[1])    


def get_city_list(state):
    '''Return [(node1, x, y), (node2, x, y)...]'''
    cities = []
    for city in state.cities:
        cities.append((city.name, city.position[0], city.position[1]))
    return cities



