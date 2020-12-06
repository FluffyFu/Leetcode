from solution import can_finish
import pudb


def test_can_finish():
    # pudb.set_trace()
    assert can_finish(2, [[1, 0]]) == True
    assert can_finish(2, [[1, 0], [0, 1]]) == False

