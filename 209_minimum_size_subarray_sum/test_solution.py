from solution import Solution
import pudb


def test_solution():
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    # pudb.set_trace()

    assert Solution().min_subarray_len(s, nums) == 2


def test_solution_binary_search():
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    # pudb.set_trace()

    assert Solution().min_subarray_len_binary_search(s, nums) == 2

