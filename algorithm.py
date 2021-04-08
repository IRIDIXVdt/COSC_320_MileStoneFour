

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
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                current_node = graph[i][j]
            if graph[i][j] > 0:
                

    neighbours = {}

    return neighbours