import random
from queue import PriorityQueue

from graph2 import Graph


#def heuristic(goal, nbr):
    #return abs(goal - nbr.get_id())



if __name__ == "__main__":
    # Using the insertion method to generate the graph
    g = Graph(1000,1000,100)
   
    # read map
    mapFlight = g.read_graph()
    # create distance matrix
    distanceMatrix = g.generateMatrix()
    # create flight plan matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,6)

    print(flightPlanMatrix)
    g.calBF(flightPlanMatrix)

    
    