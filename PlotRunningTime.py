from graph2 import Graph
import time
def runningTime(graph, Ns = range(1,5000, 500), numTrials = 20):
	#Ns X-axis start form 0, end at 5000, 500 incremental 
	#numTrials At one point, run numTrials times then get the average time
	nValues = []	
	tValues = []
	for n in Ns:
		runtime = 0
		for i in range(numTrials):
			start = time.time()#start time
			Graph(2000,2000,1000) #call algorithm
			end = time.time() #end time
			runtime += (end - start) * 1000 #cover to milliseconds
		runtime = runtime/numTrials #get the average
		nValues.append(n)	#store n in this array
		tValues.append(runtime)#store time in this array
	return nValues,tValues
			