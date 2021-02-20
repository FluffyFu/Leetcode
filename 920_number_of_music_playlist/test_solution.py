from solution import num_playlist
import pudb


def test():
    n = 2
    l = 3
    k = 0
    res = num_playlist(n, l, k)

    assert res == 6

    n = 3
    l = 3
    k = 1
    res = num_playlist(n, l, k)

    assert res == 6

    n = 2
    l = 3
    k = 1
    res = num_playlist(n, l, k)

    assert res == 2
