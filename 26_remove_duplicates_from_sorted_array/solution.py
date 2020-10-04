from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        fast = 0

        while fast < len(nums):
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1

            if fast == len(nums):
                break
            slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1

        return slow + 1
