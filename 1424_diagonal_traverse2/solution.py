def find_diag(nums):
    temp = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            temp.append((i+j, i, j))

    temp = sorted(temp, key=lambda x: (x[0], -x[1]))

    return [nums[x[1]][x[2]] for x in temp]

