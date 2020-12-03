def max_swap(num):
    digits = list(str(num))
    res = 0
    for i in range(len(digits)-1):
        for j in range(i+1, len(digits)):
            c_digits = digits[:]
            c_digits[i], c_digits[j] = c_digits[j], c_digits[i]
            if int("".join(c_digits)) > res:
                res = int("".join(c_digits))

    return num
