def find_peak(nums):
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return 0 if nums[0] > nums[1] else 1

    if nums[0] > nums[1]:
        return 0

    if nums[-1] > nums[-2]:
        return len(nums) - 1

    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i


def find_peak_binary(nums):
    l, h = 0, len(nums) - 1

    while l <= h:
        mid1 = (l + h) // 2
        mid2 = mid1 + 1

        if mid2 < len(nums) and nums[mid1] < nums[mid2]:
            l = mid1 + 1
        else:
            h = mid1 - 1

    return l

