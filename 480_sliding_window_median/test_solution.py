from solution import median
import pudb


def test():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    res = median(nums, k)
    assert res == [1, -1, -1, 3, 5, 6]

