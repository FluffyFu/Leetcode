def move_zeros(nums):
    if not nums:
        return

    slow = 0
    while slow < len(nums) and nums[slow] != 0:
        slow += 1

    fast = slow + 1

    while fast < len(nums):
        while fast < len(nums) and nums[fast] == 0:
            fast += 1

        if fast < len(nums):
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1

