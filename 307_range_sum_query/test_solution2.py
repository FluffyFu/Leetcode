from solution2 import NumArray


def test_numarray():
    nums = [1, 3, 5]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 2) == 9
    assert num_array.sumRange(1, 2) == 8

    num_array.update(0, 2)
    assert num_array.sumRange(0, 2) == 10
