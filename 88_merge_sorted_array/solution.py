def merge(nums1, m, nums2, n):
    p = m - 1
    q = n - 1
    k = m + n - 1

    while p >= 0 or q >= 0:
        if p >= 0:
            n1 = nums1[p]
        else:
            n1 = -float('inf')
        if q >= 0:
            n2 = nums2[q]
        else:
            n2 = -float('inf')

        nums1[k] = max(n1, n2)

        if n1 > n2:
            p -= 1
        else:
            q -= 1
        k -= 1

