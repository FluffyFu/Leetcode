from typing import List


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        """
        Time complexity O(n**2). Although this is faster than O(n**3) solution (brutal force without
        cumulative array), it is still not fast enough to pass the test.
        """
        if not nums:
            return 0
        cum_sum = [0]
        for num in nums:
            cum_sum.append(cum_sum[-1] + num)

        res = 0
        for i in range(len(cum_sum)-1):
            for j in range(i+1, len(cum_sum)):
                if (cum_sum[j] - cum_sum[i]) == k:
                    res += 1
        return res

    def subarray_sum_hash_map(self, nums: List[int], k: int) -> int:
        """
        O(n) solution. While scanning the array, maintain a dictionary maps cumulative sum to
        number of appearance.
        """
        if not nums:
            return 0

        counts_map = {0: 1}
        cum_sum = 0
        res = 0

        for num in nums:
            cum_sum += num
            res += counts_map.get(cum_sum - k, 0)
            counts_map[cum_sum] = counts_map.get(cum_sum, 0) + 1

        return res

