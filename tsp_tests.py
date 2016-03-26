from tsp import *


def get_worst_cost(state):
    '''Starting from the start_city, travel to each city in the list one by one
       and come back to the start_city. Follow a polygon path. 
       This cost will be the UPPER BOUND on the minimum TSP cost.
    '''
    distances = []
    cities = deepcopy(state.cities)
    start_city = state.cities[0]
    while cities:
        curr_city = cities[0]
        next_city = cities[1]
        distances.append(dist_Euclidean(curr_city, next_city))
        del cities[0]
        if len(cities) == 1:
            # go back to the start city
            distances.append(dist_Euclidean(cities[0], start_city))
            break
    return sum(distances)


def test_successors(s):
    s.print_state()
    
    for i in s.successors():
        #test_heuristics(i)
        i.print_state()
        
        
def test_hash(s1, s2):
    return s1.hashable_state() == s2.hashable_state()
    

def goal_check(s):
    for city in s.cities:
        city.is_visited = True
    
    return tsp_goal_fn(s)


#def test_heuristics(s):
    #return (heur_min_moves(s))
    
    
def test_DFS_none(state):
    '''Depth first with no cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'depth_first', cc_level = 'none')
    print("=========Test. Depth first with no cycle checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)    
    
    
def test_DFS_path(state):
    '''Depth first with only path checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'depth_first', cc_level = 'path')
    print("=========Test. Depth first with only path checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)    


def test_DFS_full(state):
    '''Depth first with full cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'depth_first', cc_level = 'full')
    print("=========Test. Depth first with full cycle checking=========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)
    
    
def test_BFS_none(state):
    '''Breadth first with no cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'breadth_first', cc_level = 'none')
    print("=========Test. Breadth first with no cycle checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)


def test_BFS_path(state):
    '''Breadth first with only path checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'breadth_first', cc_level = 'path')
    print("=========Test. Breadth first with only path checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)


def test_BFS_full(state):
    '''Breadth first with full cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'breadth_first', cc_level = 'full')
    print("=========Test. Breadth first with full cycle checking=========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)


def test_UCS_none(state):
    '''Uniform Cost with no cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'astar', cc_level = 'none')
    print("=========Test. Uniform Cost with no cycle checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)
    

def test_UCS_path(state):
    '''Uniform Cost with only path checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'astar', cc_level = 'path')
    print("=========Test. Uniform Cost with only path checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)


def test_UCS_full(state):
    '''Uniform Cost with full cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)    
    se = SearchEngine(strategy = 'astar', cc_level = 'full')
    print("=========Test. Uniform Cost with full cycle checking==========")
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST)
    draw_final_path(final)


def test_Astar_none(state, heur_func):
    '''A* with no cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)    
    se = SearchEngine(strategy = 'astar', cc_level = 'none')
    print("=========Test. A* with no cycle checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST, heur_func)
    draw_final_path(final)
    
    
def test_Astar_path(state, heur_func):
    '''A* with only path checking'''
    UPPER_BOUND_COST = get_worst_cost(state)
    se = SearchEngine(strategy = 'astar', cc_level = 'path')
    print("=========Test. A* with only path checking==========") 
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST, heur_func)
    draw_final_path(final)


def test_Astar_full(state, heur_func):
    '''A* with full cycle checking'''
    UPPER_BOUND_COST = get_worst_cost(state)    
    se = SearchEngine(strategy = 'astar', cc_level = 'full')
    print("=========Test. A* with full cycle checking==========")
    final = se.search(state, tsp_goal_fn, UPPER_BOUND_COST, heur_func)
    draw_final_path(final)





if __name__ == '__main__':
   
    random_5 = [('4', -11, 244), ('1', 249, 253), ('2', 339, 151), ('3', -375, -228), ('5', 334, 255)]
    
    random_10 = [('2', 376, -126), ('1', -304, 123), ('3', -332, 281), ('4', 275, 113), ('5', 337, 210), ('6', 75, 121), ('7', 148, -176), ('8', -112, -328), ('9', 228, 354), ('10', -243, 263)]

    random_25 = [('3', -401, -267), ('1', -16, -95), ('2', 34, -312), ('4', -315, 31), ('5', 258, -140), ('6', 112, -60), ('7', 322, 221), ('8', 160, -10), ('9', 176, -91), ('10', 216, 218), ('11', -375, 151), ('12', 68, -334), ('13', 64, -47), ('14', -194, 263), ('15', -114, -221), ('16', 276, 111), ('17', -204, -285), ('18', -28, 6), ('19', -38, -48), ('20', -410, 199), ('21', -229, -33), ('22', -3, -315), ('23', -134, -118), ('24', 142, 72), ('25', 246, 311)]

    random_50 = [('37', -346, -319), ('1', 85, -237), ('2', 218, 170), ('3', -228, 343), ('4', 94, 194), ('5', 318, -49), ('6', 298, -73), ('7', 209, -230), ('8', 315, -95), ('9', -28, -269), ('10', -211, -305), ('11', 13, -314), ('12', 52, 143), ('13', -75, -94), ('14', -249, 352), ('15', -298, -203), ('16', 198, 87), ('17', -50, 218), ('18', 179, 144), ('19', 69, 27), ('20', -168, -365), ('21', 372, -14), ('22', 383, -40), ('23', -84, -78), ('24', 107, -113), ('25', -382, 361), ('26', 68, 58), ('27', 65, -16), ('28', 309, -222), ('29', -47, -69), ('30', 321, 326), ('31', 346, 286), ('32', 79, 102), ('33', 183, -13), ('34', 354, 72), ('35', -279, 157), ('36', -354, 260), ('38', 69, -219), ('39', -251, 171), ('40', -403, 367), ('41', 196, -171), ('42', 211, 0), ('43', 353, 43), ('44', -315, -373), ('45', -193, -269), ('46', 127, -197), ('47', 10, -326), ('48', 306, 370), ('49', -222, -159), ('50', 122, -141)]

    random_100 = [('37', 6, -378), ('1', 243, 313), ('2', -26, 226), ('3', 193, 248), ('4', -322, 337), ('5', -166, 320), ('6', -398, -130), ('7', -21, 152), ('8', -164, 233), ('9', 355, -75), ('10', -370, -90), ('11', -95, -61), ('12', 60, 193), ('13', -133, -189), ('14', -318, -338), ('15', -304, 159), ('16', 249, 113), ('17', 347, -141), ('18', -132, -52), ('19', 113, 25), ('20', 164, 137), ('21', -375, 63), ('22', 58, 230), ('23', -91, -174), ('24', 226, 119), ('25', 22, -362), ('26', -250, -343), ('27', 244, -132), ('28', -191, 267), ('29', -36, 99), ('30', 289, -373), ('31', 166, 85), ('32', -182, 11), ('33', -30, 159), ('34', 73, 376), ('35', 234, -175), ('36', -404, -370), ('38', 399, -268), ('39', -51, -296), ('40', 323, -26), ('41', -229, 39), ('42', -209, -2), ('43', -348, 3), ('44', -38, 107), ('45', 375, 314), ('46', -401, -316), ('47', 403, -86), ('48', -134, 161), ('49', 417, 45), ('50', 378, -90), ('51', -8, -298), ('52', -412, 333), ('53', 353, -1), ('54', 41, -48), ('55', -214, -74), ('56', -60, 117), ('57', 416, 372), ('58', 18, 276), ('59', 58, -7), ('60', -348, 190), ('61', -346, -225), ('62', -185, 290), ('63', 226, 137), ('64', 60, 353), ('65', 323, 203), ('66', 114, 308), ('67', -344, 343), ('68', -226, 315), ('69', 31, -342), ('70', 136, 112), ('71', -92, -320), ('72', 162, -90), ('73', 136, -312), ('74', 263, -120), ('75', -338, -280), ('76', 346, 86), ('77', 213, 99), ('78', -186, -233), ('79', 192, 173), ('80', 47, 129), ('81', 399, 142), ('82', -77, -188), ('83', -213, 68), ('84', 101, -367), ('85', -335, 23), ('86', -73, 188), ('87', 152, 271), ('88', 73, -171), ('89', 68, 121), ('90', -12, -154), ('91', 390, 333), ('92', -289, -173), ('93', -91, 266), ('94', 138, 241), ('95', -87, 129), ('96', 408, 144), ('97', -358, -79), ('98', -296, -237), ('99', -238, 182), ('100', 283, 209)]


    s5 = make_init_state(random_5, 4)
    
    s10 = make_init_state(random_10, 2)
    
    s25 = make_init_state(random_25, 3)
    
    s50 = make_init_state(random_50, 37)
    
    s100 = make_init_state(random_100, 37)
    
    #print ('_______________________________________________________________________________________________')
    #print ('Testing Successors')
    #test_successors(s1)

    #print ('_______________________________________________________________________________________________')
    #print ('Testing Hash Function')
    #print ('Expected=True\tReturned={}'.format(test_hash(s1, s2)))
    #print ('Expected=False\tReturned={}'.format(test_hash(s1, s3)))
    #print ('Expected=False\tReturned={}'.format(test_hash(s2, s3)))
    
    #print ('_______________________________________________________________________________________________')    
    #print ('Testing Goal Function')
    #print ('Expected=True\tReturned={}'.format(goal_check(goal_check_1)))
    #print ('Expected=False\tReturned={}'.format(tsp_goal_fn(s1)))
    #print ('Expected=False\tReturned={}'.format(tsp_goal_fn(s2)))
    
    
    #print ('_______________________________________________________________________________________________')
    #print ('Testing Heuristics')
    #test_heuristics(s1)
    
    #se.trace_on(1)
    
    
    
    #test_DFS_none(s5)
    #test_DFS_path(s5)
    #test_DFS_full(s5)
    
    #test_BFS_none(s5)
    #test_BFS_path(s5)
    #test_BFS_full(s5)
    
    #test_UCS_none(s5)
    #test_UCS_path(s5)
    #test_UCS_full(s5)
    
    #heur_func = None
    #test_Astar_none(s5, heur_func)
    #test_Astar_path(s5, heur_func)
    #test_Astar_full(s5, heur_func)