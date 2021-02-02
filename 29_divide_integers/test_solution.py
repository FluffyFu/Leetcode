from solution import divide, divide_simple
import pudb


def test():
    a = 10
    b = 2
    # pudb.set_trace()
    res = divide(a, b)
    assert res == 5
