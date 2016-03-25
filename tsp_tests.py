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
    
    random_5 = [('4', -11, 244), ('1', 249, 253), ('2', 339, 151), ('3', -375, -228), ('5', 334, 255)]
    
    random_6 = [('2', -97, 379), ('1', -186, 105), ('3', -87, -139), ('4', 14, -269), ('5', 259, -298), ('6', 78, 280)]
    
    random_7 = [('3', 289, -116), ('1', 315, -150), ('2', -232, -275), ('4', 65, 288), ('5', -182, 7), ('6', 403, -230), ('7', 145, -101)]

    random_8 = [('5', -134, -99), ('1', 345, -194), ('2', 352, 348), ('3', -387, -301), ('4', 99, -377), ('6', 269, -178), ('7', 134, 167), ('8', 297, 364)]

    random_9 = [('6', 259, -72), ('1', 395, 55), ('2', 107, -315), ('3', 204, -225), ('4', 256, 297), ('5', 199, 358), ('7', 167, 119), ('8', -84, 313), ('9', -163, -318)]
    
    random_10 = [('2', 376, -126), ('1', -304, 123), ('3', -332, 281), ('4', 275, 113), ('5', 337, 210), ('6', 75, 121), ('7', 148, -176), ('8', -112, -328), ('9', 228, 354), ('10', -243, 263)]

    random_20 = [('10', -245, 5), ('1', -59, -277), ('2', -350, 179), ('3', -283, -207), ('4', -200, -231), ('5', -416, -83), ('6', 282, 46), ('7', 195, 60), ('8', -228, 18), ('9', -334, 1), ('11', -144, 79), ('12', -203, -140), ('13', -171, 351), ('14', 284, -187), ('15', 105, 376), ('16', 338, 112), ('17', 34, 341), ('18', -290, -341), ('19', -134, -120), ('20', -190, 142)]

    random_30 = [('12', 106, 169), ('1', -208, 182), ('2', -227, 281), ('3', 28, -261), ('4', -125, 97), ('5', 66, 145), ('6', -328, 327), ('7', 254, 91), ('8', 177, -301), ('9', 14, 140), ('10', 9, -16), ('11', -193, 276), ('13', 133, -159), ('14', -309, -344), ('15', 170, 262), ('16', 183, 280), ('17', -365, -216), ('18', 217, -56), ('19', 91, 220), ('20', -22, 136), ('21', 51, -303), ('22', 193, -45), ('23', -408, -212), ('24', -258, 255), ('25', 379, 114), ('26', 70, 273), ('27', -172, 133), ('28', 233, 133), ('29', -162, 53), ('30', -293, 131)]

    random_40 = [('22', -26, -372), ('1', -138, 203), ('2', 173, -70), ('3', 277, -2), ('4', 154, -99), ('5', -328, -84), ('6', -50, -41), ('7', 371, -87), ('8', -282, 145), ('9', -94, -58), ('10', 93, 107), ('11', 225, -293), ('12', 41, -70), ('13', 156, 136), ('14', -148, -137), ('15', 152, -226), ('16', 387, -295), ('17', -23, 262), ('18', 194, -366), ('19', -337, -375), ('20', 197, -264), ('21', -51, 38), ('23', 389, 126), ('24', 316, 185), ('25', 128, -228), ('26', 312, -108), ('27', -308, -231), ('28', 234, 64), ('29', 173, -12), ('30', -417, 302), ('31', -240, -183), ('32', 362, 92), ('33', -165, -82), ('34', 346, -164), ('35', 118, -200), ('36', 63, 142), ('37', 205, 359), ('38', 101, 214), ('39', 16, -176), ('40', 122, 70)]

    s5 = make_init_state(random_5, 4)
    s6 = make_init_state(random_6, 2)
    s7 = make_init_state(random_7, 3)
    s8 = make_init_state(random_8, 5)
    s9 = make_init_state(random_9, 6)

    s10 = make_init_state(random_10, 2)
    s20 = make_init_state(random_20, 10)
    s30 = make_init_state(random_30, 12)
    s40 = make_init_state(random_40, 22)
    
    #goal_check_1 = deepcopy(s1)
    
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
    
    
    
    
    
    se = SearchEngine('astar', 'full')
    #se.trace_on(2)
    #final = se.search(s10, tsp_goal_fn, heur_zero)
    #draw_final_path(final)
    
    
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
    
    
    
    
    
    