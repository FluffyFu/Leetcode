from typing import List


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        """
        maintain a array dp whose i-th element is the length of the longest increasing substring
        in nums[:i+1] and must contain nums[i], the dynamic programming relation is:

        dp[i] = max(dp[j]) + 1 where j < i and nums[j] < nums[i]
        """
        if not nums:
            return 0

        dp = [0] * (len(nums))
        dp[0] = 1

        for i in range(1, len(nums)):
            cur_max = 0
            for j in range(i, -1, -1):
                if nums[i] > nums[j]:
                    cur_max = max(cur_max, dp[j])
            dp[i] = cur_max + 1

        return max(dp)
