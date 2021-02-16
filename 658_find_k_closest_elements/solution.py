def find_k_close(arr, k, x):
    if k >= len(arr):
        return arr

    l, h = 0, len(arr) - 1

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] == x:
            l = mid
            break
        elif x < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1

    if l == len(arr):
        return arr[-k:]
    elif l == 0:
        return arr[:k]

    # p1 and p2 are boundary (not inclusive)
    p1 = l - 1
    p2 = l

    while p1 >= 0 and p2 <= len(arr) - 1:
        if abs(arr[p1] - x) <= abs(arr[p2] - x):
            p1 -= 1
        else:
            p2 += 1

        if p2 - p1 - 1 == k:
            return arr[p1+1:p2]

    if p1 == -1:
        return arr[:k]
    else:
        return arr[-k:]

