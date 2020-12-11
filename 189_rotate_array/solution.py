def rotate(nums, k):
    if k == 0:
        return nums
    return nums[-k:] + nums[:-k]


def rotate_in_place(nums, k):
    if k == 0:
        return
    n = len(nums)
    k = k % n

    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

