from collections import defaultdict


def valid(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    if dfs(0, -1, visited, graph) or len(visited) != n:
        return False
    return True


def dfs(v, parent, visited, graph):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            if dfs(u, v, visited, graph):
                return True
        elif u in visited and parent != u:
            return True
    return False
