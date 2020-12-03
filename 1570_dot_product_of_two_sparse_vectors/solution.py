class SparseVector:
    def __init__(self, nums):
        self.non_zero = set(i for i, num in enumerate(nums) if num != 0)
        self.nums = nums

    def dotProduct(self, vec):
        other_non_zero = vec.non_zero
        other_nums = vec.nums
        overlap = self.non_zero & other_non_zero

        res = 0
        for i in overlap:
            res += self.nums[i] * other_nums[i]

        return res

