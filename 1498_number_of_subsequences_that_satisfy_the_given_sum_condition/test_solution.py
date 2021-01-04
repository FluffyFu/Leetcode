from solution import find_num, find_num_fast
import pudb


def test():
    nums = [3, 5, 6, 7]
    target = 9
    assert find_num(nums, target) == 4
    assert find_num(nums, target) == find_num_fast(nums, target)

    nums = [3, 3, 6, 8]
    target = 10
    assert find_num(nums, target) == 6
    assert find_num(nums, target) == find_num_fast(nums, target)

    nums = [5, 2, 4, 1, 7, 6, 8]
    target = 16
    assert find_num(nums, target) == 127
    assert find_num(nums, target) == find_num_fast(nums, target)
