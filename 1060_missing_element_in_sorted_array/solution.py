
def missing(nums, k):
    cur = nums[0]

    for i in range(1, len(nums)):
        while k > 0 and cur < nums[i]-1:
            cur += 1
            k -= 1
        if k == 0:
            return cur
        else:
            cur = nums[i]

    return cur + k


def missing_bs(nums, k):
    l = 0
    r = len(nums) - 1

    n_miss = (nums[-1] - nums[0] + 1) - len(nums)

    if n_miss < k:
        return nums[-1] + k - n_miss

    while l < r-1:
        mid = (r + l) // 2
        n_miss = num_miss(nums, l, mid)

        if n_miss < k:
            l = mid
            k -= n_miss
        elif n_miss >= k:
            r = mid
    return nums[l] + k


def num_miss(nums, start, end):
    return nums[end] - nums[start] - (end - start)

