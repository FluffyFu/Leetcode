def mul(num1, num2):
    res = [0] * (len(num1) + len(num2))

    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            cur = int(num1[i]) * int(num2[j])

            cur_sum = res[i+j+1] + cur
            res[i+j+1] = cur_sum % 10
            res[i+j] += cur_sum // 10
            # it is possible res[i] >= 10
            # at sometime but it'll be cleaned up
            # at future iteration.

    i = 0
    while i < len(res) and res[i] == 0:
        i += 1
    if i == len(res):
        return '0'

    return ''.join((str(c) for c in res[i:]))

