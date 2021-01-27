from solution import flatten, flatten2


def test():
    a = [1, 2, [3]]
    res = flatten(a)

    assert res == [1, 2, 3]

    a = [1, [2, [3]]]
    res = flatten(a)

    assert res == [1, 2, 3]


def test_flatten2():
    a = [1, 2, [3]]
    res = flatten2(a)

    assert res == [1, 2, 3]

    a = [1, [2, [3]]]
    res = flatten2(a)

    assert res == [1, 2, 3]
