class Solution:
    def max_profit(self, prices, fee):
        if not prices:
            return 0
        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[len(prices) - 1][0]

    def max_profit_space_efficient(self, prices, fee):
        if not prices:
            return 0

        not_has = 0
        has = -prices[0]

        for p in prices[1:]:
            temp = not_has
            not_has = max(not_has, has + p - fee)
            has = max(has, temp - p)

        return not_has


"""
[1, 3, 7, 5, 10, 3], fee = 3


i = 0: 0, -1
i = 1 price = 3: max(0, -1 + 3 -3) = 0, max(-1, -3) = -1
i = 2 price = 7: max(0, -1 + 7 - 3) = 3, max(-1, -7) = -1
i = 3 price = 5: max(3, -1 + 5 -3) = 3, max(-1, -2) = -1
i = 4 price = 10: max(3, -1 + 10 - 3) = 6, max(-1, 3 - 10) = -1
"""
