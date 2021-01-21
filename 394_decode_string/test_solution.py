from solution import decode
import pudb


def test():
    s = '3[a]2[bc]'
    # pudb.set_trace()
    assert decode(s) == 'aaabcbc'
