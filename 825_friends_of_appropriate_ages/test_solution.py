from solution import num_fast, low_b_inclusive, norm_bs, up_b_inclusive, num_b
import pudb


def test():
    ages = [73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]
    res = num_b(ages)
    assert res == 29
    # assert res3 == 29


def test_low_b_inclusive():
    ages = [2, 2, 2]
    t = 2
    res = low_b_inclusive(ages, t)
    assert res == 0

    ages = [2, 2, 2]
    t = 3
    res = low_b_inclusive(ages, t)
    assert res == 3

    ages = [1, 2, 2, 2]
    t = 1
    res = low_b_inclusive(ages, t)
    assert res == 0


def test_up_b_inclusive():
    ages = [2, 2, 2]
    t = 2
    res = up_b_inclusive(ages, t)
    assert res == 2

    ages = [2, 2, 2]
    t = 3
    res = up_b_inclusive(ages, t)
    assert res == 2

    ages = [1, 2, 2, 2]
    t = 1
    res = up_b_inclusive(ages, t)
    assert res == 0


def test_norm_bs():
    ages = [1, 5, 9]
    t = 6
    res = norm_bs(ages, t)
    assert res == 2
    t = 0
    res = norm_bs(ages, t)
    assert res == 0
    t = 10
    res = norm_bs(ages, t)
    assert res == 3

