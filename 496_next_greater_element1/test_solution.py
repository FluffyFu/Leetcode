from solution import next_element, next_element_2


def test():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    res = next_element_2(nums1, nums2)
    assert res == [-1, 3, -1]
