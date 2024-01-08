def astarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                temp_g = g[n] + weight
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    g[m] = temp_g
                    parents[m] = n
                else:
                    if g[m] > temp_g: 
                        g[m] = temp_g
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n is None:
            print("Path does not exist")
            return None

        if n == stop_node:
            path = []
            while n != start_node:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            return path

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist")
    return None

def get_neighbors(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 8}
    return H_dist[n]

graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)]
}

astarAlgo('A', 'G')
