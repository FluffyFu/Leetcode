from collections import defaultdict


def find_order(numCourses, prerequisites):
    graph = build_graph(numCourses, prerequisites)

    if has_cycle(numCourses, graph):
        return []

    res = []
    visited = set()
    for i in range(numCourses):
        if i not in visited:
            post_order(graph, i, visited, res)

    return res[::-1]


def post_order(graph, v, visited, res):
    visited.add(v)

    for w in graph[v]:
        if w not in visited:
            post_order(graph, w, visited, res)

    res.append(v)


def build_graph(numCourses, prerequisites):
    graph = defaultdict(list)

    for p in prerequisites:
        graph[p[1]].append(p[0])

    return graph


def has_cycle(n, graph):
    visited = set()
    stack = set()
    flag = [False]

    for i in range(n):
        if i not in visited:
            dfs(graph, i, visited, stack, flag)

    if flag[0]:
        return True
    return False


def dfs(graph, v, visited, stack, flag):
    stack.add(v)
    visited.add(v)

    for w in graph[v]:
        if w in stack:
            flag[0] = True
        elif w not in visited:
            dfs(graph, w, visited, stack, flag)
    stack.remove(v)
