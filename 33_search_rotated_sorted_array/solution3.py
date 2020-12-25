def search(nums, target):
    l, h = 0, len(nums) - 1

    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target <= nums[mid] and target >= nums[l]:
                h = mid - 1
            else:
                l = mid + 1

        elif nums[mid] < nums[l]:
            if target >= nums[mid] and target <= nums[h]:
                l = mid + 1
            else:
                h = mid - 1

    return -1

