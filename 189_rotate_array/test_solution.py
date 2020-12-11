from solution import rotate


def test_rotate():
    nums = [i for i in range(1, 8)]
    k = 3

    res = rotate(nums, k)
    assert res == [5, 6, 7, 1, 2, 3, 4]
