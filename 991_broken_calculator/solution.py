def broken(x, y):
    if y <= x:
        return x - y
    if y % 2 == 0:
        return broken(x, y//2)
    else:
        return broken(x, y+1)

