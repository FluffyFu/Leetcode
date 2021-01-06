def max_vowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    cnts = 0

    for r in range(k):
        if s[r] in vowels:
            cnts += 1
    res = cnts

    l, r = 0, k

    while r < len(s):
        if s[r] in vowels:
            cnts += 1
        if s[l] in vowels:
            cnts -= 1

        res = max(res, cnts)

        l += 1
        r += 1

    return res

