from solution import Solution, Solution_2
import pudb


def test_solution():
    n = 3
    # pudb.set_trace()
    res = Solution().generate_parenthesis(n)
    assert len(res) == 5


def test_solution_2():
    n = 3
    # pudb.set_trace()
    res = Solution_2().generate_parenthesis(n)
    assert len(res) == 5

