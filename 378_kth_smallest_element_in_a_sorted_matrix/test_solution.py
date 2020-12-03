from solution import kth_smallest


def test_kth_smallest():
    matrix = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]]
    k = 8

    assert kth_smallest(matrix, k) == 13

