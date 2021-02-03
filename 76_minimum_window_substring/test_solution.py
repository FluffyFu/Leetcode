from solution import min_win


def test():
    s = "ADOBECODEBANC"
    t = "ABC"
    res = min_win(s, t)
    assert res == 'BANC'

    s = "ab"
    t = "a"
    res = min_win(s, t)
    assert res == 'a'

