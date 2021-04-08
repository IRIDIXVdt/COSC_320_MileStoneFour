import random
import math
class Graph:
    def __init__(self,rangeX,rangeY,qty):
        self.rangeX = rangeX
        self.rangeY = rangeY
        self.qty = qty
        openfile = open('file.txt','w')
        for x in random.sample(range(self.rangeX*self.rangeY),self.qty):
            openfile.write(str('{},{}'.format(*divmod(x,self.rangeX)))+ '\n')
        openfile.close()
    
    def read_graph(self):    
        cell_array = [[]]
        with open('file.txt','r') as file:
            line_array = file.read().splitlines()
            cell_array = [line.split(',') for line in line_array]
        cell_array2 = [list(map (int,i)) for i in cell_array]
        # print(cell_array2)
        return cell_array2
    
    def calDistance(self,p1,p2):
        return round(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ),3)
   
    def removePair(self, mapInput, i, j):
    # we remove a flight availabe between city index i and j
        mapInput[i][j]=-1
        mapInput[j][i]=-1
   
    def generateMatrix(self):
        distanceMap = []
# index corresponds to the order we have in cell_array
# in other words, the distance between city index i,j in cell_array will be in distanceMap[i][j]
        cell_array2 = self.read_graph()
        for node in cell_array2:
            distanceArray = []
            for node2 in cell_array2:
        # print(calDistance( node, node2 ))
                distanceArray.append(self.calDistance( node, node2 ))# iterate through each pair of node and compute distances
            distanceMap.append(distanceArray)
        return distanceMap

# print(distanceMap)
# now we have the distanceMap ready
# removePair(distanceMap,2,3)

# print(distanceMap)

    def randomFlightPlan(self,mapInput, branchingFactor):
    # we first create a copy of the array
        mapCopy = []
        for line in mapInput:
            newline = []
            for element in line:
                newline.append(element)
            mapCopy.append(newline)
    # print(mapCopy)
    # print(mapInput)
    # notice that the original branching factor would be qty-1
        chance = branchingFactor/self.qty# this is the chance we need to remove the node 
    # oldBranchNumber = (qty+1)*qty
    # newBranchNumber = (qty+1)*branchingFactor
        print('chance is : ', chance)
        for i in range(1,self.qty):
            for j in range(0,i):
                target = random.random()
            # print('The current pair is: ', i ,j)
                if (target>chance):
                    self.removePair(mapCopy,i,j)
    # print(mapCopy)
        return mapCopy
    def calBF(self,mapInput):
        existBranch = 0
        for line in mapInput:
            for element in line:
                if (element>0):
                    existBranch+=1
        print('exist branch number is: ',existBranch)
        branchingFactor = existBranch/(self.qty)
        print('branching factor is :', branchingFactor)
    