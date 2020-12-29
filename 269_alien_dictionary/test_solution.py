from solution import alien_order
import pudb


def test():
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    assert alien_order(words) == 'wertf'

    words = ['z', 'x', 'z']
    assert alien_order(words) == ''

    # words = ['ac', 'ab', 'zc', 'zb']
    # pudb.set_trace()
    # assert alien_order(words) == 'cabz'  # one possible result

    words = ['abc', 'ab']
    assert alien_order(words) == ''

    words = ['z', 'z']
    # pudb.set_trace()
    assert alien_order(words) == 'z'

