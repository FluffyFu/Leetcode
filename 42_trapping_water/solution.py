def trap(height):
    if not height:
        return 0

    left_max = height[0]
    right_max = height[-1]

    left = 0
    right = len(height) - 1
    res = 0

    while left <= right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            res += max(0, left_max - height[left])
            left += 1
        else:
            res += max(0, right_max - height[right])
            right -= 1

    return res

