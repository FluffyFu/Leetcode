from solution import Solution
import pudb


def test_solution():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # pudb.set_trace()
    res = Solution().max_profit_generalize_k(prices)
    assert res == 6
