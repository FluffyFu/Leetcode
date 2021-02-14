from solution import regex


def test():
    s = 'a'
    p = 'ab*'
    assert regex(s, p) == True

    s = 'abb'
    p = 'ab*'
    assert regex(s, p) == True
