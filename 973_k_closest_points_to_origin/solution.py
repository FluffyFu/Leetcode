import heapq


class Solution:
    def k_closest(self, points, k):
        """
        Time complexity is O(NlogN)
        """
        pq = []
        for p in points:
            heapq.heappush(pq, (p[0]**2 + p[1]**2, p))

        res = []
        while k > 0:
            res.append(heapq.heappop(pq)[1])
            k -= 1

        return res

    def k_closest_clean(self, points, k):
        """
        maintain the priority queue size to be k.
        """
        pq = []
        for p in points:
            if len(pq) == k:
                heapq.heappushpop(pq, (-(p[0]**2 + p[1]**2), p))
            else:
                heapq.heappush(pq, (-(p[0]**2 + p[1]**2), p))

        return [p for _, p in pq]
