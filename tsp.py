from search import *
from random import randint
from copy import deepcopy
import math
import turtle


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
    def __init__(self, curr_city, cities, action, gval, parent=None):
        """Initialize a tsp search state object."""
        StateSpace.__init__(self, action, gval, parent)
        self.curr_city = curr_city
        self.cities = cities    # cities = [node1, node2, ... nodek]
        

    def successors(self):
        '''Return list of tsp objects that are the successors of the current object'''
        States = []
        current_city = self.curr_city
        
        current_index = 0
        for city in self.cities:
            if city != current_city:
                new_gval = self.gval + dist_Euclidean(current_city, city)
                new_cities = deepcopy(self.cities)
                curr_city = new_cities[current_index]
                curr_city.is_visited = True
                del new_cities[current_index]
                new_cities.insert(0, curr_city)
                States.append(tsp(curr_city, new_cities, 'Move to {}'.format(city.name), new_gval, self))
            
            current_index += 1
            
        return States        
        
        
    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
        hash_list = []
        for city in self.cities:
            hash_list.append(city.get_city_details())
            
        hash_list.insert(0, self.curr_city) 
        
        return tuple(hash_list)
        

    def print_state(self):
        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))
                   
        for city in self.cities:
            print ('Name={}\tPosition={}\tVisited={}\tStart={}\tCurrent={}'.format(city.name, city.position, city.is_visited, city.is_start,city == self.curr_city))        

        print ('')



#############################################
# Goal Function and Initialization          #
#############################################


def tsp_goal_fn(state):
    '''Have we reached a goal state'''
    # Check if we're back at the start city
    if not (state.curr_city).is_start:
        return False
    else:
        goal = True
        for city in state.cities:
            if not city.is_visited:
                goal = False
                break
        return goal


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
    
    curr_city = all_cities[0]   # set the current city as the start_city
    return tsp(curr_city, all_cities, "START", 0)



#############################################
# heuristics                                #
#############################################


def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0


def Euclidean_Next(state):
    '''The euclidean distance to the nearest unvisited neighbour from the current city'''
    pass


def Euclidean_Start(state):
    '''The minimum euclidean distance from an unvisited city to the start city'''
    pass


def Manhattan_Next(state):
    '''The manhattan distance to the nearest unvisited neighbour from the current city'''
    pass


def Manhattan_Start(state):
    '''The minimum manhattan distance from an unvisited city to the start city'''
    pass


def MST(state):
    '''Estimated distance to travel all the unvisited nodes starting from the current city'''
    pass


def Euclidean_Next_MST_Euclidean_Start(state):
    return (  Euclidean_Next(state)
            + MST(state)
            + Euclidean_Start(state))


def Manhattan_Next_MST_Manhattan_Start(state):
    return (  Manhattan_Next(state)
            + MST(state)
            + Manhattan_Start(state))
            




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

    current_city = state.curr_city
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
    
    start_city = state.cities[0]
    cities = state.cities[1:]
    cities = [i for i in reversed(cities)]
    cities.insert(0, start_city)
    
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
    turtle.goto(start_city.position[0], start_city.position[1])    


def get_city_list(state):
    '''Return [(node1, x, y), (node2, x, y)...]'''
    cities = []
    for city in state.cities:
        cities.append((city.name, city.position[0], city.position[1]))
    return cities