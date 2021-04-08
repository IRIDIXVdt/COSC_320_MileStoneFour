import random
from graph2 import Graph
import algorithm


if __name__ == "__main__":
    # Using the insertion method to generate the graph
    g = Graph(10,10,8)
    # read map
    mapFlight = g.read_graph()
    # create distance matrix
    distanceMatrix = g.generateMatrix()
    # create flight plan matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,3)

    for line in flightPlanMatrix:
        print(line)
    
    g.calBF(flightPlanMatrix)
    test = algorithm.find_neighbours(flightPlanMatrix,2)
    print(test)


    
    