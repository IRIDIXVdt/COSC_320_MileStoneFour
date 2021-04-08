import random
from queue import PriorityQueue
from graph2 import Graph
from A_star_search import a_star_search

#def heuristic(goal, nbr):
    #return abs(goal - nbr.get_id())



if __name__ == "__main__":
    # Using the insertion method to generate the graph
    g = Graph(10,10,5)
   
    # read map
    mapFlight = g.read_graph()
    # create distance matrix
    distanceMatrix = g.generateMatrix()
    # create flight plan matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,3)

    print(flightPlanMatrix)
    
    g.calBF(flightPlanMatrix)
    search = a_star_search()
    heuristic = search.heuristic()
    find_path = search.a_star_search_algorithm()


    
    