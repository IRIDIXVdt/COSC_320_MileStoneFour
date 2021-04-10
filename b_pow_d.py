import time
import random
import algorithm
import matplotlib
import matplotlib.pyplot as plt
from graph2 import Graph
import math

class Quantity:
    def __init__(self, b,d):
        self.b = b
        self.d = d
    def __eq__(self, other):    # Compare nodes
        return self.d*math.log10(self.b) == other.d*math.log10(other.b)
    def __lt__(self, other): # Sort nodes
         return self.d*math.log10(self.b) < other.d*math.log10(other.b)

def create_random_bdlist(b,d):
    bdlist = []
    for branching_dummy in b:
        branching_factor = branching_dummy/10
        for state in d:
            bdlist.append(Quantity(branching_factor,state))
    bdlist.sort()
    return bdlist

def b_power_d_cal(b,d):
    start = time.time()
    dummy = 0
    for i in range (0, int(pow(b,d))):
        dummy+=1
    
    end = time.time() #end time
    return (end - start) * 1000

def b_power_dRunningTime(bdlist): 
    nValues = []	
    tValues = []
    for bd in bdlist:
        nValues.append(pow(bd.b,bd.d))	#store n in this array
        tValues.append(b_power_d_cal(bd.b,bd.d)/100)#store time in this array
    return nValues,tValues

def algorithm_runningTime(bdlist):
    nValues1 = []	
    tValues1 = []
    nValues2 = []	
    tValues2 = []
    for bd in bdlist:
        g = Graph(100,100,bd.d) # We 'Draw' a map in a coordinate system
        mapFlight = g.read_graph()   # read map
        distanceMatrix = g.generateMatrix()    # create distance matrix
        flightPlanMatrix = g.randomFlightPlan(distanceMatrix,bd.b)    # create flight plan matrix
        # intialize map
        startPoint = random.randint(0,bd.d-1)
        endPoint = random.randint(0,bd.d-1)
        # decide start and 
        
        start1 = time.time()#start time
        algorithm.uniform_cost_search(flightPlanMatrix,startPoint,endPoint)#call method
        end1 = time.time() #end time

        start2 = time.time()#start time
        algorithm.a_star_search(flightPlanMatrix,distanceMatrix,startPoint,endPoint)#call method
        end2 = time.time() #end time
        quantity = bd.d*math.log10(bd.b)
        nValues1.append(quantity)
        tValues1.append((end1-start1) * 1000)
        nValues2.append(quantity)
        tValues2.append((end2-start2) * 1000)
    return nValues1,tValues1,nValues2,tValues2


def show_all_time(b = range(50,60,1),d = range(500,1000,10)):
    bdlist = create_random_bdlist(b,d)
    # this is a sorted list of random quantities
    nValues1,tValues1,nValues2,tValues2 = algorithm_runningTime(bdlist)
    # nValues3, tValues3 = b_power_dRunningTime(bdlist) #put value in to the b_power_dRunningTime in b_pow_d page
  
    plt.plot(nValues2, tValues2, color="red", label="A Star Search") #plot a star search running time with red line and a star search lable
    plt.plot(nValues1, tValues1,  color="blue", label="UCS") #plot UCS running time with -- line, blue color and UCS lable
    # plt.plot(nValues3,tValues3,"--",color = "orange" , label = "b^d")
    
    
    plt.xlabel('log10(b^d)') #X represents n
    plt.ylabel('Time(ms)')#Y represents Time(ms)
    plt.title('A star search running time')#Graph title represents A star search running time
    plt.legend()
    plt.show()
