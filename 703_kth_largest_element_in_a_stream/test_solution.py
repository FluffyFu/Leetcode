from solution import KthLargest


def test_solution():
    k = 3
    nums = [4, 5, 8, 2]

    k_largest = KthLargest(k, nums)
    assert k_largest.add(3) == 4
    assert k_largest.add(5) == 5
    assert k_largest.add(10) == 5
    assert k_largest.add(9) == 8
    assert k_largest.add(4) == 8

