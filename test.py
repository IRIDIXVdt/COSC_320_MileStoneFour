import random
from queue import PriorityQueue
from graph2 import Graph
from algorithm import algorithm
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
    test = algorithm.find_neighbours(flightPlanMatrix,2)


    
    