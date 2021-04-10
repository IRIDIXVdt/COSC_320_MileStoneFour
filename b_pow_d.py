import time
import random
import algorithm

class Quantity:
    # Initialize the class for states in UCS
    def __init__(self, b,d):
        self.b = b
        self.d = d
    def __eq__(self, other):    # Compare nodes
        return pow(self.b,self.d) == pow(other.b,other.d)
    def __lt__(self, other): # Sort nodes
         return pow(self.b,self.d) < pow(other.b,other.d)

def b_power_dRunningTime(b = range(30,50,1),d = range(5,10,1)): 
    nValues = []	
    tValues = []
    bdlist = []
    for branching_dummy in b:
        branching_factor = branching_dummy/10
        for state in d:
            bdlist.append(Quantity(branching_factor,state))
    bdlist.sort()
    for bd in bdlist:
        nValues.append(pow(bd.b,bd.d))	#store n in this array
        tValues.append(b_power_d_cal(bd.b,bd.d))#store time in this array
    return nValues,tValues

def b_power_d_cal(b,d):
    start = time.time()
    dummy = 0
    for i in range (0, int(pow(b,d))):
        dummy+=1
    
    end = time.time() #end time
    return (end - start) * 1000

