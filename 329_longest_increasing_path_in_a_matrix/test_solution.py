from solution import longest_increase_path
import pudb


def test_path():
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    res = longest_increase_path(matrix)
    assert res == 4
