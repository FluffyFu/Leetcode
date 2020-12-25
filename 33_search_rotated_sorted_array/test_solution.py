from solution import Solution
import pudb


def test_solution():
    nums = [5, 4, 3, 2, 1]
    target = 3
    # pudb.set_trace()

    assert Solution().search(nums, target) == 2

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    assert Solution().search(nums, target) == 4

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert Solution().search(nums, target) == -1

    nums = [1]
    target = 0
    assert Solution().search(nums, target) == -1

