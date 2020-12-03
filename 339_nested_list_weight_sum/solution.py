def weighted_sum(nums):
    res = 0
    depth = 1
    nested_list = nums

    while nested_list:
        new_nested_list = []
        sub_sum = 0
        for element in nested_list:
            if not isinstance(element, list):
                sub_sum += element
            else:
                new_nested_list += element
        res += depth * sub_sum
        nested_list = new_nested_list
        depth += 1

    return res
