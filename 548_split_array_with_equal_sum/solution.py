def is_equal(nums):
    if len(nums) < 7:
        return False

    n_sum = [nums[0]]
    for i in range(1, len(nums)):
        n_sum.append(n_sum[-1] + nums[i])

    for j in range(3, len(nums)-3):
        # it is possible there are more than one sum value
        # 2, 1, -1, 2, 1, remove -1, we have 3, remove 1, we have 2
        seen = set()
        for i in range(1, j-1):
            if n_sum[i-1] == (n_sum[j-1] - n_sum[i]):
                seen.add(n_sum[i-1])

        for k in range(j+2, len(nums)-1):
            if (n_sum[k-1] - n_sum[j]) == (n_sum[-1] - n_sum[k]) and (n_sum[k-1] - n_sum[j]) in seen:
                return True

    return False

