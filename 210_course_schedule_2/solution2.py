from collections import defaultdict
from queue import Queue


def find_order(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for c, p in prerequisites:
        graph[p].append(c)
        indegree[c] += 1

    q = Queue()
    res = []

    for c in range(numCourses):
        if c not in indegree:
            q.put(c)

    while not q.empty():
        cur = q.get()
        res.append(cur)

        for w in graph[cur]:
            indegree[w] -= 1
            if indegree[w] == 0:
                q.put(w)

    return res if len(res) == numCourses else []

