def trap(height):
    """
    Fill the water layer by layer. For index i, we find the first left and
    first right bar that is higher than height[i]. The water for this layer is
    [min(h(right), h(left)) - h(i)] * (right - left)

    This can be done with O(1) space.
    """
    if not height:
        return 0

    stack = []
    res = 0

    for i in range(len(height)):
        while stack and height[stack[-1]] < height[i]:
            bot = height[stack.pop()]
            if not stack:
                break
            top = min(height[stack[-1]], height[i])
            w = i - stack[-1] - 1
            res += w * (top - bot)
        stack.append(i)

    return res
