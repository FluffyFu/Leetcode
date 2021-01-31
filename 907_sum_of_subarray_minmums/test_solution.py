from solution import sum_sub_2


def test():
    A = [3, 1, 2, 4]
    res = sum_sub_2(A)
    assert res == 17

    A = [11, 81, 94, 43, 3]
    res = sum_sub_2(A)
    assert res == 444
