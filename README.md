# csc384-tsp
CSC 384 Project TSP

Title:	 Traveling Salesman Problem

Type:	 Search

Description:
Our problem is the travelling salesman problem. Given n different locations, what is the shortest possible route that visits each node exactly once and returns to the origin node? We will be using  heuristic search to find the route. 
There are many different heuristics for this problem and we will be using multiple techniques including finding the nearest neighbor and constructing a minimum spanning tree. 
This project is well suited to heuristic search because it is NP-hard. The running time of using anything other than a heuristic search becomes impractical with anything other than extremely small datasets. 
We will start each search at an origin node and then use heuristics to find the next node to visit. We will know that we have arrived at our goal state when we visited each node exactly once and are back in the origin node.


Evaluation Plan:
We will be comparing the space and time complexity of different heuristics searches. More specifically, we’ll compare Greedy, A* and its variants - Beam Search, Iterative Deepening and Dynamic Weighting. 
We will keep track of the number of nodes expanded to reach the optimal solution and the total time taken from start to end. We will also note down instances where each heuristics performs extremely well or very poorly and give reasonable explanations as to what is the case.
Test cases will be developed by generating random places to visit in a 2D plane. We will start with fewer nodes in the beginning to test that the path returned is actually optimum and then increase the nodes and its complexity to measure performance. 
Since the TSP is a NP-Hard problem, we cannot check if we have the optimal solution as the number of nodes increases. 
For that, we must be confident in our heuristic and eyeball our solution to see if it at least makes sense.
