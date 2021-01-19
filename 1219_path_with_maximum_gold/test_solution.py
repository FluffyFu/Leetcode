from solution import max_gold
import pudb


def test():
    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    assert max_gold(grid) == 24
