import random
from queue import PriorityQueue

from graph2 import Graph


#def heuristic(goal, nbr):
    #return abs(goal - nbr.get_id())



if __name__ == "__main__":
    # Using the insertion method to generate the graph
    g = Graph(1000,1000,10)
    g.generate_graph()
    #for i in range(6):
    #g.add_vertex(i)
    #g.add_edge(0, 1, 5)
    #g.add_edge(0, 5, 2)
    #g.add_edge(1, 2, 4)
    #g.add_edge(2, 3, 9)
    #g.add_edge(3, 4, 7)
    #g.add_edge(3, 5, 3)
    #g.add_edge(4, 0, 1)
    #g.add_edge(5, 4, 8)
    #g.add_edge(5, 2, 1)

    

    # Randomly generate the graph
    # for v in g:
    #         for w in v.get_connections():
    #             print("(%s, %s)  the cost/weight: %s  %s" % (v.get_id(), w.get_id(), v.get_weight(w), v.get_id()))

    
    
    