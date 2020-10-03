from solution import Solution
import pudb


def test_solution():
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    # pudb.set_trace()
    assert Solution().length_of_lis(nums) == 6
