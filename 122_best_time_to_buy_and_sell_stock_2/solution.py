

def max_profit(prices):
    """
    maintain two variables: current_min and current_max.
    And the update rule is:

    current_min = min(current_min, price[i])
    if price[i] <= current_max,
        we should sell the stock, current_min = float('inf'),
        current_max = -float('inf')
    if price[i] > current_max,
        we update current_max.
    """
    if not prices:
        return 0
    current_min = prices[0]
    current_max = prices[0]

    res = 0
    for p in prices[1:]:
        if p < current_max:
            res += (current_max - current_min)
            current_min = p
        else:
            current_min = min(current_min, p)
        current_max = p

    res += (current_max - current_min)  # take care of increasing list.
    return res


"""
[7, 1, 5, 3, 6, 4]
current_min = 7, current_max = 7

p = 1, res = 0, current_min = 1, current_max = 1
p = 5, res = 0, current_min = 1, current_max = 5
p = 3, res = 4, current_min = 3, current_max = 3
p = 6, res = 4, current_min = 3, current_max = 6
p = 4, res = 7, current_min = 4, current_max = 4


[1, 2, 3]
current_min = 1, current_max = 1

p = 2, current_max = 2, current_min = 1
p = 3, current_max = 3, current_min = 1


[7, 6, 5]

current_min = 7, current_max = 7
p = 6, res = 0, current_min = 6, current_max = 6
p = 5, res = 0 , current_min = 5, current_max = 5

"""

