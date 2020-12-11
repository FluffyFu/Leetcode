from collections import defaultdict


def subarray_sum(nums, k):
    cum_s = 0
    seen = defaultdict(int)
    seen[0] = 1
    res = 0

    for num in nums:
        cum_s += num
        res += seen.get(cum_s - k, 0)

        seen[cum_s] += 1
    return res

