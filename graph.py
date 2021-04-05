import random
import math
#map size(x*y)
    rangeX = 100
    rangeY = 100
    qty = 5 # or however many points you want
# and the matrix of distance will also be qty by qty
#random vertex
    openfile = open('file.txt','w')
    for x in random.sample(range(rangeX*rangeY),qty):
      openfile.write(str('{},{}'.format(*divmod(x,rangeX)))+ '\n')
    #print('{},{}'.format(*divmod(x,rangeX)))

    openfile.close()
    cell_array = [[]]
    with open('file.txt','r') as file:
        line_array = file.read().splitlines()
        cell_array = [line.split(',') for line in line_array]

        print (cell_array)
    cell_array2 = [list(map (int,i)) for i in cell_array]


# （2. 这个先不着急 但是这个随机的分布 真的没问题么 我觉得按照一个模拟现实的地图 
    # 中间会更加密集 四周会疏散 你现在的地图多半每个点出现城市的几率是相同的）

# print (cell_array2)


    for node in cell_array2:
        print(node)


def calDistance( p1, p2 ):
        return round(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ),3)
   
def removePair( map, i, j):
    # we remove a flight availabe between city index i and j
        map[i][j]=-1
        map[j][i]=-1
   

distanceMap = []
# index corresponds to the order we have in cell_array
# in other words, the distance between city index i,j in cell_array will be in distanceMap[i][j]

for node in cell_array2:
    distanceArray = []
    for node2 in cell_array2:
        # print(calDistance( node, node2 ))
        distanceArray.append(calDistance( node, node2 ))# iterate through each pair of node and compute distances
    distanceMap.append(distanceArray)

print(distanceMap)
# now we have the distanceMap ready
removePair(distanceMap,2,3)

print(distanceMap)

def randomFlightPlan( map, branchingFactor, qty):
    # we first create a copy of the array
    
    # notice that the original branching factor would be qty-1
    chance = branchingFactor/(qty-1)
    print(chance)
    for i in range(0,qty):
        for j in range(i,qty):
            target = random.random()
            if (target<chance):
                removePair(map,i,j)


randomFlightPla


    
