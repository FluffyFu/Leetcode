from solution import Solution


def test_solution():
    intervals = [[1, 4], [3, 6], [2, 8]]
    assert Solution().remove_covered_intervals(intervals) == 2

    intervals = [[1, 4], [2, 8], [1, 6]]
    assert Solution().remove_covered_intervals(intervals) == 2
