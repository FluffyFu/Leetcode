def max_subarray(nums):
    pass


def helper(nums, i):
    """
    max subarray containing i-th element
    """
    if i == 0:
        return nums[0]
    if helper(nums, i-1) > 0:
        return helper(nums, i-1) + nums[i]
    else:
        return nums[i]

