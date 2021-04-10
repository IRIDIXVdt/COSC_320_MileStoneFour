class State:
    # Initialize the class for states in UCS
    def __init__(self, index,parent_index, optimal_path_cost):
        self.index = index
        self.parent_index = parent_index
        self.optimal_path_cost = optimal_path_cost
    def __eq__(self, other):    # Compare nodes
        return self.optimal_path_cost == other.optimal_path_cost
    def __lt__(self, other): # Sort nodes
         return self.optimal_path_cost < other.optimal_path_cost

class State_A_Star:
    # Initialize the class for states in A star
    def __init__(self, index,parent_index, optimal_path_cost, heuristic_cost):
        self.index = index
        self.parent_index = parent_index
        self.optimal_path_cost = optimal_path_cost
        self.heuristic_cost = heuristic_cost
    def __eq__(self, other):    # Compare nodes
        return (self.optimal_path_cost + self.heuristic_cost)== (other.optimal_path_cost+other.heuristic_cost)
    def __lt__(self, other): # Sort nodes
         return (self.optimal_path_cost + self.heuristic_cost) < (other.optimal_path_cost+other.heuristic_cost)

def find_neighbours(graph,current_node):
    neighbours = []         #create a neighbours matrix to store neighbours
    for i in range(0,len(graph[current_node])):#iterate through a line in the relation matrix
        bridge = graph[current_node][i]
        if(bridge>0):
            # then we have a connection
            neighbours.append(i)
    #if the distance is greater than 0, store them in it
    # print('current_node is: ',current_node)
    # print('neighbours are: ',neighbours)
    return neighbours

def in_array(frontier,state):
    # for i in frontier:
    #     if(i.index == index):
    #         return i
    # return None
    # we return the index given state
    for i in range(0,len(frontier)):
        if(frontier[i].index == state):
            return i
    return -1
    # if we do not have a result, we return -1

def update_optimal_solution(graph,frontier,solution_map,cost_map,parent,child):
    # now find the distance cost between parent and child
    # print('try to insert optimal solution now:',parent,child)
    cost = graph[parent][child]
    # find the optimal path cost to child
    optimal_cost = cost+cost_map[parent]
    frontier_node_index = in_array(frontier,child)
    if(frontier_node_index != -1):
        if(frontier[frontier_node_index].optimal_path_cost>optimal_cost):
            # print('---------------------We update the frontier',frontier[frontier_node_index].optimal_path_cost,optimal_cost)
            frontier[frontier_node_index].optimal_path_cost=optimal_cost
            frontier[frontier_node_index].parent_index = parent
    elif(frontier_node_index == -1):
        # print('We append to frontier')
        frontier.append(State(child,parent,optimal_cost))   
    frontier.sort()    

def update_optimal_solution_A_Star(graph,heuristic,frontier,solution_map,cost_map,parent,child,end_node):
    cost = graph[parent][child]
    new_optimal_cost = cost+cost_map[parent]
    new_h_cost = new_optimal_cost+heuristic[child][end_node]
    frontier_node_index = in_array(frontier,child)
    if(frontier_node_index != -1):
        old_h_cost = frontier[frontier_node_index].optimal_path_cost + frontier[frontier_node_index].heuristic_cost
        if(old_h_cost>new_h_cost):
            # we update the node
            frontier[frontier_node_index].optimal_path_cost=new_optimal_cost
            frontier[frontier_node_index].heuristic_cost=heuristic[child][end_node]
            frontier[frontier_node_index].parent_index = parent
    elif(frontier_node_index == -1):  
        frontier.append(State_A_Star(child,parent,new_optimal_cost,heuristic[child][end_node]))  
    frontier.sort()    


def uniform_cost_search(graph=[[]], start_node=0, end_node=1):
    print('We start from',start_node,'and try to find how to get to',end_node)
    frontier = [State(start_node,start_node,0)]# to store the list of nodes we are about to pop
    # explored = []# to store the list of nodes we have explored
    
    solution_map = []
    cost_map = []
    for line in graph:
        cost_map.append(-1)
        solution_map.append("from: ")
    # the two arrays above tracks the costs and solution
    # solution_map[start_node]+= str(start_node)+' -> '

    while True:
        if(len(frontier) == 0):
            print('No solution from UCS')
            return False # as there is no solution
        current_node = frontier.pop(0)# this is the node of the lowest cost
        # print('now we pop ',current_node.index)
        # print('list is like this ', len(frontier))
        current = current_node.index
        
        cost_map[current] = current_node.optimal_path_cost
        if(current_node.parent_index != None):
            solution_map[current]= solution_map[current_node.parent_index]+' -> '+str(current)
        # add the state of node to the expolored list

        if(current == end_node):
            # print('found solution with UCS')
            # print('Path cost is: ', current_node.optimal_path_cost)
            # print('Path is ',solution_map[current])
            return True
        # we have the optimal solution
        # explored.append(current)

        current_node_neighbours = find_neighbours(graph,current)
        parent = current #for clarity, we call this parent now
        for child in current_node_neighbours:
            # now we iterate through all available actions in node
            
            # define child as the successor we are looking at in the iteratoipn
            if(cost_map[child] == -1):#not in the cost map list means we do not have its op sol'n, and not in the explored list
                # we handle everything in update optimal solution
                update_optimal_solution(graph,frontier,solution_map,cost_map,parent,child)

def a_star_search(graph=[[]], heuristic=[[]], start_node=0, end_node=1):
    # it is very similar to UCS, so I will not put redundant comments here
    frontier = [State_A_Star(start_node,start_node,0,heuristic[start_node][end_node])]
    solution_map = []
    cost_map = []
    for line in graph:
        cost_map.append(-1)
        solution_map.append("from: ")

    while True:
        if(len(frontier) == 0):
            print('No solution from A Star Search')
            return False 
        current_node = frontier.pop(0)
        current = current_node.index
        
        cost_map[current] = current_node.optimal_path_cost
        if(current_node.parent_index != None):
            solution_map[current]= solution_map[current_node.parent_index]+' -> '+str(current)

        if(current == end_node):
            # print('found solution with A Star Search')
            # print('Path cost is: ', current_node.optimal_path_cost)
            # print('Path is ',solution_map[current])
            return True

        current_node_neighbours = find_neighbours(graph,current)
        parent = current 
        for child in current_node_neighbours:
            if(cost_map[child] == -1):
                update_optimal_solution_A_Star(graph,heuristic,frontier,solution_map,cost_map,parent,child,end_node)
                # notice that the update function is different
                # it is because we are using different evaluations
def b_power_d(b,d):
    dummy = 0
    for i in range(0, pow(b,d)):
        dummy +=1


            
            
            
            





