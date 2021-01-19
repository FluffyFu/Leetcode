def path(graph):
    visited = set()
    visited.add(0)

    res = []

    dfs(0, graph, [0], visited, res, len(graph)-1)
    return res


def dfs(v, graph, path, visited, res, target):
    if v == target:
        res.append(path[:])
        return

    for u in graph[v]:
        if u not in visited:
            visited.add(u)
            dfs(u, graph, path + [u], visited, res, target)
            visited.remove(u)

