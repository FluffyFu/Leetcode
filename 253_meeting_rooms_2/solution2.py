import heapq


class Solution:
    def min_meeting_rooms(self, intervals):
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[0])
        pq = []
        heapq.heappush(pq, (intervals[0][1]))
        res = len(pq)

        for m in intervals[1:]:
            if m[0] >= pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, m[1])
            else:
                heapq.heappush(pq, m[1])
                res = max(res, len(pq))
        return res


"""
[2, 4], [7, 10]

pq = [4], res = 1
m = [7, 10], pq = [10]
res = 10

[0, 30], [5, 10], [15, 20]
pq = [30], res = 1
m = [5, 10], pq = [10, 30], res = 2
m = [15, 20], pq = [20, 30]
res = 2
"""

