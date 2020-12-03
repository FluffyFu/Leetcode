class Solution:
    def serachRange(self, nums, target):
        if not nums:
            return [-1, -1]
        left = self.search_left(nums, target)
        if left == len(nums):
            return [-1, -1]
        right = self.search_right(nums, target)

        if nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]

    def search_left(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def search_right(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right

