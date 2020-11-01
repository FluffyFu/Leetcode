class Solution:
    def length_lis(self, nums):
        if not nums:
            return 0
        res = [1]
        self._back_tracking(nums, 0, [], res)

        return res[0]

    def _back_tracking(self, nums, start, path, res):
        if start == len(nums):
            if len(path) > res[0]:
                res[0] = len(path)
            return

        if len(path) + len(nums) - start <= res[0]:
            """
            Pruning those branch cannot exceed current result.
            """
            return

        if not path or path[-1] < nums[start]:
            self._back_tracking(nums, start+1, path + [nums[start]], res)
        self._back_tracking(nums, start+1, path, res)


class Solution2:
    """
    DP, O(n**2) solution.
    """

    def length_lis(self, nums):
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            cur_max = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    cur_max = max(dp[j] + 1, cur_max)
            dp[i] = cur_max
        return max(dp)


class Solution3:
    """
    Keep track of the smallest ending element of different increasing
    subsequence.
    """

    def length_lis(self, nums):
        tails = [0] * len(nums)
        size = 0

        for n in nums:
            low, high = 0, size - 1
            while low <= high:
                mid = low + (high - low) // 2
                if n > tails[mid]:
                    low = mid + 1
                elif n < tails[mid]:
                    high = mid - 1
                else:
                    low = mid
                    break

            tails[low] = n
            size = max(size, low+1)

        return size


"""
[10, 2, 5, 3, 7]
tails = [ 0, 0, 0, 0, 0], size = 0

n = 10, low = 0, high = -1, tails = [10, 0, 0, 0, 0], size = 1
n = 2, low = 0, high = 0, mid = 0, tails = [2, 0, 0, 0, 0], size = 1
n = 5, low = 0, high = 0,
    mid = 0, low = 1, tails = [2, 5, 0, 0, 0], size = 2
n = 3, low = 0, high = 2, mid = 1, high = 0, low = 1, tails = [2, 3, 0, 0, 0], size = 2

n = 7, low = 0, high = 2, low = 2, size = 3

"""
