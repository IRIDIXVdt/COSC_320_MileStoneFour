from graph2 import Graph
import time
import random
import algorithm
def runningTime(graph, Ns = range(1,100, 20), numTrials = 5):
    #Ns X-axis start form 0, end at 5000, 500 incremental 
    #numTrials At one point, run numTrials times then get the average time
    nValues = []	
    tValues = []
    for n in Ns:
        runtime = 0
        for i in range(numTrials):

            g = Graph(100,100,n) # We 'Draw' a map in a coordinate system
            mapFlight = g.read_graph()   # read map
            distanceMatrix = g.generateMatrix()    # create distance matrix
            flightPlanMatrix = g.randomFlightPlan(distanceMatrix,6)    # create flight plan matrix
            startPoint = random.randint(0,n-1)
            endPoint = random.randint(0,n-1)
            start = time.time()#start time
            algorithm.a_star_search(flightPlanMatrix,flightPlanMatrix,startPoint,endPoint) #call algorithm
            algorithm.uniform_cost_search(flightPlanMatrix,startPoint,endPoint)
            end = time.time() #end time
            runtime += (end - start) * 1000 #cover to milliseconds
        runtime = runtime/numTrials #get the average
        nValues.append(n)	#store n in this array
        tValues.append(runtime)#store time in this array
    return nValues,tValues
            