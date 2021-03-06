from solution import median
import pudb


def test():
    nums1 = [1, 3]
    nums2 = [2]
    assert median(nums1, nums2) == 2

    nums1 = [1, 2]
    nums2 = [3, 4]
    assert median(nums1, nums2) == 2.5

    nums1 = [1]
    nums2 = [1]
    # pudb.set_trace()
    assert median(nums1, nums2) == 1

    nums1 = [1]
    nums2 = [2]
    # pudb.set_trace()
    assert median(nums1, nums2) == 1.5
