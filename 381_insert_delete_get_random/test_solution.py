from solution import RandomizedCollection
import pudb


def test():
    rd = RandomizedCollection()
    # pudb.set_trace()
    rd.insert(1)
    rd.insert(1)
    rd.remove(1)
    res = rd.getRandom()
    assert res == 1
