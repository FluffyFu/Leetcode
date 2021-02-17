def find_k(arr, k):
    cur = 1
    index = 0
    while index < len(arr):
        if cur != arr[index]:
            k -= 1
        else:
            index += 1
        if k == 0:
            return cur
        cur += 1

    return cur + k - 1
