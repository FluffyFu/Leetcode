def valid(flowerbed, n):
    l = len(flowerbed)
    s = sum(flowerbed)

    if s + n > (l + 1) // 2:
        return False
    if n == 0:
        return True

    if l == 1:
        if s == 1:
            return False
        elif n == 1:
            return True
        return False

    i = 0
    # l >= 2
    while i < l:
        if flowerbed[i] == 1:
            i += 1
            continue
        if i == 0 and flowerbed[i+1] == 0:
            n -= 1
            flowerbed[i] = 1
        elif i == l-1 and flowerbed[i-1] == 0:
            flowerbed[i] = 1
            n -= 1
        elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
        i += 1

    return n <= 0

