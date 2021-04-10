from graph2 import Graph
import algorithm 
import time
import random
def runningTime(graph, Ns = range(1,5000, 500), numTrials = 20):
    #Ns X-axis start form 0, end at 5000, 500 incremental 
    #numTrials At one point, run numTrials times then get the average time
    nValues = []	
    tValues = []
    for n in Ns:
        runtime = 0
        for i in range(numTrials):
            #g = Graph(100,100,100)
            #mapFlight = g.read_graph()   # read map
            #distanceMatrix = g.generateMatrix()
            #flightPlanMatrix = g.randomFlightPlan(distanceMatrix,6)    # create flight plan matrix
            #startPoint = random.randint(0,99)
            #endPoint = random.randint(0,99)
            start = time.time()#start time
            #algorithm.a_star_search(flightPlanMatrix,flightPlanMatrix,startPoint,endPoint)
            end = time.time() #end time
            runtime += (end - start) * 1000 #cover to milliseconds
        runtime = runtime/numTrials #get the average
        nValues.append(n)	#store n in this array
        tValues.append(runtime)#store time in this array
    return nValues,tValues
            