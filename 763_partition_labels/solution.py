def partition(S):
    index = {c: i for i, c in enumerate(S)}

    left, right = 0, 0
    res = []
    right_most = index[S[0]]

    while right < len(S):
        right_most = max(right_most, index[S[right]])

        if right_most == right:
            res.append(right - left + 1)
            left = right + 1
        right += 1

    return res

