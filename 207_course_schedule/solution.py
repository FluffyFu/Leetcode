from collections import defaultdict


def can_finish(numCourses, prerequisites):
    # using default dict can avoid key error
    # we only need to add edges.
    graph = defaultdict(list)

    for p in prerequisites:
        graph[p[1]].append(p[0])

    visited = set()
    stack = set()

    for node in range(numCourses):
        if node not in visited:
            if not dfs(node, visited, graph, stack):
                return False

    return True


def dfs(node, visited, graph, stack):
    if node in stack:
        return False
    if node in visited:
        return True
    visited.add(node)
    stack.add(node)
    for v in graph[node]:
        if v not in visited:
            if not dfs(v, visited, graph, stack):
                return False
        elif v in stack:
            return False
    stack.remove(node)
    return True

