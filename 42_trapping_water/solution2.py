def brutal_force(height):
    """
    This is a 3 pass solution.
    """
    if not height:
        return 0

    left_max = []
    right_max = []

    cur_max = 0
    for h in height:
        cur_max = max(cur_max, h)
        left_max.append(cur_max)

    cur_max = 0
    for h in height[::-1]:
        cur_max = max(cur_max, h)
        right_max.append(cur_max)
    right_max = right_max[::-1]

    res = 0

    for i in range(len(height)):
        res += max(0, min(left_max[i], right_max[i]) - height[i])

    return res


def trap(height):
    """
    Make the three pass to one pass solution.
    The tricky part is how to move the left and right pointers.

    The idea is have max_left and max_right. For height[left],
    max_left is accurate, max_right is not (height[left]'s right components have not been
    scanned yet.) For height[right], max_right is accurate, max_left is not.

    However, the water only depends on the min(max_left, max_right). Therefore when:
        max_left <= max_right, we calculate height[left]. And move left pointer.
        when:
        max_left > max_right, we calculate height[right]. And move the right pointer.
    """
    if not height:
        return 0

    left = 0
    right = len(height) - 1

    max_left = 0
    max_right = 0

    res = 0

    while left <= right:
        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])

        if max_left <= max_right:
            res += max(0, max_left - height[left])
            left += 1
        else:
            res += max(0, max_right - height[right])
            right -= 1

    return res

