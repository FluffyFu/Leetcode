def to_goat(S):
    res = []
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I',
              'O', 'U'}

    for i, w in enumerate(S.split()):
        if w[0] in vowels:
            res.append(w + 'ma' + (i+1) * 'a')
        elif w[0] not in vowels:
            res.append(w[1:] + w[0] + 'ma' + (i+1) * 'a')

    return ' '.join(res)

