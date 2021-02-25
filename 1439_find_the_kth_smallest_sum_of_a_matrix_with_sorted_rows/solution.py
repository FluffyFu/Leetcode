import heapq


def kth_smallest(mat, k):
    if len(mat) == 1:
        return mat[0][k-1]
    else:
        res = mat[0]
        for i in range(1, len(mat)):
            res = kth_pair_sum2(res, mat[i], k)
    return res[k-1]


def kth_pair_sum(r1, r2, k):
    hq = []
    res = []
    heapq.heappush(hq, (r1[0] + r2[0], 0, 0))
    visited = set((0, 0))

    while len(res) < k and hq:
        cur, p1, p2 = heapq.heappop(hq)
        res.append(cur)
        if p1 < len(r1) - 1 and (p1+1, p2) not in visited:
            heapq.heappush(hq, (r1[p1+1] + r2[p2], p1+1, p2))
            visited.add((p1+1, p2))
        if p2 < len(r2) - 1 and (p1, p2+1) not in visited:
            heapq.heappush(hq, (r1[p1] + r2[p2+1], p1, p2+1))
            visited.add((p1, p2+1))

    return res


def kth_pair_sum2(r1, r2, k):
    hq = []
    res = []

    i = 0
    while i < len(r1) and i < k:
        heapq.heappush(hq, (r1[i] + r2[0], i, 0))
        i += 1

    while len(res) < k and hq:
        cur, p1, p2 = heapq.heappop(hq)
        res.append(cur)

        if p2 < len(r2) - 1:
            heapq.heappush(hq, (r1[p1] + r2[p2+1], p1, p2+1))
    return res

