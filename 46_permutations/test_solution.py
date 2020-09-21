from solution import Solution, Solution_2
import pudb


def test_solution_2():
    nums = [1, 2, 3]
    # pudb.set_trace()
    res = Solution_2().permute(nums)
    assert len(res) == 6
    assert [1, 2, 3] in res
