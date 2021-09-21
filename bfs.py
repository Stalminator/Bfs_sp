from collections import defaultdict

def create_graph(size):
    counter = 1
    graph = defaultdict(list)
    nodes = []
    nodes_pos = {}
    for i in range(size):
        tmp = []
        for j in range(size):
            tmp.append(counter)
            nodes_pos[counter]=(i,j)
            counter += 1

        nodes.append(tmp)

    for i in range(size):
        for j in range(size):
            if j - 1 >= 0: graph[nodes[i][j]].append(nodes[i][j - 1])
            if j + 1 < size: graph[nodes[i][j]].append(nodes[i][j + 1])
            if i - 1 >= 0: graph[nodes[i][j]].append(nodes[i-1][j])
            if i + 1 < size: graph[nodes[i][j]].append(nodes[i+1][j])

    return graph,nodes_pos,nodes

def bfs_path(graph,start,end):
    queue = []
    queue.append([start])
    explored = []
    while queue:
        tmp = queue.pop(0)
        node = tmp[-1]
        if node not in explored:
            for i in graph[node]:
                path = list(tmp)
                path.append(i)
                queue.append(path)
                if i == end:
                    return path
        explored.append(node)

def graph_update(rects_list,graph,nodes):
    for i in rects_list:
        if nodes[i[1]//10][i[0]//10] in graph:
            del graph[nodes[i[1]//10][i[0]//10]]
        for j in graph.values():
            if nodes[i[1]//10][i[0]//10] in j:
                j.remove(nodes[i[1]//10][i[0]//10])
