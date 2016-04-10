The main program to execute is tsp.py

Step 1: The first thing to input is the number of cities in the problem.
        Enter the number of cities: xx

Step 2: Once you input an integer, the next step is to choose the algorithm to use.
        You get to choose from 7 different algorithms, each indicated with a number.
        Simply enter the number corresponding to the algorithm you need to use.
        1: 'depth_first'
        2: 'breadth_first'
        3: 'ucs'
        4: 'best_first'
        5: 'astar'
        6: 'ida*'
        7: 'beam'

Step 3: Next, you get to choose the successor function. Since we developed 2 kinds of
        successors, you either input 1 or 2 corresponding to your choice.
        1: 'Normal Sucessors'
        2: 'Modified Successor'

Step 4: Suppose in step 3, you chose an algorithm that requires an heuristic, you
        will be prompted to choose one out of the 8 available.
        1: 'heur_MST_Euclidean'
        2: 'heur_MST_Manhattan'
        3: 'heur_MST_Greedy'
        4: 'heur_MST_Greedy_Full'
        5: 'dynamic_heur_MST_Euclidean'
        6: 'dynamic_heur_MST_Manhattan'
        7: 'dynamic_heur_Greedy'
        8: 'dynamic_heur_Greedy_Full'

        If you chose an algorithm that doesn't requires an heuristic, the search
        starts to compute the optimal path.
        
Step 5: Once the search has completed, a GUI with the TSP path will be presented.

Step 6: You will be prompted to either continue with another problem or exit.
        Input 0 to exit, or any key to continue: 
        
Step 7: Appreciate this cool interface and reward us :) :) :)