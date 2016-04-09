from search import *
from random import randint
from copy import deepcopy
import math
import turtle
import itertools
from MinimumSpanningTree import MinimumSpanningTree
from MinimumSpanningTree import MinimumSpanningCost



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
    
    xdiff = abs(x2 - x1)
    ydiff = abs(y2 - y1)
    
    return math.sqrt(xdiff*xdiff + ydiff*ydiff)


def dist_Manhattan(node1, node2):
    '''Compute the Manhattan distance between two nodes.'''

    # The two points are located on coordinates (x1,y1) and (x2,y2)
    (x1,y1) = node1.position
    (x2,y2) = node2.position
    
    return abs(x2-x1) + abs(y2-y1)




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

    def successors2(self):
        '''Return list of tsp objects that are the successors of the current object'''
        States = []
        current_city = self.current_city
        unvisited_cities = self.get_unvisited()
        
        for city in unvisited_cities:
            new_gval = self.gval + dist_Euclidean(current_city, city)
            new_cities = deepcopy(self.cities)
            current_index = self.cities.index(city)
            new_cities[current_index].is_visited = True
            States.append(tsp(new_cities[current_index], new_cities, 'Move to {}'.format(city.name), new_gval, self))
            
        if not unvisited_cities:
            # move from currrent city back to start
            start_city = self.get_start()
            new_gval = self.gval + dist_Euclidean(current_city, start_city)
            new_cities = deepcopy(self.cities)
            current_index = self.cities.index(start_city)
            new_cities[current_index].is_visited = True
            States.append(tsp(new_cities[current_index], new_cities, 'Move to {}'.format(start_city.name), new_gval, self))            
        return States        

    def successors(self):
        '''Return list of tsp objects that are the BEST choices of successors of the current object'''
        States = []
        current_city = self.current_city        
        best_choices = [city for city in get_best_choices(self)]
        
        for city in best_choices:
            new_gval = self.gval + dist_Euclidean(current_city, city)
            new_cities = deepcopy(self.cities)
            current_index = self.cities.index(city)
            new_cities[current_index].is_visited = True
            States.append(tsp(new_cities[current_index], new_cities, 'Move to {}'.format(city.name), new_gval, self))
            
        if not best_choices:
            # move from currrent city back to start
            start_city = self.get_start()
            new_gval = self.gval + dist_Euclidean(current_city, start_city)
            new_cities = deepcopy(self.cities)
            current_index = self.cities.index(start_city)
            new_cities[current_index].is_visited = True
            States.append(tsp(new_cities[current_index], new_cities, 'Move to {}'.format(start_city.name), new_gval, self))            
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


    def get_unvisited(self):
        return [city for city in self.cities if not city.is_visited]
    
    
    def get_start(self):
        for city in self.cities:
            if city.is_start:
                return city

    def get_city(self, name):
        for city in self.cities:
            if city.name == name:
                return city

#############################################
# Goal Function and Initialization          #
#############################################


def tsp_goal_fn(state):
    '''Have we reached a goal state, such that we have visited all cities
       and back at the start city.'''
    
    return not state.get_unvisited() and (state.current_city).is_start


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
    current_city.is_visited = True
    
    return tsp(current_city, all_cities, "START", 0)
    


#############################################
# heuristics                                #
#############################################

def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0


def heur_Euclidean(state):
    '''The MIN from all unvisited cities {
       The euclidean distance to the unvisited city from the current city + 
       The euclidean distance from that unvisited city back to the start city }
    '''
    current_city = state.current_city
    d1 = [dist_Euclidean(current_city, city) for city in state.get_unvisited()]
    
    start_city = state.get_start()
    d2 = [dist_Euclidean(start_city, city) for city in state.get_unvisited()]
    
    if not d1 and not d2:
        return 0
    else:
        return min(d1) + min(d2)
        

def heur_Manhattan(state):
    '''The MIN from all unvisited cities {
       The manhattan distance to the unvisited city from the current city + 
       The manhattan distance from that unvisited city to the start city }
    '''
    current_city = state.current_city
    d1 = [dist_Manhattan(current_city, city) for city in state.get_unvisited()]
    
    start_city = state.get_start()
    d2 = [dist_Manhattan(start_city, city) for city in state.get_unvisited()]
    
    if not d1 and not d2:
        return 0
    else:
        return min(d1) + min(d2)

def heur_Greedy(state):
    '''Returns the estimated Euclidean distance to the closest node
        to the current city + distance from that node to the start (goal)'''
    current_city = state.current_city
    closest_city = state.get_start()
    min_distance = 9999999

    for city in state.get_unvisited():
        distance = dist_Euclidean(current_city, city)

        if distance < min_distance:
            min_distance = distance
            closest_city = city

    distance_to_start = dist_Euclidean(closest_city, state.get_start())
    total_distance = min_distance + distance_to_start

    return total_distance

def heur_Greedy_Full(state):
    '''computes entire greedy path for this state, returns the cost'''
    current_city = state.current_city
    temp_city = state.current_city
    temp_distance = 9999999
    total_distance = 0
    next_city = state.get_start()
    marked_cities = []

    while (len(state.get_unvisited())>0):
        for city in state.get_unvisited():
            distance = dist_Euclidean(temp_city, city)

            if distance < temp_distance:
                temp_distance = distance
                next_city = city

        total_distance = total_distance + temp_distance
        temp_distance = 9999999
        current_city = next_city
        next_city.is_visited = True
        marked_cities.append(next_city)

    last_distance = dist_Euclidean(current_city, state.get_start())
    total_distance = total_distance + last_distance

    for city in marked_cities:
        city.is_visited = False

    return total_distance/1

def heur_MST_Euclidean(state):
    '''Estimated Euclidean distance to travel all the unvisited nodes
       starting from the current city + heur_Euclidean.'''
    return (MST(state, dist_Euclidean) + heur_Euclidean(state))


def heur_MST_Manhattan(state):
    '''Estimated Manhattan distance to travel all the unvisited nodes 
       starting from the current city + heur_Manhattan.'''
    return (MST(state, dist_Manhattan) + heur_Manhattan(state))

def heur_MST_Greedy(state):
    return (MST(state, dist_Euclidean) + heur_Greedy(state))

def heur_MST_Greedy_Full(state):
    return (MST(state, dist_Euclidean) + heur_Greedy_Full(state))

def dynamic_heur_MST_Euclidean(state):
    return dynamic_weight(state) * heur_MST_Euclidean(state)

def dynamic_heur_MST_Manhattan(state):
    return dynamic_weight(state) * heur_MST_Manhattan(state)

def dynamic_heur_Greedy(state):
    return dynamic_weight(state) * heur_Greedy(state)

def dynamic_heur_Greedy_Full(state):
    return dynamic_weight(state) * heur_Greedy_Full(state)
   
    
#############################################
# Helper functions for heuristics           #
#############################################

def MST(state, func):
    ''' Kruskal's algorithm.
        1. Sort the edges of G in ascending (non-decreasing) order
        2. Return mst_distance
    '''
    current_city = state.current_city
    unvisited_cities = state.get_unvisited()
    
    city_pairs = itertools.combinations(unvisited_cities, 2)
    
    edges = []
    for x,y in city_pairs:
        edges.append((func(x, y), (x,y)))
    edges = sorted(edges, key=lambda x: x[0])
    
    G = {}
    for c in unvisited_cities:
        G[c.name] = {}
        
    for e in edges:
        city1 = e[1][0].name
        city2 = e[1][1].name
        edge = e[0]
        G[city1][city2] = edge
        G[city2][city1] = edge
        
    return MinimumSpanningCost(G)
            
            
def dynamic_weight(state):
    '''Return the number of unvisited cities in the current state'''
    return len(state.get_unvisited()) + 1



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



def get_best_choices(state):
    current_city = state.current_city
    unvisited_cities = state.get_unvisited()
    unvisited_cities.insert(0, current_city)
    city_pairs = itertools.combinations(unvisited_cities, 2)
    
    edges = []
    for x,y in city_pairs:
        edges.append((dist_Euclidean(x, y), (x,y)))
    edges = sorted(edges, key=lambda x: x[0])
       
    good_sucessors = []    
    for e in edges:
        x,y = e[1]
        if x == current_city:
            good_sucessors.append(y)
        elif y == current_city:
            good_sucessors.append(x)
        if len(state.cities) > 5 and len(good_sucessors) >= len(state.cities)/5:
            break
        
    return good_sucessors


if __name__ == "__main__":
    #test_Greedy_BFS(state, heur_MST_Euclidean)
    #test_Greedy_BFS(state, heur_MST_Manhattan)
    #test_Greedy_BFS(state, heur_MST_Greedy)
    #test_Greedy_BFS(state, heur_MST_Greedy_Full)
    #test_Greedy_BFS(state, dynamic_heur_MST_Euclidean)
    #test_Greedy_BFS(state, dynamic_heur_MST_Manhattan)
    #test_Greedy_BFS(state, dynamic_heur_Greedy)
    #test_Greedy_BFS(state, dynamic_heur_Greedy_Full)
    
    no_cities = 1
    
    algorithms = {1: 'depth_first',
                  2: 'breadth_first',
                  3: 'ucs',
                  4: 'best_first',
                  5: 'astar',
                  6: 'ida*',
                  7: 'beam'}
    
    heuristics = {1: 'heur_MST_Euclidean',
                  2: 'heur_MST_Manhattan',
                  3: 'heur_MST_Greedy',
                  4: 'heur_MST_Greedy_Full',
                  5: 'dynamic_heur_MST_Euclidean',
                  6: 'dynamic_heur_MST_Manhattan',
                  7: 'dynamic_heur_Greedy',
                  8: 'dynamic_heur_Greedy_Full'}
    
    while no_cities:
                      
        try:
            no_cities = int(input("Enter the number of cities: "))
            state = make_rand_init_state(no_cities)
            
            print (algorithms)
            strategy = int(input("\nChoose the algorithm to use: "))
            
            if strategy > 3:
                print (heuristics)
                heur_func = int(input("\nChoose the heuristic to use: "))
                
                se = SearchEngine(algorithms[strategy], cc_level = 'full')
                final = se.search(state, tsp_goal_fn, eval(heuristics[heur_func]))
                draw_final_path(final)     
                
            else:
                se = SearchEngine(algorithms[strategy], cc_level = 'full')
                final = se.search(state, tsp_goal_fn)
                draw_final_path(final)               
            
            print ('________________________________________________________')
            no_cities = int(input("\nInput 0 to exit, or any key to continue: "))
            
        except ValueError:
            pass
            
        