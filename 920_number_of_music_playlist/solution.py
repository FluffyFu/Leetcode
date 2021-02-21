import math


def num_playlist(n, l, k):
    """
    dp[i][j] is the number of player list with i songs and length j.

    when i <= k, its impossible to satisfy the requirement (the longest distance between
    two songs is k-1).

    when i == j, every song need to be used once, so dp[i][j] = factorial(i)

    other cases we can use the transition relation.
    """
      dp = [[0] * (l+1) for _ in range(n+1)]

       for i in range(k+1, n+1):
            for j in range(i, l+1):
                if i == j or i == k + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i-1][j-1] * i + dp[i][j-1] * (i-k)

        return dp[-1][-1] % (10**9 + 7)

