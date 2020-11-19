class Solution:
    """
    O(n**2) solution
    """

    def check_subarray_sum(self, nums, k):
        if len(nums) < 2:
            return False
        cum_sum = [0]
        for n in nums:
            cum_sum.append(cum_sum[-1] + n)

        for i in range(len(cum_sum) - 2):
            for j in range(i+2, len(cum_sum)):
                if k != 0 and (cum_sum[j] - cum_sum[i]) % k == 0:
                    return True
                elif k == 0 and cum_sum[j] - cum_sum[i] == 0:
                    return True

        return False

    def check_subarray_sum_fast(self, nums, k):
        """
        O(n) solution. Calculate cum_sum mod k, if there is any duplicates in
        the cum_sum, there will be a hit.
        """
        if len(nums) < 2:
            return False
        if k == 0:
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
        collection = {0: -1}
        acc = 0
        for i, n in enumerate(nums):
            acc = (n + acc) % k

            if acc in collection and i - collection[acc] > 1:
                return True
            elif acc not in collection:
                collection[acc] = i

        return False


"""
[0, 0], -1
collection = {0: -1}
i = 0, n = 0, acc = 0
[2, 2] k = 0

[23, 2, 1, 6, 7] k = 9
collection = {}, acc = 0
n = 23, acc = 5, collection = {5}
n = 2, acc = 7, collection = {5, 7}
n = 1, acc = 8, collection = {5, 7, 8}
n = 6, acc = 5, return True
"""
