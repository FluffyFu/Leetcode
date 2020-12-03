class Solution:
    def maxProfit(self, prices):
        """
        dp[i][j][k] i = [0, n-1], j = [0, 1], k = [0, 1, 2],
        represents the maximum profit at (i+1)-th day, with / without
        a holding and the number of already finished transactions.
        """
        n = len(prices)
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]
        # specify init conditions
        for i in range(n):
            dp[i][1][2] = -float('inf')  # impossible case

        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]
        dp[0][0][1] = -float('inf')
        dp[0][1][1] = -float('inf')
        dp[0][0][2] = -float('inf')
        dp[0][1][2] = -float('inf')

        for i in range(1, n):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0] + prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][1] - prices[i])
            dp[i][0][2] = max(dp[i-1][0][2], dp[i-1][1][1] + prices[i])

        return max(dp[n-1][0][0], dp[n-1][0][1], dp[n-1][0][2])
