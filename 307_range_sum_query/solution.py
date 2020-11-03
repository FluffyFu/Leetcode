class NumArray:
    def __init__(self, nums):
        self._nums = nums
        self._cum_sum = [0 for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            res += self._nums[i]
            self._cum_sum[i] = res

    def update(self, i, val):
        """
        Worst case O(n).
        """

        for j in range(i, len(self._nums)):
            self._cum_sum[j] = self._cum_sum[j] - self._nums[i] + val
        self._nums[i] = val

    def sumRange(self, i, j):
        """
        O(1)
        """
        return self._cum_sum[j] - self._cum_sum[i-1] if i - 1 >= 0 else self._cum_sum[j]
