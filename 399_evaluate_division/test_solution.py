from solution import evaluate
import pudb


def test():
    equations = [["a", "e"], ["b", "e"]]
    values = [4.0, 3.0]
    queries = [["a", "b"], ["e", "e"], ["x", "x"]]

    # pudb.set_trace()
    # assert evaluate(equations, values, queries) == [1.333, 1.000, -1.000]

    equations = [["a", "b"], ["b", "c"], ["a", "c"]]
    values = [2.0, 3.0, 6.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    # pudb.set_trace()
    assert evaluate(equations, values, queries) == [1.333, 1.000, -1.000]
