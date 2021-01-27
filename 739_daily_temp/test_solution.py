from solution import find_days
import pudb


def test():
    T = [1, 2, 3, 1, 0, 4]
    # pudb.set_trace()
    res = find_days(T)
    assert res == [1, 1, 3, 2, 1, 0]
