from collections import defaultdict
from queue import Queue


def reconstruct(org, seqs):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    org_nodes = set(org)
    nodes = set()

    for s in seqs:
        nodes = nodes | set(s)
        if len(s) == 1:
            continue
        for i in range(len(s)-1):
            graph[s[i]].append(s[i+1])
            indegree[s[i+1]] += 1

    if nodes - org_nodes:
        return False

    q = Queue()
    res = []

    for e in nodes:
        if e not in indegree:
            q.put(e)

    while not q.empty():
        if q.qsize() > 1:
            return False
        cur = q.get()
        res.append(cur)

        for w in graph[cur]:
            indegree[w] -= 1
            if indegree[w] == 0:
                q.put(w)

    return res == org

