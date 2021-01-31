from solution3 import trap


def test():
    height = [4, 2, 0, 3, 2, 5]
    res = trap(height)
    assert res == 9
