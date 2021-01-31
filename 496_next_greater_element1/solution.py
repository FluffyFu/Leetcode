def next_element(nums1, nums2):
    stack = []
    pre_res = [-1] * len(nums2)

    for i in range(len(nums2)):
        while stack and nums2[stack[-1]] < nums2[i]:
            index = stack.pop()
            pre_res[index] = nums2[i]
        stack.append(i)

    pos_index = {}
    for i in range(len(nums2)):
        pos_index[nums2[i]] = i

    res = []

    for k in nums1:
        res.append(pre_res[pos_index[k]])

    return res


def next_element_2(nums1, nums2):
    stack = []
    pre_res = {}

    for k in nums2:
        while stack and stack[-1] < k:
            cur = stack.pop()
            pre_res[cur] = k

        stack.append(k)

    return [pre_res.get(k, -1) for k in nums1]

