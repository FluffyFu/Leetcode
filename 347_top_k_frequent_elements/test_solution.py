from solution import Solution


def test_solution():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert Solution().top_k_frequent(nums, k) == [1, 2]

    nums = [1]
    k = 1
    assert Solution().top_k_frequent(nums, k) == [1]
