class Solution:
    def max_profit(self, prices):
        if not prices:
            return 0
        # dp[i][k][j] i-th day, conducted k+1 transactions, if holding stock
        dp = [[[0, 0] for _ in range(2)] for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1] + prices[i])
            dp[i][0][1] = max(dp[i-1][0][1], -prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])

        return max(0, dp[len(prices)-1][0][0], dp[len(prices)-1][1][0])

    def max_profit_generalize_k(self, prices):
        """
        Generalize k
        """
        if not prices:
            return 0
        K = 2
        dp = [[[0, 0] for _ in range(K+1)] for _ in range(len(prices))]
        # base cases
        for k in range(K+1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]

        for i in range(1, len(prices)):
            for k in range(1, K+1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return max(dp[len(prices)-1][0][0],
                   dp[len(prices)-1][1][0],
                   dp[len(prices)-1][2][0])

    def max_profit_space_efficient(self, prices):
        if not prices:
            return 0
        cur_0_0 = 0
        cur_0_1 = -prices[0]
        cur_1_0 = 0
        cur_1_1 = -prices[0]

        for p in prices[1:]:
            temp_0_0, temp_0_1, temp_1_0, temp_1_1 = cur_0_0, cur_0_1, cur_1_0, cur_1_1

            cur_0_0 = max(temp_0_0, temp_0_1 + p)
            cur_0_1 = max(temp_0_1, -p)
            cur_1_0 = max(temp_1_0, temp_1_1 + p)
            cur_1_1 = max(temp_1_1, temp_0_0 - p)

        return max(0, cur_1_0, cur_0_0)


"""
[1, 4, 2, 3]

cur_min = 1, pre = 1

p = 4, res = [], cur_min = 1, pre = 4
p = 2, res = [3], cur_min = 2, pre = 2
p = 3, res = [3], cur_min = 2, pre = 3
"""
