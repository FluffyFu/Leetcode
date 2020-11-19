class Solution:
    def search_range(self, nums, target):
        if not nums:
            return [-1, -1]

        left = self.search_left(nums, target)
        right = self.serach_right(nums, target)

        return [left, right] if left <= right else [-1, -1]

    def search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def serach_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right


"""
[5, 7, 7, 8, 8, 10], target = 6
search left:
    left = 0, right = 5, mid = 2
    left = 0, right = 1, mid = 0
    left = 1, right = 1, mid = 1
    left = 1, right = 0, return -1

serach right:
    left = 0, right = 5, mid = 2
    left = 0, right = 1, mid = 0
    left = 1, right = 1, mid = 1
    left = 1, right = 0, return -1
[5, 7, 7, 8, 8, 10], target = 8
serach_left:
    left = 0, right = 5, mid = 2
    left = 3, right = 5, mid = 4
    left = 3, right = 4, mid = 3
    left = 3, right = 3, mid = 3
    left = 3, right = 2
    return 3
serach right:
    left = 0, right = 5, mid = 2
    left = 3, right = 5, mid = 4
    left = 4, right = 5, mid = 4
    left = 5, right = 5, mid = 5
    left = 5, right = 4
"""
