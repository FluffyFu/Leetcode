from solution import simple, helper, cal


def test_simple():
    s = '1+2-3'
    res = simple(s)
    assert res == 0

    s = '27-4+5-0'
    res = simple(s)
    assert res == 28


def test_helper():
    s = '1-2*3'
    res = helper(s)
    assert res == -5

    s = '1-2*3/4'
    res = helper(s)
    assert res == 0


def test_cal():
    s = '1-2*3'
    res = cal(s)
    assert res == -5

    s = '1-2*3/4'
    res = cal(s)
    assert res == 0
