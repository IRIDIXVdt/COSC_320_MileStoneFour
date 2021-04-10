import time
import random
import algorithm
import matplotlib
import matplotlib.pyplot as plt

class Quantity:
    def __init__(self, b,d):
        self.b = b
        self.d = d
    def __eq__(self, other):    # Compare nodes
        return pow(self.b,self.d) == pow(other.b,other.d)
    def __lt__(self, other): # Sort nodes
         return pow(self.b,self.d) < pow(other.b,other.d)

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

def b_power_dRunningTime(b,d): 
    nValues = []	
    tValues = []
    for bd in create_random_bdlist(b,d):
        nValues.append(pow(bd.b,bd.d))	#store n in this array
        tValues.append(b_power_d_cal(bd.b,bd.d))#store time in this array
    return nValues,tValues




def show_all_time(distanceMatrix,flightPlanMatrix,b = range(30,50,1),d = range(5,10,1)):

    nValues3, tValues3 = b_power_dRunningTime(b,d) #put value in to the b_power_dRunningTime in b_pow_d page
  
        # plt.plot(nValues, tValues, color="red", label="A Star Search") #plot a star search running time with red line and a star search lable
    # plt.plot(nValues2, tValues2, "--", color="blue", label="UCS") #plot UCS running time with -- line, blue color and UCS lable
    plt.plot(nValues3,tValues3,color = "orange" , label = "b_pow_d")
    
    
    plt.xlabel('b^d') #X represents n
    plt.ylabel('Time(ms)')#Y represents Time(ms)
    plt.title('A star search running time')#Graph title represents A star search running time
    plt.legend()
    plt.show()
