from solution2 import insert_interval


def test_insert_interval():
    intervals = [[1, 5]]
    new_interval = [2, 3]

    res = insert_interval(intervals, new_interval)
    assert res == [[1, 5]]

