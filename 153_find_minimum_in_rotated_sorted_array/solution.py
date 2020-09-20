from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return None
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                return nums[right]

        return nums[right]

