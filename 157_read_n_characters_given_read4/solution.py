def read4(buf4):
    return 1


def read(buf, n):

    already_read = 0
    while n > 0:
        buf4 = [' '] * 4
        r_n = read4(buf4)
        if r_n == 0:
            break
        elif r_n > 0:
            for i in range(min(r_n, n)):
                buf[already_read+i] = buf4[i]
            already_read += min(n, r_n)
        n -= r_n

    return already_read

