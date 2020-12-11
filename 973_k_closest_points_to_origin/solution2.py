import heapq


def k_close_point(points, k):
    hq = []
    for x, y in points:
        dist = x**2 + y**2
        if len(hq) <= k:
            heapq.heappush(hq, (-dist, x, y))
        else:
            heapq.heappushpop(hq, (-dist, x, y))

    _, x, y = heapq.heappop(hq)

    return [[x, y] for _, x, y in hq]

