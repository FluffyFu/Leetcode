def is_bipartite(graph):
    visited = dict()
    flag = 1
    res = [True]

    for i in range(len(graph)):
        if i not in visited:
            dfs(i, graph, visited, flag, res)

    return res[0]


def dfs(node, graph, visited, flag, res):
    visited[node] = flag
    for v in graph[node]:
        if v in visited and visited[v] != -flag:
            res[0] = False
            return
        elif v not in visited:
            dfs(v, graph, visited, flag * (-1), res)

