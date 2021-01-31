from solution import brutal_force, area
import pudb


def test():
    heights = [2, 1, 5, 6, 2, 3]
    # pudb.set_trace()
    res = brutal_force(heights)
    assert res == 10

    heights = [1, 0, 3, 0]
    # pudb.set_trace()
    res = brutal_force(heights)
    assert res == 3

    heights = [1, 0, 0]
    res = brutal_force(heights)
    assert res == 1

    heights = [1, 1]
    res = brutal_force(heights)
    assert res == 2

