
import random
from graph2 import Graph
import algorithm
import PlotRunningTime
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":
    g = Graph(100,100,100) # We 'Draw' a map in a coordinate system
    mapFlight = g.read_graph()   # read map
    distanceMatrix = g.generateMatrix()    # create distance matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,6)    # create flight plan matrix
    
    g.calBF(flightPlanMatrix)

    test1 = algorithm.uniform_cost_search(flightPlanMatrix,5,10)
    
    test2 = algorithm.a_star_search(flightPlanMatrix,flightPlanMatrix,5,10)
    # print(test)
    #ns = range(1,1000,50) #set X-axis range and incremental 
    #nValues, tValues = PlotRunningTime.runningTime(g,Ns = ns, numTrials = 10)
    #plt.plot(nValues, tValues, color="red", label="Random Graph Runing Time")
    #plt.xlabel('n')
    #plt.ylabel('Time(ms)')
    #plt.title('Random Graph Test')
    #plt.legend()
    #plt.show()
    