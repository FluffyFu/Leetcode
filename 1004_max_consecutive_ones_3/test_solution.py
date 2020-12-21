from solution import max_ones, max_ones_2
import pudb


def test_max_ones():
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    # pudb.set_trace()

    res = max_ones_2(A, K)
    assert res == 6
