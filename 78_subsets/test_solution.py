from solution import Solution
import pudb


def test_solution():
    nums = [1, 2, 3]
    # pudb.set_trace()
    res = Solution().subsets(nums)
    assert len(res) == 8
