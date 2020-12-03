import heapq


def kth_smallest(matrix, k):
    hq = [(row[0], i, 0) for i, row in enumerate(matrix)]
    heapq.heapify(hq)

    for _ in range(k-1):
        _, i, j = heapq.heappop(hq)
        if j < len(matrix[0]) - 1:
            heapq.heappush(hq, (matrix[i][j+1], i, j+1))

    return heapq.heappop(hq)[0]
