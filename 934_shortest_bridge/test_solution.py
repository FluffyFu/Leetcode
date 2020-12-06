from solution import shortest_bridge
import pudb


def test_shortest_bridge():
    A = [[0, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    # pudb.set_trace()
    res = shortest_bridge(A)
    assert res == 1
