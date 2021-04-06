from queue import PriorityQueue
class a_star_search:
    def __init__(slef, name)
    def a_star(self,g, start, goal):
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


    def a_star_algorithm(self,g, start, goal):
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