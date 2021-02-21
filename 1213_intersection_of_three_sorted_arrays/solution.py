def array_intersection(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0

    res = []
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            min_val = min([arr1[p1], arr2[p2], arr3[p3]])
            if min_val == arr1[p1]:
                p1 += 1
            if min_val == arr2[p2]:
                p2 += 1
            if min_val == arr3[p3]:
                p3 += 1
    return res

