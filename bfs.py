from collections import defaultdict
import settings as s


def create_graph():
    counter = 1
    graph = defaultdict(list)
    nodes = []
    nodes_pos = {}
    for i in range(s.rect_number):
        tmp = []
        for j in range(s.rect_number):
            tmp.append(counter)
            nodes_pos[counter] = (i, j)
            counter += 1

        nodes.append(tmp)

    for i in range(s.rect_number):
        for j in range(s.rect_number):
            if j - 1 >= 0: graph[nodes[i][j]].append(nodes[i][j - 1])
            if j + 1 < s.rect_number: graph[nodes[i][j]].append(nodes[i][j + 1])
            if i - 1 >= 0: graph[nodes[i][j]].append(nodes[i - 1][j])
            if i + 1 < s.rect_number: graph[nodes[i][j]].append(nodes[i + 1][j])

    return graph, nodes_pos, nodes


def bfs_path():
    queue = []
    queue.append([s.graph[2][s.start[1] // 10][s.start[0] // 10]])
    explored = []
    while queue:
        tmp = queue.pop(0)
        node = tmp[-1]
        if node not in explored:
            for i in s.graph[0][node]:
                path = list(tmp)
                path.append(i)
                queue.append(path)
                if i == s.graph[2][s.end[1] // 10][s.end[0] // 10]:
                    return path
        explored.append(node)


def graph_update():
    for i in s.black_rects:
        if s.graph[2][i[1] // 10][i[0] // 10] in s.graph[0]:
            del s.graph[0][s.graph[2][i[1] // 10][i[0] // 10]]
        for j in s.graph[0].values():
            if s.graph[2][i[1] // 10][i[0] // 10] in j:
                j.remove(s.graph[2][i[1] // 10][i[0] // 10])
