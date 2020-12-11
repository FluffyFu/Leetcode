def max_profit(k, prices):
    if len(prices) // 2 < k:
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                res += (prices[i+1] - prices[i])

        return res
    else:
        # dp[i][j][t]
        dp = [[[0, 0] for _ in range(k)] for _ in range(len(prices))]

        for j in range(k):
            dp[0][j][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k):
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])

        return max(dp[len(prices)-1][j][0] for j in range(k))

