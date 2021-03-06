from solution import cheapest
import pudb


def test():
    n = 11
    flights = [[0, 3, 3], [3, 4, 3], [4, 1, 3], [0, 5, 1], [5, 1, 100], [0, 6, 2], [6, 1, 100], [
        0, 7, 1], [7, 8, 1], [8, 9, 1], [9, 1, 1], [1, 10, 1], [10, 2, 1], [1, 2, 100]]
    src = 0
    dst = 2
    k = 4

    pudb.set_trace()
    assert cheapest(n, flights, src, dst, k) == 11
