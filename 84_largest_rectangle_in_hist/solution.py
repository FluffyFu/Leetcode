def brutal_force(heights):
    res = 0
    for i in range(len(heights)):
        h = heights[i]
        for j in range(i, -1, -1):
            if heights[j] < h:
                break
        if j == i or heights[j] >= h:
            j -= 1

        for k in range(i, len(heights)):
            if heights[k] < h:
                break
        if k == i or heights[k] >= h:
            k += 1

        res = max(res, h * (k - j - 1))
    return res


def one_pass(heights):
    """
    For a position i, find the first left and right index such that
    h[left] < heights[i], h[right] < heights.
    The area is (right - left - 1) * heights[i].

    Scan the height from left and build a non-decreasing stack.
    When h[stack[-1]] < h[i] happens, the right boundary is i
    and the left boundary is stack[-2].

    One trick is put a 0 in the end, in case the origin list is increasing
    and the area calculation is never triggered.
    """
    heights.append(0)
    stack = [-1]

    res = 0
    for i in range(len(heights)):
        # non-decreasing stack
        while heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i - 1 - (stack[-1] + 1) + 1
            res = max(res, h * w)
        stack.append(i)

    return res


def area(heights):
    heights.append(0)
    stack = [-1]

    res = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - 1 - stack[-1]
            res = max(res, h * w)
        stack.append(i)

    return res

