from typing import List


class Solution:
    def move_zeros(self, nums: List[int]) -> None:
        if not nums:
            return
        slow = 0

        while slow < len(nums) and nums[slow] != 0:
            slow += 1

        if slow == len(nums):
            return

        fast = slow + 1
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
