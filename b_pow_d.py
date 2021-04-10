import time
import random
import algorithm
def b_power_dRunningTime(b=6,d = range(5,10,1)): 
    nValues = []	
    tValues = []
    runtime=0
    for x in d:
        start = time.time()
        algorithm.b_power_d(6,x)
        end = time.time() #end time
        runtime += (end - start) * 1000 #cover to milliseconds
     #get the average
    nValues.append(x)	#store n in this array
    tValues.append(runtime)#store time in this array
    return nValues,tValues
