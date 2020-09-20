from typing import List


class Solution:
    def min_subarray_len(self, s: int, nums: List[int]) -> int:
        """
        Two pointer. time complexity: O(N)
        """
        if not nums:
            return 0
        res = float('inf')

        left = 0
        current_sum = 0
        for right in range(len(nums)):
            if current_sum < s:
                current_sum += nums[right]
            while current_sum >= s:
                res = min(right - left + 1, res)
                current_sum -= nums[left]
                left += 1
        return res if res != float('inf') else 0

    def min_subarray_len_binary_search(self, s: int, nums: List[int]) -> int:
        """
        Construct a accumulative sum array and for each element greater than s, apply
        binary search to find the start position. time complexity: O(NlogN)
        """
        accum_sum = [0]
        res = float('inf')
        for num in nums:
            accum_sum.append(accum_sum[-1] + num)

        for i in range(len(accum_sum)):
            if accum_sum[i] < s:
                continue
            # binary search for left side
            left = 0
            right = i - 1
            while left <= right:
                mid = left + (right - left) // 2
                if accum_sum[i] - accum_sum[mid] >= s:
                    res = min(res, i - mid)
                    left = mid + 1
                elif accum_sum[i] - accum_sum[mid] < s:
                    right = mid - 1
        return res if res != float('inf') else 0

