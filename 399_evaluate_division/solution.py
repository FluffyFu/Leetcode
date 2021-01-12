from collections import defaultdict
from queue import Queue


def evaluate(equations, values, queries):
    graph = defaultdict(list)

    for e, v in zip(equations, values):
        graph[e[0]].append((e[1], v))
        graph[e[1]].append((e[0], 1/v))

    res = []
    for start, end in queries:
        if start not in graph:
            res.append(-1.0)
            continue
        if start == end:
            res.append(1.0)
            continue

        q = Queue()
        visited = set()
        q.put((start, 1))
        visited.add(start)

        reached = False

        while not q.empty():
            cur, prod = q.get()
            if cur == end:
                res.append(prod)
                reached = True
                break
            for v, val in graph[cur]:
                if v not in visited:
                    visited.add(v)
                    q.put((v, prod * val))
        if not reached:
            res.append(-1.0)

    return res

