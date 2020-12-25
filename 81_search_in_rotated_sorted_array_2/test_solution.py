from solution import search
import pudb


def test_search():
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    assert search(nums, target) == True

    # pudb.set_trace()
    target = 3
    assert search(nums, target) == False

