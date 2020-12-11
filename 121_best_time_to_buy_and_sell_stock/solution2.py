def max_profit(prices):
    low = -float('inf')
    res = 0

    for i in range(len(prices)-1):
        if low > prices[i]:
            low = prices[i]
        if prices[i+1] > prices[i]:
            res = max(res, prices[i+1]-low)

    return res

