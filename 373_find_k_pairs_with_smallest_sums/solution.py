import heapq
from typing import List


class Solution:
    def k_smallest_pairs_brutal_force(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Time complexity O(m*n*log(k))
        Space complexity O(k)
        """
        if not nums1 or not nums2:
            return []

        heap = []
        for n1 in nums1:
            for n2 in nums2:
                element = (-(n1 + n2), [n1, n2])  # maintain a max heap
                if len(heap) == k and (-(n1 + n2) > heap[0][0]):
                    heapq.heapreplace(heap, element)
                elif len(heap) < k:
                    heapq.heappush(heap, element)

        res = []
        while len(heap) > 0:
            _, element = heapq.heappop(heap)
            res.append(element)

        return res

    def k_smallest_pairs_efficient(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Form a matrix where the i-j element is the sum of nums[i], nums[j]. The next smallest
        element can either be (i+1) - j or i-(j + 1). Maintain a min_heap to keep track of possible
        candidates.
        Time complexity: O(k * log(k))
        Space complexity: O(k)
        """
        if not nums1 or not nums2:
            return []

        heap = []
        res = []
        visited = set()
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while len(heap) > 0 and len(res) < k:
            _, m, n = heapq.heappop(heap)
            res.append([nums1[m], nums2[n]])
            self._add_element(heap, visited, nums1, nums2, m+1, n)
            self._add_element(heap, visited, nums1, nums2, m, n+1)
        return res

    def _add_element(self, heap, visited, nums1, nums2, i, j):
        if i < len(nums1) and j < len(nums2) and (not (i, j) in visited):
            heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
            visited.add((i, j))

