from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        If a house is not robbed, we can break the circle from there and
        it simplified to a linear problem see house robber 1.

        Since no two consecutive houses can be robber, the problem can
        be simplified to
            1. 0 is not robbed
            2. n-1 is not robbed
        Note, there is an intersection between these two cases (both 0 and n-1 are not robbed).
        There are some redundancy. But it is okay, since we are calculating the max.
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob_a_line(nums, 1, len(nums)-1),
                   self.rob_a_line(nums, 0, len(nums)-2))

    def rob_a_line(self, nums, low, high):
        if low > high:
            return 0
        if low == high:
            return nums[low]
        pre_2 = nums[low]
        pre_1 = max(nums[low + 1], nums[low])

        for i in range(low+2, high+1):
            temp = pre_1
            pre_1 = max(nums[i] + pre_2, pre_1)
            pre_2 = temp

        return pre_1

    def rob_no_intersection(self, nums):
        """
        We can also divide the problem into if 0-th house has been robbed.
            1. 0-th not robbed, search [1, n-1]
            2. 0-th robbed, search [2, n-2] + nums[0]
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob_a_line(nums, 1, len(nums)-1),
                   nums[0] + self.rob_a_line(nums, 2, len(nums)-2))

