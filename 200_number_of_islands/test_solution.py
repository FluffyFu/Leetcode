from solution import Solution
import pudb


def test_solution():
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '1'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    assert Solution().num_islands(grid) == 1

    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    assert Solution().num_islands(grid) == 3
