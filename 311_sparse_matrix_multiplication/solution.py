def multiply(A, B):
    # da[i][j] is the value of i-th row and j-th column
    da = dict()
    for i in range(len(A)):
        col_d = dict()
        for j in range(len(A[0])):
            if A[i][j] != 0:
                col_d[j] = A[i][j]
        da[i] = col_d

    # db[i][j] is the value of i-th column and j-th row.
    db = dict()
    for j in range(len(B[0])):
        row_d = dict()
        for i in range(len(B)):
            if B[i][j] != 0:
                row_d[i] = B[i][j]
        db[j] = row_d

    res = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            s = 0
            for k, v in da[i].items():
                if k in db[j]:
                    s += v * db[j][k]
            res[i][j] = s

    return res

