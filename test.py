
import random
from graph2 import Graph
import algorithm
import PlotRunningTime
import matplotlib
import matplotlib.pyplot as plt
import ucsRunningTime
import b_pow_d

if __name__ == "__main__":
    factor = range(5,10,1)
    g = Graph(100,100,6) # We 'Draw' a map in a coordinate system
    mapFlight = g.read_graph()   # read map
    distanceMatrix = g.generateMatrix()    # create distance matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,6)    # create flight plan matrix
    
    g.calBF(flightPlanMatrix)

    test1 = algorithm.uniform_cost_search(flightPlanMatrix,5,3)
    
    test2 = algorithm.a_star_search(flightPlanMatrix,flightPlanMatrix,5,3)
    # print(test)
    ns = range(5,10,1) #set X-axis range and incremental 
    nValues, tValues = PlotRunningTime.runningTime(g,Ns = ns, numTrials = 10) #put value in to the runningTime method in PlotRunningTime page
    nValues2, tValues2 = ucsRunningTime.runningTime(g,Ns = ns, numTrials = 10)#put value in to the runningTime method in ucsRunningTime page
    nValues3, tValues3 = b_pow_d.b_power_dRunningTime(b = 6, d = factor) #put value in to the b_power_dRunningTime in b_pow_d page
    plt.plot(nValues, tValues, color="red", label="A Star Search") #plot a star search running time with red line and a star search lable
    plt.plot(nValues2, tValues2, "--", color="blue", label="UCS") #plot UCS running time with -- line, blue color and UCS lable
    plt.plot(nValues3,nValues3,color = "orange" , label = "b_pow_d")
    plt.xlabel('b^d') #X represents n
    plt.ylabel('Time(ms)')#Y represents Time(ms)
    plt.title('A star search running time')#Graph title represents A star search running time
    plt.legend()
    plt.show()
    