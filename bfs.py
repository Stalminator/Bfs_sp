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

    '''
    for i in nodes:
        for j in i:
            print(j,end=' ')
        print()
    '''
    #for i,j in graph.items():
    #    print(i,j)
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

#c,nodes_pos,nodes = create_graph(40)
#w = bfs_path(c,1,399)

a,b,c = create_graph(40)
print(a)

##del a[2]
##w = []
##for i in a.values():
  ##  if 2 in i:
    ##    i.remove(2)

##path = bfs_path(a,1,15)
##print(path)
##for i in path:
  ##  w.append((b[i][1]*10,b[i][0]*10))
#print(a)
print(b)