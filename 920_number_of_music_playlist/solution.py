import math


def num_playlist(n, l, k):
    dp = [[0] * l for _ in range(n)]

    if k == 0:
        for j in range(l):
            dp[0][j] = 1
    for i in range(n):
        dp[i][i] = math.factorial(i+1)

    for i in range(1, n):
        for j in range(i+1, l):
            dp[i][j] = dp[i-1][j-1] * n + dp[i][j-1] * (n-k)

    return dp[-1][-1]

