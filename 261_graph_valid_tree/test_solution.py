from solution import valid
import pudb


def test():
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    # pudb.set_trace()
    assert True == valid(n, edges)

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    # pudb.set_trace()
    assert False == valid(n, edges)
