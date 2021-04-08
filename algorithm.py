

def a_star_search_algorithm(graph=[[]], heuristic=[[]], start_node=0, end_node=1):
    frontier = [start_node]
    # to store the list of nodes we are about to pop
    explored = [start_node]
    # to store the list of nodes we have explored
    while true:
        if(len(frontier) == 0):
            return None
            # as there is no solution
        current = frontier.pop(0)
        # this is the node of the lowest cost
        if(current == end_node):
            print('found solution')
            return end_node
        # we have the optimal solution
        explored.append(current)
        # add the state of node to the expolored list
        current_node_neighbours = find_neighbours(graph,current)
        for child in current_node_neighbours:
            # now we iterate through all available actions in node
            
            # define child as the successor we are looking at in the iteratoipn
            if(explored.index(child) == -1 and frontier.index(child) == -1):
                frontier.append(child)
                frontier.sort()
                # if child's state is not in frontier or explored then we add it to the frontier
            # else if():
    return None



def find_neighbours(graph,current_node):
    neighbours = []         #create a neighbours matrix to store neighbours
    for i in range(0,len(graph[current_node])):#iterate through a line in the relation matrix
        neighbour = graph[current_node][i]
        if(neighbour>0):
            # then we have a connection
            neighbours.append(i)
    #if the distance is greater than 0, store them in it
    return neighbours