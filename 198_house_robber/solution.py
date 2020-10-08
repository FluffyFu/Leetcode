from typing import List

"""
nums = [8, 1, 2, 3]
dp = [8, 1]

i = 2, c1 = 10, c2 = 0

dp = [8, 1, 10]

i = 3, c1 = 4, c2 = 11
dp = [8, 1, 10, 11]

nums = [1, 4, 1]
dp = [1, 4]

i = 2, c1 = 2, c2 = 0
dp = [1, 4, 2]

"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] is maximum sum contain nums[i]
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            c1 = dp[i-2] + nums[i]
            c2 = dp[i-3] + nums[i] if i - 3 >= 0 else 0
            dp[i] = max(c1, c2)

        return max(dp[-1], dp[-2])

    def rob_2(self, nums: List[int]) -> int:
        """
        dp[i] is the maximum sum for nums[:i+1], it does not necessarily
        contains nums[i].
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]

    def rob_2_space_efficient(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        pre_2, pre_1 = nums[0], max(nums[:2])

        for num in nums[2:]:
            temp = pre_1
            pre_1 = max(num + pre_2, pre_1)
            pre_2 = temp

        return pre_1

    def rob_recursive(self, nums: List[int]) -> int:

        def recursive(nums, i, cache):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i in cache:
                return cache[i]
            else:
                cache[i] = max(recursive(nums, i-2, cache) + nums[i],
                               recursive(nums, i-1, cache))
                return cache[i]

        return recursive(nums, len(nums)-1, {})

