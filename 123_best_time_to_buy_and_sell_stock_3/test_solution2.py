from solution2 import Solution


def test_solution():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    assert Solution().maxProfit(prices) == 6

    prices = [1, 2, 3, 4, 5]
    assert Solution().maxProfit(prices) == 4

    prices = [7, 6, 4, 3, 1]
    assert Solution().maxProfit(prices) == 0

    prices = [1]
    assert Solution().maxProfit(prices) == 0

