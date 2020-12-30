from solution import max_point
import pudb


def test():
    nums = [100, 40, 17, 9, 73, 75]
    k = 3
    # pudb.set_trace()
    assert max_point(nums, k) == 248
