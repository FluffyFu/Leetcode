from solution import Solution


def test_solution():
    nums = [1, 1, 2]
    res = Solution().permutation(nums)
    assert res == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

