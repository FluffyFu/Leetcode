def can_partition(nums):
    if sum(nums) % 2 == 1:
        return False
    else:
        target = sum(nums) // 2

    # dp[i][j] using nums up to nums[i] and see if it's possible to form j
    dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
    n = len(nums)

    for i in range(n):
        dp[i][0] = True

    for j in range(1, target + 1):
        if nums[0] == j:
            dp[0][j] = True
        else:
            dp[0][j] = False

    for i in range(1, n):
        for j in range(target+1):
            dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i]]
                                      if j >= nums[i] else False)

    return dp[n-1][target]

