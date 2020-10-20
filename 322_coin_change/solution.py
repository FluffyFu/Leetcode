class Solution:

    def coin_change(self, coins, amount):
        if not coins:
            return -1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for val in coins:
                if i - val < 0:
                    continue
                dp[i] = min(dp[i], dp[i-val]+1)

        return dp[amount] if dp[amount] != amount + 1 else -1


class Solution2:

    def coin_change(self, coins, amount):
        if not coins:
            return -1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for val in coins:
            for i in range(val, amount+1):
                dp[i] = min(dp[i], dp[i-val]+1)

        return dp[-1] if dp[-1] != amount + 1 else -1


"""
coins = [2], amount = 3
dp = [0, 0, 0, 0]

i = 1, cur_min = 'inf', dp = [0, -1, 0, 0]
i = 2 cur_min = 0, dp = [0, -1, 1, 0]
i = 3 cur_min = 'inf', dp = [0, -1, 1, -1]
"""
