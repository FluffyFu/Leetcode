from solution import kth_smallest


def test():
    mat = [[1, 3, 11], [2, 4, 6]]
    k = 5
    res = kth_smallest(mat, k)

    assert res == 7

    mat = [[1, 3, 11], [2, 4, 6]]
    k = 9
    res = kth_smallest(mat, k)

    assert res == 17

    mat = [[1, 10, 10], [1, 4, 5], [2, 3, 6]]
    k = 7
    res = kth_smallest(mat, k)

    assert res == 9

    mat = [[1, 10, 10], [1, 4, 5], [2, 3, 6]]
    k = 14
    res = kth_smallest(mat, k)

    assert res == 16

