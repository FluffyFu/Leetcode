from solution2 import Solution, Solution2, Solution3
import pudb


def test_solution():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # pudb.set_trace()
    res = Solution().length_lis(nums)
    assert res == 4


def test_solution2():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = Solution2().length_lis(nums)
    assert res == 4


def test_solution3():
    nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    # pudb.set_trace()
    res = Solution3().length_lis(nums)
    assert res == 6

