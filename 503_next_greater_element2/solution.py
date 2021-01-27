def next_max(nums):
    res = [-1] * len(nums)
    stack = []

    for i in list(range(len(nums))) * 2:
        while stack and nums[stack[-1]] < nums[i]:
            cur = stack.pop()
            res[cur] = nums[i]
        stack.append(i)

    return res

