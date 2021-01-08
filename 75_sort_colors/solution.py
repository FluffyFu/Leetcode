def sort_color(nums):
    left = 0
    right = len(nums) - 1
    cur = 0

    while cur <= right:
        if nums[cur] == 0:
            nums[cur], nums[left] = nums[left], nums[cur]
            cur += 1
            left += 1
        elif nums[cur] == 2:
            nums[cur], nums[right] = nums[right], nums[cur]
            right -= 1
        else:
            cur += 1

