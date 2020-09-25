from solution import Solution, SolutionFast


def test_solution():
    candidates = [2, 3, 6, 7]
    target = 7
    res = Solution().combination_sum(candidates, target)
    # assert len(res) == 2

    candidates = [2, 3, 5]
    target = 8
    res = Solution().combination_sum(candidates, target)
    assert len(res) == 3


def test_solution_fast():
    candidates = [2, 3, 6, 7]
    target = 7
    res = SolutionFast().combination_sum(candidates, target)
    # assert len(res) == 2

    candidates = [2, 3, 5]
    target = 8
    res = SolutionFast().combination_sum(candidates, target)
    assert len(res) == 3
