from solution import spiral
import pudb


def test():
    R, C = 1, 4
    r0, c0 = 0, 0
    # pudb.set_trace()

    res = spiral(R, C, r0, c0)
    assert res == [[0, 0], [0, 1], [0, 2], [0, 3]]

