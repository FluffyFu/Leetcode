def pre_permutation(arr):
    if not arr:
        return arr
    i = len(arr) - 1
    while i > 0 and arr[i] >= arr[i-1]:
        i -= 1
    if i == 0:
        return arr

    j = len(arr) - 1
    while j > i-1 and arr[j] >= arr[i-1]:
        j -= 1

    while j > i-1 and arr[j] == arr[j-1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    return arr

