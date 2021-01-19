from solution import restore, create_ip
import pudb


def test_restore():
    s = "25525511135"
    res = restore(s)
    assert len(res) == 2

    s = '010010'
    res = restore(s)
    assert len(res) == 2
