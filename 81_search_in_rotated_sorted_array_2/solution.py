def search(nums, target):
    l, h = 0, len(nums) - 1

    while l <= h:
        mid = (l + h) // 2

        if nums[mid] == target:
            return True

        while l < mid and nums[l] == nums[mid]:
            l += 1

        if mid == l:
            l = mid + 1

        elif nums[mid] > nums[l]:
            if target >= nums[l] and target < nums[mid]:
                h = mid - 1
            else:
                l = mid + 1

        elif nums[mid] < nums[l]:
            if target > nums[mid] and target <= nums[h]:
                l = mid + 1
            else:
                h = mid - 1

    return False

