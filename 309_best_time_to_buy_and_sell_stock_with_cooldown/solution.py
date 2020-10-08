class Solution:
    def max_profit(self, prices):
        if not prices:
            return 0

        dp = [[0, 0] for _ in range(len(prices) + 1)]
        dp[-1][0] = 0
        dp[-1][1] = -float('inf')
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[len(prices)-1][0]


"""
[1, 2, 3, 0, 2]

i = -1: 0, -inf
i = 0: 0, -1
i = 1, p = 2, max(0, 1) = 1, max(-1, -inf) = -1
i = 2, p = 3, max(1, -1 + 3) = 2, max(-1, -1 - 3) = -1
i = 3, p = 0, max(2, -1 + 0) = 2, max(-1, 1) = 1
i = 4, p = 2, max(2, 1 + 2) = 3, max(1, 0) = 1
"""
