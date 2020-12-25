from solution2 import search
import pudb


def test_search():
    nums = [1, 3, 5]
    target = 3
    # pudb.set_trace()

    res = search(nums, target)
    assert res == 1

    nums = [5, 1, 3]
    target = 5

    # pudb.set_trace()
    res = search(nums, target)
    assert res == 0

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    # pudb.set_trace()
    res = search(nums, target)
    assert res == 4
