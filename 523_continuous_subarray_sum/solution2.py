def subarray_sum(nums, k):
    if len(nums) < 2:
        return False
    if k == 0:
        return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))

    acc = 0
    m_index = {0: -1}

    for i, n in enumerate(nums):
        acc = (acc + n) % k

        if acc in m_index and i - m_index[acc] > 1:
            return True
        elif acc not in m_index:
            m_index[acc] = i

    return False

