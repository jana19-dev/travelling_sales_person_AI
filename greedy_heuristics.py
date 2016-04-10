''' THIS WAS USED TO GET FASTER RESULTS BUT IT WASN"T GIVING OPTIMAL RESULTS.
    SO WE ARE NOT USING THIS IN THE FINAL CODE.
'''

import tsp

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

    return total_distance

    
def heur_MST_Greedy(state):
    return (MST(state, dist_Euclidean) + heur_Greedy(state))
    
def heur_MST_Greedy_Full(state):
    return (MST(state, dist_Euclidean) + heur_Greedy_Full(state))

def dynamic_heur_Greedy(state):
    return dynamic_weight(state) * heur_Greedy(state)

def dynamic_heur_Greedy_Full(state):
    return dynamic_weight(state) * heur_Greedy_Full(state)