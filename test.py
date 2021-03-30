import random
from queue import PriorityQueue

from graph import Graph


def generate_graph(num_vertices, max_num_edge, max_weight):
    # We will abandon this method due to some of its deficiencies
    """
    Randomly generate the graph
    :param num_vertices: vertex numverss
    :param max_num_edge: maximum number of edges
    :param max_weight: maximum weight
    :return: the generated graph
    """
    g = Graph()
    check_dict = {}
    for i in range(num_vertices):
        g.add_vertex(i)
        check_dict[str(i)] = []
    for i in range(num_vertices):
        index = 0
        while index == 0:
            # print(index)
            for j in range(random.choice([i for i in range(num_vertices)])):
                if j != i and j not in check_dict.get(str(i)) and i not in check_dict.get(str(j)):
                    check_dict[str(i)].append(j)
                    g.add_edge(i, j, random.randint(1, max_weight))
                    index += 1
    print(check_dict)
    return g


def generate_graph(num_verticies,branching_factor,size_of_map):
    """
    Randomly generate the graph
    :param num_vertices: vertex numverss
    :param max_num_edge: maximum number of edges
    :param max_weight: maximum weight
    :return: the generated graph
    """
    g = Graph()

    return g

#def heuristic(goal, nbr):
    #return abs(goal - nbr.get_id())


def a_star(g, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    visted = []
    while not frontier.empty():
        current = frontier.get()
        visted.append(current)
        if goal == current:
            break
        for nbr in g.get_vertex(current).get_connections():
            print(current, nbr)
            new_cost = cost_so_far[current] + g.get_vertex(current).get_weight(nbr)
            if nbr.get_id() not in cost_so_far.keys() or new_cost < cost_so_far[nbr.get_id()]:
                cost_so_far[nbr.get_id()] = new_cost
                # priority = new_cost + heuristic(goal, nbr)
                priority = new_cost
                frontier.put(nbr.get_id(), priority)
                came_from[nbr.get_id()] = current
    print("cost_so_far", cost_so_far, cost_so_far.keys())
    print("came_from", came_from)

    res = [start]
    while True:
        find = False
        for k, v in came_from.items():
            # print(k, v)
            if res[-1] == v:
                res.append(k)
                find = True
        if find:
            continue
        if res[-1] == goal:
            break
        else:
            came_from.pop(res[-1])
            res.pop(-1)

    print(res)
    # return res


def a_star_algorithm(g, start, goal):
    open_lst = set([start])
    closed_lst = set([])
    poo = {start: 0}
    par = {start: start}
    while len(open_lst) > 0:
        n = None
        for v in open_lst:
            if n is None or poo[v] < poo[n]:
                n = v
        if n is None:
            print('Path does not exist!')
            return None

        if n == goal:
            reconst_path = []
            while par[n] != n:
                reconst_path.append(n)
                n = par[n]
            reconst_path.append(start)
            reconst_path.reverse()
            print('Path found: {}'.format(reconst_path))
            return reconst_path

        for nbr in g.get_vertex(n).get_connections():

            if nbr.get_id() not in open_lst and nbr.get_id() not in closed_lst:
                open_lst.add(nbr.get_id())
                par[nbr.get_id()] = n
                poo[nbr.get_id()] = poo[n] + g.get_vertex(n).get_weight(nbr)
            else:
                if poo[nbr.get_id()] > poo[n] + g.get_vertex(n).get_weight(nbr):
                    poo[nbr.get_id()] = poo[n] + g.get_vertex(n).get_weight(nbr)
                    par[nbr.get_id()] = n

                    if nbr.get_id() in closed_lst:
                        closed_lst.remove(nbr.get_id())
                        open_lst.add(nbr.get_id())

        open_lst.remove(n)
        closed_lst.add(n)

    return None


if __name__ == "__main__":
    # Using the insertion method to generate the graph
    g = Graph()
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
    g = generate_graph(1000, 3, 9)
    # for v in g:
    #         for w in v.get_connections():
    #             print("(%s, %s)  the cost/weight: %s  %s" % (v.get_id(), w.get_id(), v.get_weight(w), v.get_id()))

    
    a_star_algorithm(g, 10 ,511)
    