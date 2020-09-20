from solution import Solution
import pudb


def test_solution():
    nums = [3, 4, 5, 1, 2]
    assert Solution().find_min(nums) == 1

    nums = [4, 5, 6, 7, 0, 1, 2]
    # pudb.set_trace()
    assert Solution().find_min(nums) == 0

    nums = [2, 1]
    assert Solution().find_min(nums) == 1
