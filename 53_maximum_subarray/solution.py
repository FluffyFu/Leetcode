from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        """
        maintain an array dp and dp[i] is the maximum subarray that ends with nums[i].
        Thus:
            dp[i+1] = nums[i+1] if dp[i] <= 0
                    = nums[i+1] + dp[i] if dp[i] > 0
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]

        return max(dp)

    def max_sub_array_less_space(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        pre = nums[0]

        for cur in nums[1:]:
            if pre < 0:
                pre = cur
            else:
                pre = cur + pre

            max_sum = max(max_sum, pre)

        return max_sum
