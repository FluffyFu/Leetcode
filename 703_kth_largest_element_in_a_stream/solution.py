import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # only need to keep track of the k-largest
        m = min(len(nums), k)
        self._heap = sorted(nums)[-m:]
        heapq.heapify(self._heap)
        self._k = k

    def add(self, val: int) -> int:
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
            if len(self._heap) == self._k:
                return self._heap[0]
            else:
                return None
        elif val <= self._heap[0]:
            return self._heap[0]
        else:
            heapq.heapreplace(self._heap, val)
            return self._heap[0]
