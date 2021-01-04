def find_num(nums, target):
    """
    O(n**2) time complexity
    """
    nums = sorted(nums)

    res = 0
    for l in range(len(nums)):
        if 2 * nums[l] > target:
            break
        for h in range(l, len(nums)):
            if h == len(nums) - 1 and nums[l] + nums[h] <= target:
                res += 2 ** (h - l)
            elif h < len(nums) - 1 and nums[l] + nums[h] <= target and nums[l] + nums[h+1] > target:
                res += 2 ** (h - l)
                break

    return res % (int(10**9) + 7)


def find_num_fast(nums, target):
    nums = sorted(nums)
    if nums[0] * 2 > target:
        return 0

    res = 0

    l, r = 0, len(nums) - 1
    res = 0
    mod = int(10**9) + 1

    while l <= r:
        if nums[l] + nums[r] > target:
            r -= 1
        else:
            res += 2 ** (r - l) % mod
            l += 1

    return res % mod

