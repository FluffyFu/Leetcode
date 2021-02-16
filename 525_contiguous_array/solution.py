def find_max_len(nums):
    """
    O(n**2) TLE
    """
    n = len(nums)
    dp = [[None] * n for _ in range(n)]

    for i in range(n):
        n0 = 1 if nums[i] == 0 else 0
        n1 = 1 - n0
        dp[i][i] = (n0, n1)

    max_len = 0

    for i in range(n-1):
        for j in range(i+1, n):
            n0 = 1 if nums[j] == 0 else 0
            n1 = 1 - n0
            dp[i][j] = (dp[i][j-1][0] + n0, dp[i][j-1][1] + n1)

            if dp[i][j][0] == dp[i][j][1]:
                max_len = max(max_len, dp[i][j][0] * 2)

    return max_len


def find_max_len2(nums):
    # {variable: index}
    var = 0
    index_map = {var: -1}
    max_len = 0

    for i, k in enumerate(nums):
        if k == 0:
            var -= 1
        elif k == 1:
            var += 1

        if var in index_map:
            max_len = max(max_len, i - index_map[var])
        else:
            index_map[var] = i

    return max_len

