from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        counter = Counter(nums2)
        res = []
        for num in nums1:
            if num in counter and counter[num] > 0:
                res.append(num)
                counter[num] -= 1

        return res


"""
nums1 = [1, 2, 2, 1], nums2 = [2, 2]

counter = {2: 2}

num = 1, res = []
num = 2, res = [2], counter = {2: 1}
num = 2, res = [2, 2], counter = {2: 0}
"""

