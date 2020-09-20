from solution import Solution


def test_solution():
    weights = [i for i in range(1, 11)]
    D = 5
    assert Solution().ship_within_d_days(weights, D) == 15

    weights = [3, 2, 2, 4, 1, 4]
    D = 3
    assert Solution().ship_within_d_days(weights, D) == 6

    weights = [1, 2, 3, 1, 1]
    D = 4
    assert Solution().ship_within_d_days(weights, D) == 3
