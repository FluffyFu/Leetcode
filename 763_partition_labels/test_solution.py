from solution import partition
import pudb


def test():
    S = 'abaccbdeffed'
    res = partition(S)
    assert res == [6, 6]
