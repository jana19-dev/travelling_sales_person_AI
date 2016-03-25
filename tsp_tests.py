from tsp import *



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
    
    


if __name__ == '__main__':

    #se.trace_on(1)
    
    cities_list_1 = [('4', 221, -286),
                     ('1', -100, -234),
                     ('2', -286, 71),
                     ('3', -413, -74),
                     ('5', -61, -289)]
    
 
    cities_list_2 = [('4', 221, -286),
                     ('1', -100, -234),
                     ('2', -286, 71),
                     ('3', -413, -74),
                     ('5', -61, -289)]    
 
 
    cities_list_3 = [('4', 220, -286),
                     ('1', -100, -234),
                     ('2', -30, 71),
                     ('3', -413, -74),
                     ('5', -61, -289)]     
    
    s1 = make_init_state(cities_list_1, 4)
    s2 = make_init_state(cities_list_2, 4)
    s3 = make_init_state(cities_list_3, 3)

    goal_check_1 = deepcopy(s1)
    
    print ('_______________________________________________________________________________________________')
    print ('Testing Successors')
    test_successors(s1)

    print ('_______________________________________________________________________________________________')
    print ('Testing Hash Function')
    print ('Expected=True\tReturned={}'.format(test_hash(s1, s2)))
    print ('Expected=False\tReturned={}'.format(test_hash(s1, s3)))
    print ('Expected=False\tReturned={}'.format(test_hash(s2, s3)))
    
    print ('_______________________________________________________________________________________________')    
    print ('Testing Goal Function')
    print ('Expected=True\tReturned={}'.format(goal_check(goal_check_1)))
    print ('Expected=False\tReturned={}'.format(tsp_goal_fn(s1)))
    print ('Expected=False\tReturned={}'.format(tsp_goal_fn(s2)))
    
    
    print ('_______________________________________________________________________________________________')
    print ('Testing Heuristics')
    #test_heuristics(s1)
    
    
    
    
    
    #se = SearchEngine('astar', 'full')
    #se.trace_on(2)
    #final = se.search(s17, rushhour_goal_fn, heur_min_moves)
    
    
    
    #print("=========Test 1. Astar with h_min heuristic========")
    #se.search(s8, rushhour_goal_fn, heur_min_moves)
    #print("===================================================")
    #print("")
    
    
    #se.set_strategy('breadth_first')
    #print("=========Test 3a. Breadth first (full cycle checking)==")
    #se.search(s8, rushhour_goal_fn)
    #print("===================================================")
    #print("")
    
    #se.set_strategy('breadth_first', 'path')
    #print("=========Test 3a. Breadth first with only path checking=====")
    #se.search(s8, rushhour_goal_fn)
    #print("===================================================")
    #print("")
    
    #se.set_strategy('breadth_first', 'none')
    #print("=========Test 3a. Breadth first with no cycle checking=====")
    #se.search(s8, rushhour_goal_fn)
    #print("===================================================")
    #print("")
    

    #se.set_strategy('breadth_first', 'path')
    #print("=========Test 4. Breadth first on unreachable goal with only path checking==")
    #se.search(s7, rushhour_goal_fn)
    #print("========================================================")
    #print("")
    
    #se.set_strategy('breadth_first', 'full')
    #print("=========Test 5. Breadth first on unreachable goal with full checking==")
    #se.search(s7, rushhour_goal_fn)
    #print("========================================================")
    #print("")
    
    #se.set_strategy('depth_first')

    #print("=========Test 6. Depth first on unreachable goal with path checking==")
    #se.search(s7, rushhour_goal_fn)
    #print("========================================================")
    #print("")
    
    
    
    
    
    