# from graph2 import Graph
# import time
# import random
# import algorithm
# def runningTime(graph, Ns = range(5,10,1), numTrials = 5, branching_factor):
#     #Ns X-axis start form 0, end at 5000, 500 incremental 
#     #numTrials At one point, run numTrials times then get the average time
#     nValues = []	
#     tValues = []
#     for n in Ns:
#         runtime = 0
#         for i in range(numTrials):

#             g = Graph(100,100,n) # We 'Draw' a map in a coordinate system
#             mapFlight = g.read_graph()   # read map
#             distanceMatrix = g.generateMatrix()    # create distance matrix
#             flightPlanMatrix = g.randomFlightPlan(distanceMatrix,branching_factor)    # create flight plan matrix
#             startPoint = random.randint(0,n-1)
#             endPoint = random.randint(0,n-1)
#             start = time.time()#start time
#             algorithm.a_star_search(flightPlanMatrix,flightPlanMatrix,startPoint,endPoint) #call algorithm
#             end = time.time() #end time
#             runtime += (end - start) * 1000 #cover to milliseconds
#         runtime = runtime/numTrials #get the average
#         nValues.append(pow(branching_factor,n))	#store n in this array
#         tValues.append(runtime)#store time in this array
#     return nValues,tValues
            