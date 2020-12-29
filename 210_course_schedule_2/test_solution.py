from solution import has_cycle
import pudb


def test_has_cycle():
    n = 2
    graph = {0: [1],
             1: [0]}

    # pudb.set_trace()
    assert has_cycle(n, graph) == True

