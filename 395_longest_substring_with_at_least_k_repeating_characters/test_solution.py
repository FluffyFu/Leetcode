from solution import find_longest
import pudb


def test():
    s = 'aaabb'
    k = 3
    assert find_longest(s, k) == 3

    s = 'ababbc'
    k = 2
    assert find_longest(s, k) == 5
