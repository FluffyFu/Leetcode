from solution import next_max
import pudb


def test():
    nums = [1, 2, 1]
    # pudb.set_trace()
    res = next_max(nums)
    assert res == [2, -1, 2]

