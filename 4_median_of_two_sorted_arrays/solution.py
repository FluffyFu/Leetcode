def median(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # make sure m <= n, otherwise, index j could be out of range
    m = len(nums1)
    n = len(nums2)

    if m == 0:
        return nums2[n//2] if n % 2 == 1 else (nums2[n//2] + nums2[n//2-1]) / 2

    l = 0
    # all the elements in nums1 goes to the lower half.
    r = m

    while l <= r:
        i = l + (r - l) // 2
        j = (m + n) // 2 - i

        if (i == 0 and nums2[j-1] <= nums1[i]) or (j == 0 and nums1[i-1] <= nums2[j]) or (j == n and nums2[j-1] <= nums1[i]) or (i == m and nums1[i-1] <= nums2[j]) or (0 < i < n and 0 < j < n and nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]):
            # found i and j, take care of all the edge cases
            break
        # i and j cannot be 0 at the same time, so
        # one of the condition will be executed.
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too large
            r = i - 1
        elif j > 0 and nums2[j-1] > nums1[i]:
            # i is too small
            l = i + 1

    # make sure the index are valid, otherwise it becomes a dummy.
    if (m + n) % 2 == 0:
        return (max(nums1[i-1] if i-1 >= 0 else -float('inf'),
                    nums2[j-1] if j-1 >= 0 else -float('inf')) +
                min(nums1[i] if i < m else float('inf'), nums2[j] if j < n else float('inf'))) / 2
    else:
        return min(nums1[i] if i < m else float('inf'), nums2[j] if j < n else float('inf'))

