def max_subarray(nums):
    if not nums:
        return None
    res = nums[0]
    cum = 0

    for n in nums:
        if cum > 0:
            cum += n
        else:
            cum = n

        res = max(res, cum)

    return res

