from random import randrange


class Solution:
    def __init__(self, w):
        self.cum_sum = [w[0]]
        for i in range(1, len(w)):
            self.cum_sum.append(self.cum_sum[-1] + w[i])

    def pickIndex(self):
        # tricky part: sample from [1, max], instead of [0, max-1].
        # think about simple case w = [1, 3]
        t = randrange(1, self.cum_sum[-1]+1)
        return self.b_search(self.cum_sum, t)

    def b_search(self, nums, target):
        """
        find the smallest index s.t nums[i] >= target
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
        return l


"""
num = [1, 5, 7]
target = 6, should return 2

l = 0, r = 2, mid = 1,
l = 2, r = 2, mid = 2
"""

