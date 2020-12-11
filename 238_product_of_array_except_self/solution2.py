def product(nums):
    front = [1]
    for num in nums[:-1]:
        front.append(front[-1] * num)

    end = [1]
    for num in nums[::-1][:-1]:
        end.append(end[-1] * num)

    end = end[::-1]

    res = []
    for i in range(len(nums)):
        res.append(front[i] * end[i])

    return res


def product_space_efficient(nums):
    res = [1]
    for num in nums[:-1]:
        res.append(res[-1] * num)

    cur = 1
    for i in range(len(nums)-2, -1, -1):
        cur *= nums[i+1]
        res[i] *= cur

    return res

