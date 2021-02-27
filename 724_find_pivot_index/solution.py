def pivot(nums):
    if not nums:
        return -1
    if len(nums) == 1:
        return 0

    cum_sum = [0]
    for i in range(len(nums)):
        cum_sum.append(cum_sum[-1] + nums[i])

    for i in range(1, len(nums)+1):
        if cum_sum[i-1] == cum_sum[-1] - cum_sum[i]:
            return i-1

    return -1

