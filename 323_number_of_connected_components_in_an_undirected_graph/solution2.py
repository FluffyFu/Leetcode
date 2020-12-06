from collections import defaultdict
from queue import Queue


def num_cc(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    n_cc = 0
    q = Queue()
    visited = set()

    for i in range(n):
        if i not in visited:
            q.put(i)
            visited.add(i)
            while not q.empty():
                cur = q.get()
                for v in graph[cur]:
                    if v not in visited:
                        visited.add(v)
                        q.put(v)

            n_cc += 1
    return n_cc

