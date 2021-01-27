from solution import min_cost
import pudb


def test():
    arr = [6, 2, 4]
    # pudb.set_trace()
    res = min_cost(arr)

    assert res == 32
