from solution import calculate
import pudb


def test():
    s = '3+2'
    # pudb.set_trace()
    res = calculate(s)
    assert res == 5

    s = '3/2'
    # pudb.set_trace()
    res = calculate(s)
    assert res == 1

    s = '14-3/2'
    # pudb.set_trace()
    res = calculate(s)
    assert res == 13

