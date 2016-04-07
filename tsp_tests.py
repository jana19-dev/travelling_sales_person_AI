from tsp import *



def test_DFS(state):
    '''Depth first with full cycle checking'''
    se = SearchEngine(strategy = 'depth_first', cc_level = 'full')
    print("=========Test. Depth first with full cycle checking=========") 
    final = se.search(state, tsp_goal_fn)
    draw_final_path(final)
    

def test_BFS(state):
    '''Breadth first with full cycle checking'''
    se = SearchEngine(strategy = 'breadth_first', cc_level = 'full')
    print("=========Test. Breadth first with full cycle checking=========") 
    final = se.search(state, tsp_goal_fn)
    draw_final_path(final)


def test_UCS(state):
    '''Uniform Cost with full cycle checking'''
    se = SearchEngine(strategy = 'ucs', cc_level = 'full')
    print("=========Test. Uniform Cost with full cycle checking==========")
    final = se.search(state, tsp_goal_fn)
    draw_final_path(final)


def test_Astar(state, heur_func=heur_zero):
    '''A* with full cycle checking'''
    se = SearchEngine(strategy = 'astar', cc_level = 'full')
    print("=========Test. A* with full cycle checking==========")
    final = se.search(state, tsp_goal_fn, heur_func)
    draw_final_path(final)


def test_Greedy_BFS(state, heur_func=heur_zero):
    '''Greedy BFS with full cycle checking'''
    se = SearchEngine(strategy = 'best_first', cc_level = 'full')
    print("=========Test. Greedy BFS with full cycle checking==========")
    final = se.search(state, tsp_goal_fn, heur_func)
    draw_final_path(final)
    
    
def test_IDAstar(state, heur_func=heur_zero, LIMIT=1):
    '''IDA* with full cycle checking'''
    se = SearchEngine(strategy = 'ida*', cc_level = 'full')
    print("=========Test. IDA* with full cycle checking DEPTH {}==========".format(LIMIT))
    final = se.search(state, tsp_goal_fn, heur_func, LIMIT)
    draw_final_path(final)


def test_Beam(state, heur_func=heur_zero, LIMIT=15):
    '''Beam search with full cycle checking'''
    se = SearchEngine(strategy = 'beam', cc_level = 'full')
    print("=========Test. Beam search with full cycle checking==========")
    final = se.search(state, tsp_goal_fn, heur_func, LIMIT)
    draw_final_path(final)




if __name__ == '__main__':
   
    random_5 = [('2', 170, -147), ('1', -325, -216), ('3', 331, 64), ('4', 65, 307), ('5', 69, -96)]
    
    random_10 = [('2', 376, -126), ('1', -304, 123), ('3', -332, 281), ('4', 275, 113), ('5', 337, 210), ('6', 75, 121), ('7', 148, -176), ('8', -112, -328), ('9', 228, 354), ('10', -243, 263)]

    random_25 = [('3', -401, -267), ('1', -16, -95), ('2', 34, -312), ('4', -315, 31), ('5', 258, -140), ('6', 112, -60), ('7', 322, 221), ('8', 160, -10), ('9', 176, -91), ('10', 216, 218), ('11', -375, 151), ('12', 68, -334), ('13', 64, -47), ('14', -194, 263), ('15', -114, -221), ('16', 276, 111), ('17', -204, -285), ('18', -28, 6), ('19', -38, -48), ('20', -410, 199), ('21', -229, -33), ('22', -3, -315), ('23', -134, -118), ('24', 142, 72), ('25', 246, 311)]

    random_50 = [('37', -346, -319), ('1', 85, -237), ('2', 218, 170), ('3', -228, 343), ('4', 94, 194), ('5', 318, -49), ('6', 298, -73), ('7', 209, -230), ('8', 315, -95), ('9', -28, -269), ('10', -211, -305), ('11', 13, -314), ('12', 52, 143), ('13', -75, -94), ('14', -249, 352), ('15', -298, -203), ('16', 198, 87), ('17', -50, 218), ('18', 179, 144), ('19', 69, 27), ('20', -168, -365), ('21', 372, -14), ('22', 383, -40), ('23', -84, -78), ('24', 107, -113), ('25', -382, 361), ('26', 68, 58), ('27', 65, -16), ('28', 309, -222), ('29', -47, -69), ('30', 321, 326), ('31', 346, 286), ('32', 79, 102), ('33', 183, -13), ('34', 354, 72), ('35', -279, 157), ('36', -354, 260), ('38', 69, -219), ('39', -251, 171), ('40', -403, 367), ('41', 196, -171), ('42', 211, 0), ('43', 353, 43), ('44', -315, -373), ('45', -193, -269), ('46', 127, -197), ('47', 10, -326), ('48', 306, 370), ('49', -222, -159), ('50', 122, -141)]

    random_100 = [('37', 6, -378), ('1', 243, 313), ('2', -26, 226), ('3', 193, 248), ('4', -322, 337), ('5', -166, 320), ('6', -398, -130), ('7', -21, 152), ('8', -164, 233), ('9', 355, -75), ('10', -370, -90), ('11', -95, -61), ('12', 60, 193), ('13', -133, -189), ('14', -318, -338), ('15', -304, 159), ('16', 249, 113), ('17', 347, -141), ('18', -132, -52), ('19', 113, 25), ('20', 164, 137), ('21', -375, 63), ('22', 58, 230), ('23', -91, -174), ('24', 226, 119), ('25', 22, -362), ('26', -250, -343), ('27', 244, -132), ('28', -191, 267), ('29', -36, 99), ('30', 289, -373), ('31', 166, 85), ('32', -182, 11), ('33', -30, 159), ('34', 73, 376), ('35', 234, -175), ('36', -404, -370), ('38', 399, -268), ('39', -51, -296), ('40', 323, -26), ('41', -229, 39), ('42', -209, -2), ('43', -348, 3), ('44', -38, 107), ('45', 375, 314), ('46', -401, -316), ('47', 403, -86), ('48', -134, 161), ('49', 417, 45), ('50', 378, -90), ('51', -8, -298), ('52', -412, 333), ('53', 353, -1), ('54', 41, -48), ('55', -214, -74), ('56', -60, 117), ('57', 416, 372), ('58', 18, 276), ('59', 58, -7), ('60', -348, 190), ('61', -346, -225), ('62', -185, 290), ('63', 226, 137), ('64', 60, 353), ('65', 323, 203), ('66', 114, 308), ('67', -344, 343), ('68', -226, 315), ('69', 31, -342), ('70', 136, 112), ('71', -92, -320), ('72', 162, -90), ('73', 136, -312), ('74', 263, -120), ('75', -338, -280), ('76', 346, 86), ('77', 213, 99), ('78', -186, -233), ('79', 192, 173), ('80', 47, 129), ('81', 399, 142), ('82', -77, -188), ('83', -213, 68), ('84', 101, -367), ('85', -335, 23), ('86', -73, 188), ('87', 152, 271), ('88', 73, -171), ('89', 68, 121), ('90', -12, -154), ('91', 390, 333), ('92', -289, -173), ('93', -91, 266), ('94', 138, 241), ('95', -87, 129), ('96', 408, 144), ('97', -358, -79), ('98', -296, -237), ('99', -238, 182), ('100', 283, 209)]


    s5 = make_init_state(random_5)
    
    s10 = make_init_state(random_10)
    
    s25 = make_init_state(random_25)
    
    s50 = make_init_state(random_50)
    
    s100 = make_init_state(random_100)
    
 
    
    state = s10

    #test_DFS(state)

    #test_BFS(state)

    #test_UCS(state)
    
    #test_Astar(state, heur_MST_Euclidean)
    #test_Astar(state, dynamic_heur_MST_Euclidean)
    #test_Astar(state, heur_MST_Manhattan)
    #test_Astar(state, dynamic_heur_MST_Manhattan)
    
    #test_Greedy_BFS(state, heur_MST_Euclidean)
    #test_Greedy_BFS(state, dynamic_heur_MST_Euclidean)
    #test_Greedy_BFS(state, heur_MST_Manhattan)
    #test_Greedy_BFS(state, dynamic_heur_MST_Manhattan)
    
    test_IDAstar(state, heur_MST_Euclidean)
    test_IDAstar(state, dynamic_heur_MST_Euclidean)
    test_IDAstar(state, heur_MST_Manhattan)
    test_IDAstar(state, dynamic_heur_MST_Manhattan)
    
    #test_Beam(state, heur_MST_Euclidean)
    #test_Beam(state, dynamic_heur_MST_Euclidean)
    #test_Beam(state, heur_MST_Manhattan)
    #test_Beam(state, dynamic_heur_MST_Manhattan)