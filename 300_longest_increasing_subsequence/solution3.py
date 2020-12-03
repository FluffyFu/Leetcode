class Solution:
    def length_of_LIS(self, nums):
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 if nums[j] < nums[i] else 1)

        return max(dp)


"""
nums = [10, 9, 2, 5, 3, 7, 101, 18]
dp = [1, 0, 0, 0, 0, 0, 0, 0]
dp[1] = max(0, 0)
"""
