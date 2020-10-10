class Solution:
    def max_profit(self, k, prices):
        if not prices:
            return 0
        if k > len(prices) // 2:
            # equivalent to 'infinite' number of transactions
            cur_min = prices[0]
            pre = prices[0]
            res = 0

            for p in prices[1:]:
                if p < pre:
                    res += (pre - cur_min)
                    cur_min = p
                else:
                    cur_min = min(cur_min, p)
                pre = p
            res += (pre - cur_min)
            return res

        else:
            # dp[i][k][j] represents the optimal profit on the i-th day with k transactions and
            # if still holding a stock
            dp = [[[0, 0] for _ in range(k+1)] for _ in range(len(prices))]

            for j in range(1, k+1):
                dp[0][j][1] = -prices[0]

            for i in range(1, len(prices)):
                for j in range(1, k+1):
                    dp[i][j][0] = max(dp[i-1][j][0],
                                      dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1],
                                      dp[i-1][j-1][0] - prices[i])
            return max((res[0] for res in dp[len(prices)-1]))
