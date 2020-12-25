from solution3 import search
import pudb


def test_search():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    assert search(nums, target) == 4

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    # pudb.set_trace()

    assert search(nums, target) == -1
