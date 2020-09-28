from typing import List


class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        """
        Modify the array in place.
        """
        if not nums:
            return

        for right in range(len(nums)-1, 0, -1):
            for left in range(right - 1, -1, -1):
                if nums[left] < nums[right]:
                    self._shift_array(nums, left, right)
                    return

        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def _shift_array(self, nums, left: int, right: int) -> None:
        temp = nums[right]
        for cur in range(right-1, left-1, -1):
            nums[cur+1] = nums[cur]

        nums[left] = temp

