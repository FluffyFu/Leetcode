def missing(nums, lower, upper):
    # create missing intervals (both sides inclusive)
    if not nums:
        ins = [(lower, upper)]
        return convert(ins)

    ins = []
    if lower <= nums[0] - 1:
        ins.append((lower, nums[0]-1))

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            ins.append((nums[i-1]+1, nums[i]-1))
    return convert(ins)

    if upper >= nums[-1] + 1:
        ins.append((nums[-1]+1, upper))


def convert(ins):
    res = []
    for low, high in ins:
        if low == high:
            res.append(str(low))
        else:
            res.append(str(low) + '->' + str(high))
    return res

