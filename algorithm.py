

def a_star_search_algorithm(graph,heuristic,start=0,end):
    frontier = {}
    # to store the list of nodes we are about to pop
    explored = {}
    # to store the list of nodes we have explored
    while true:
        if(len(frontier) == 0):
            return None
            # as there is no solution
        current = frontier.pop(0)
        # this is the node of the lowest cost
        if(current == end):
            print('found solution')
            return end
        # we have the optimal solution
        explored.append(current)
        
    return None



def find_neighbours(graph,current_node):
    a = graph[current_node]
    neighbours = []
    for i in range (len(a)):
        if a[i] > 0:
            append.neighbours(i)


    return neighbours