def search(nums, target):
    if nums[0] < nums[-1]:
        return b_search(nums, 0, len(nums)-1, target)

    # find the pivot point. the smallest element in the array.
    l, h = 0, len(nums) - 1
    while l <= h:
        mid = l + (h - l) // 2
        if nums[mid] > nums[h]:
            l = mid + 1
        elif nums[mid] < nums[h]:
            # this part is different from normal binary search
            # since the criteria is the function of both mid and h,
            # we need to hold one side. In this case, we hold the h.
            h = mid
        else:
            break

    # when the while loop ends h == l.
    res1 = b_search(nums, 0, l-1, target)
    res2 = b_search(nums, l, len(nums)-1, target)

    if res1 == -1 and res2 == -1:
        return -1
    else:
        return res1 if res2 == -1 else res2


def b_search(nums, l, h, target):

    while l <= h:
        mid = l + (h - l) // 2

        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            h = mid - 1
        else:
            return mid

    return -1
