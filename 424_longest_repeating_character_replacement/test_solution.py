from solution import replace
import pudb


def test():
    s = 'ABAB'
    k = 2
    assert replace(s, k) == 4

    s = 'AABABBA'
    k = 1
    assert replace(s, k) == 4

