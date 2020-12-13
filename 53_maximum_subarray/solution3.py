def max_subarray(nums):
    if len(nums) < 2:
        return nums[0]
    pre = nums[0]
    res = pre
    for cur in nums[1:]:
        if pre > 0:
            pre += cur
        else:
            pre = cur

        res = max(res, pre)

    return res

