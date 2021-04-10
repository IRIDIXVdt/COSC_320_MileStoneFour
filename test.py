
import random
from graph2 import Graph
import algorithm
import PlotRunningTime
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":
    g = Graph(100,100,10) # We 'Draw' a map in a coordinate system
    mapFlight = g.read_graph()   # read map
    distanceMatrix = g.generateMatrix()    # create distance matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,6)    # create flight plan matrix
    
    g.calBF(flightPlanMatrix)

    test1 = algorithm.uniform_cost_search(flightPlanMatrix,5,3)
    
    test2 = algorithm.a_star_search(flightPlanMatrix,flightPlanMatrix,5,3)
    # print(test)
    ns = range(1,100,20) #set X-axis range and incremental 
    factor = range(1,10,1)
    nValues, tValues = PlotRunningTime.runningTime(g,Ns = ns, numTrials = 10) #put value in to the runningTime method in PlotRunningTime page
    nValues2, tValues2 = PlotRunningTime.runningTime(g,Ns = ns, numTrials = 10)#put value in to the runningTime method in PlotRunningTime page
    plt.plot(nValues, tValues, color="red", label="A Star Search") #plot a star search running time with red line and a star search lable
    plt.plot(nValues2, tValues2, "--", color="blue", label="UCS") #plot UCS running time with -- line, blue color and UCS lable
    plt.plot(ns,[pow(6,b) for b in ns],color = "orange",label="O(d^b)") #plot O(d^b) running time with orange color and O(d^b) lable
    plt.xlabel('n') #X represents n
    plt.ylabel('Time(ms)')#Y represents Time(ms)
    plt.title('A star search running time')#Graph title represents A star search running time
    plt.legend()
    plt.show()
    