def sorted_square(nums):
    res = []

    l, h = 0, len(nums) - 1

    while l <= h:
        if abs(nums[l]) < abs(nums[h]):
            res.append(nums[h]**2)
            h -= 1
        else:
            res.append(nums[l]**2)
            l += 1

    return res[::-1]

