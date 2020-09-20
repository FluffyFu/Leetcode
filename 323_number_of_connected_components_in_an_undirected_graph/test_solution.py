from solution import Solution


def test_solution():
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    assert Solution().count_components(n, edges) == 2
