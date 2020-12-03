class Solution:
    def numWays(self, n, k):
        if n == 0 or k == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k**2
        elif n == 3:
            return k**3 - k

        dp = [0] * n
        dp[0], dp[1], dp[2] = k, k**2, k**3 - k

        for i in range(3, n):
            dp[i] = k * (k-1) * dp[i-2] + (k-1)**2 * dp[i-3]

        return dp[n-1]
