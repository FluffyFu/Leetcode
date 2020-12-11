def max_profit(prices):
    # dp[i][j][k]
    k = 2
    dp = [[[0, 0] for _ in range(k+1)] for _ in range(len(prices))]

    for j in range(k+1):
        dp[0][j][1] = -prices[0]

    for i in range(1, len(prices)):
        for j in range(1, k+1):
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

    return max(dp[len(prices)-1][j][0] for i in range(k+1))

