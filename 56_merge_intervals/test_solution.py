from solution import Solution


def test_solution():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge_clean(intervals) == [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    assert Solution().merge(intervals) == [[1, 5]]
    assert Solution().merge_clean(intervals) == [[1, 5]]
