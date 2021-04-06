import random
from queue import PriorityQueue
from graph2 import Graph


#def heuristic(goal, nbr):
    #return abs(goal - nbr.get_id())



if __name__ == "__main__":
    # Using the insertion method to generate the graph
    g = Graph(10,10,5)
   
    # read map
    mapFlight = g.read_graph()
    # create distance matrix
    distanceMatrix = g.generateMatrix()
    # create flight plan matrix
    flightPlanMatrix = g.randomFlightPlan(distanceMatrix,3)

    print(flightPlanMatrix)
    #兄弟今天我没法跟你meeting了，我这边360的队友们找我meeting写code
    #关于nodes的想法：找到每个key。我感觉用matrix的index就可行 然后把哪个点与哪个点之间有连线 类似于1->2,3 2->5这种我没想到怎么实现它或者我整个的思路就有问题
    # https://www.annytab.com/a-star-search-algorithm-in-python/ 这个是我在网上找的例子
    #
    for i in range(len(flightPlanMatrix)):
        for j in range(len(flightPlanMatrix[i])):
            if flightPlanMatrix[i][j] == 0:
                a = j+1
                print(a)
            if flightPlanMatrix[i][j] > 0:
                b = j+1
                print(b)
    g.calBF(flightPlanMatrix)

    
    