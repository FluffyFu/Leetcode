class Solution:
    def max_profit(self, prices):
        """
        The meaning of dp[i] is the maximum profit of selling the stock
        at i-th day. And the stock has to be bought on or before that day.
        dp[i+1] is max(dp[i] + (prices[i+1] - prices[i]), 0). This is because
        the sell day is fixed and bought day must be the same as bought day of
        dp[i]. However, if this value is less than zero, we would rather buy and
        sell on the (i+1)-th day, to make the profit equal to 1.
        """
        if not prices:
            return 0

        pre = 0
        opt_profit = 0
        for i in range(1, len(prices)):
            pre = max(pre + (prices[i] - prices[i-1]), 0)
            opt_profit = max(opt_profit, pre)

        return opt_profit

    def max_profit_min_price(self, prices):
        """
        The idea is to maintain the min_price and max_profit, the update rule for
        max_profit is max(max_profit, current_price - min_price)
        """
        if not prices:
            return 0
        min_price = float('inf')
        opt = 0

        for price in prices:
            min_price = min(price, min_price)
            opt = max(opt, price - min_price)

        return opt


"""
nums = [7, 1, 5, 3, 6, 4]

price = 7, min_price = 7, opt = 0
price = 1, min_price = 1, opt = 0
price = 5, min_price = 1, opt = 4
price = 3, min_price = 1, opt = 4
price = 6, min_price = 1, opt = 5
price = 4, min_price = 1, opt = 5

"""

