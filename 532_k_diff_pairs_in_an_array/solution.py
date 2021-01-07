def find_pairs(nums, k):
    nums.sort()

    slow, fast = 0, 1
    res = set()

    while fast < len(nums) and slow < len(nums):
        if nums[fast] - nums[slow] < k:
            fast += 1
        elif nums[fast] - nums[slow] > k:
            slow += 1
        elif nums[fast] - nums[slow] == k and fast != slow:
            res.add((nums[slow], nums[fast]))
            fast += 1
            slow += 1
        else:
            fast += 1

    return len(res)

