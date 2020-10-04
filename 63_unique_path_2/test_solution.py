from solution import Solution
import pudb


def test_solution():
    obstacle_grid = [[0]]
    res = Solution().unique_path_with_obstacles(obstacle_grid)
    assert res == 1

    obstacle_grid = [[1, 0], [0, 0]]
    res = Solution().unique_path_with_obstacles(obstacle_grid)
    assert res == 0

    obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    pudb.set_trace()
    res = Solution().unique_path_with_obstacles(obstacle_grid)
    assert res == 2
