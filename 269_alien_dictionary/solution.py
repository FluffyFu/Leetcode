from collections import defaultdict
import collections
from queue import Queue


def alien_order(words):
    flag, graph, indegree, chars = build_graph(words)
    if flag:
        return ''

    res = []
    q = Queue()
    for c in chars:
        if c not in indegree:
            q.put(c)

    while not q.empty():
        cur = q.get()
        res.append(cur)
        for v in graph[cur]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.put(v)

    return ''.join(res) if len(res) == len(chars) else ''


def build_graph(words):
    indegree = defaultdict(set)
    graph = defaultdict(set)
    chars = set(''.join(words))
    flag = False

    for i in range(len(words)-1):
        found = False
        for c1, c2 in zip(words[i], words[i+1]):
            if c1 != c2:
                graph[c1].add(c2)
                indegree[c2].add(c1)
                found = True
                break
        if found == False and len(words[i]) > len(words[i+1]):
            flag = True

    indegree = {key: len(val) for key, val in indegree.items()}
    return flag, graph, indegree, chars
