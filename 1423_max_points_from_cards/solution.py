def max_point(cardPoints, k):
    if k >= len(cardPoints):
        return sum(cardPoints)

    l, r = len(cardPoints)-1, k-1

    res = max(sum(cardPoints[:k]), sum(cardPoints[-k:]))
    cum = sum(cardPoints[:k])
    while k > 1:
        cum = cum - cardPoints[r] + cardPoints[l]

        res = max(cum, res)
        k -= 1
        r -= 1
        l -= 1

    return res

