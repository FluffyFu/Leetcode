def product(nums):
    if len(nums) < 2:
        return None
    res = [1]

    for n in nums[:-1]:
        res.append(res[-1] * n)

    i = len(nums) - 1
    cum_p = 1

    while i >= 0:
        res[i] *= cum_p
        cum_p *= nums[i]
        i -= 1

    return res

