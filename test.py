
import random
from graph2 import Graph
import algorithm

import matplotlib
import matplotlib.pyplot as plt

import plot_running_time

if __name__ == "__main__":

    """
    The following code is for demonstrations
    Graph(100,100,6) is for creating a random map
    generateMatrix() creates a distance matrix
    randomFlightPlan() removes certain to create a flight map given branching factor
    you can verify the braching factor by calling calBF()

    uniform_cost_search()
    and
    a_star_search()
    from algorithm does the search
    """

    # g = Graph(100,100,6) # We 'Draw' a map in a coordinate system
    # mapFlight = g.read_graph()   # read map
    # distanceMatrix = g.generateMatrix()    # create distance matrix
    # flightPlanMatrix = g.randomFlightPlan(distanceMatrix,6)    # create flight plan matrix

    # g.calBF(flightPlanMatrix)

    # test1 = algorithm.uniform_cost_search(flightPlanMatrix,5,3)
    # test2 = algorithm.a_star_search(flightPlanMatrix,flightPlanMatrix,5,3)

    
    plot_running_time.show_all_time()# we plot graph here
 
    