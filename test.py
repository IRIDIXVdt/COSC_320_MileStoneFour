
import random
from graph2 import Graph
import algorithm
import PlotRunningTime
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Using the insertion method to generate the graph
    g = Graph(100,100,10)
    # read map
    mapFlight = g.read_graph()
    # create distance matrix
    distanceMatrix = g.generateMatrix()
    # create flight plan matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,3)

    for line in flightPlanMatrix:
        print(line)
    
    g.calBF(flightPlanMatrix)

    test1 = algorithm.uniform_cost_search(flightPlanMatrix,5,6)
    
    # test2 = algorithm.find_neighbours(flightPlanMatrix,5)
    # print(test)
    # ns = range(1,1000,50) #set X-axis range and incremental 
    # nValues, tValues = PlotRunningTime.runningTime(g,Ns = ns, numTrials = 10)
    # plt.plot(nValues, tValues, color="red", label="Random Graph Runing Time")
    # plt.xlabel('n')
    # plt.ylabel('Time(ms)')
    # plt.title('Random Graph Test')
    # plt.legend()
    # plt.show()
    