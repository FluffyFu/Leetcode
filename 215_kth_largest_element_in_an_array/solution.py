import heapq
from typing import List


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        hq = []
        for n in nums:
            if len(hq) < k:
                heapq.heappush(hq, n)
            else:
                heapq.heappushpop(hq, n)

        return sorted(hq)[0]
