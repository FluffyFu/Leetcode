def max_profit(prices):
    res = 0
    if len(prices) < 2:
        return res
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            res += (prices[i+1] - prices[i])

    return res

