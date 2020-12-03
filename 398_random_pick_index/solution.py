from collections import defaultdict
import random


class Solution:

    def __init__(self, nums):
        self.index = defaultdict(list)
        for i, num in enumerate(nums):
            self.index[num].append(i)

    def pick(self, target):
        return random.choice(self.index[target])


class Solution2:
    """
    Reservoir sampling, does not take extra space.
    """

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, cnt) == 0:
                    # give 1/cnt prob to the new choise, and 1 - 1/cnt to the previous one
                    res = i
                cnt += 1

        return res

