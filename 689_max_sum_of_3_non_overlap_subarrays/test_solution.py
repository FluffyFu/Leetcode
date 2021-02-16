from solution import max_non_overlap
import pudb


def test():
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    k = 2
    res = max_non_overlap(nums, k)

    assert [0, 3, 5] == res
