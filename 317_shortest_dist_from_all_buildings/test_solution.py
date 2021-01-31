from solution import shortest, shortest_2


def test():
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    res = shortest(grid)
    res2 = shortest_2(grid)
    assert res == 7
    assert res2 == 7

    grid = [[1, 1, 1]]
    res = shortest_2(grid)
    assert res == -1
