from collections import defaultdict
import heapq


def cheapest(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, p in flights:
        graph[u].append((v, p))

    hq = [(0, src, k)]

    while hq:
        pre_p, u, k = heapq.heappop(hq)
        if u == dst:
            return pre_p
        if k >= 0:
            for v, p in graph[u]:
                heapq.heappush(hq, (p + pre_p, v, k-1))

    return -1

