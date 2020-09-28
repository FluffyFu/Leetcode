from solution import Solution


def test_solution():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3

    assert Solution().k_smallest_pairs_brutal_force(
        nums1, nums2, k) == [[1, 6], [1, 4], [1, 2]]
    assert Solution().k_smallest_pairs_efficient(
        nums1, nums2, k) == [[1, 2], [1, 4], [1, 6]]

    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2

    assert Solution().k_smallest_pairs_brutal_force(
        nums1, nums2, k) == [[1, 1], [1, 1]]
    assert Solution().k_smallest_pairs_efficient(
        nums1, nums2, k) == [[1, 1], [1, 1]]

    nums1 = [1, 2]
    nums2 = [3]
    k = 3

    assert Solution().k_smallest_pairs_brutal_force(
        nums1, nums2, k) == [[2, 3], [1, 3]]
    assert Solution().k_smallest_pairs_efficient(
        nums1, nums2, k) == [[1, 3], [2, 3]]

