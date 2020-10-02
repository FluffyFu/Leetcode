from typing import List


class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        """
        Modify the array in place.
        """
        if not nums:
            return
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        if i == 0:
            self._reverse_list(nums, 0, len(nums)-1)
        else:
            for j in range(len(nums) - 1, i-1, -1):
                if nums[i-1] < nums[j]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break
            self._reverse_list(nums, i, len(nums) - 1)

    def _reverse_list(self, nums, left, right):

        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

