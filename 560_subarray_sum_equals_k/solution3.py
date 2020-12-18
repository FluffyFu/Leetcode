from collections import defaultdict


def subarray_sum_k(nums, k):
    cum_sum_cnt = defaultdict(int)
    cum_sum_cnt[0] = 1
    cum_sum = 0
    res = 0
    for num in nums:
        cum_sum += num
        res += cum_sum_cnt[cum_sum - k]
        cum_sum_cnt[cum_sum] += 1
    return res

