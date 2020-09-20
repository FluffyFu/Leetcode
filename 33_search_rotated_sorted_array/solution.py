from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        # first find the index of the smallest element

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[right]:
                break

        res1 = self._dfs(nums, 0, right-1, target)
        res2 = self._dfs(nums, right, len(nums)-1, target)

        if res1 == -1 and res2 == -1:
            return -1
        return res1 if res2 == -1 else res2

    def _dfs(self, nums: List[int], left: int, right: int, target: int):
        """
        nums[left, right+1] is sorted. Find the index of the target, if not found return -1
        """

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return -1
