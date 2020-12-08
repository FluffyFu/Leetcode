def max_subarray(nums):
    max_sum = nums[0]

    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = n
        else:
            cur_sum += n

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum

