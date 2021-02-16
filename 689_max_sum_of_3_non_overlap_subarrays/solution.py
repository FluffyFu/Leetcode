def max_non_overlap(nums, k):
    single_index = [0]
    double_index = [0, k]
    triple_index = [0, k, 2*k]

    first_sum = sum(nums[:k])
    second_sum = sum(nums[k:2*k])
    third_sum = sum(nums[2*k: 3*k])

    max_single_sum = first_sum
    max_double_sum = first_sum + second_sum
    max_triple_sum = max_double_sum + third_sum

    first_index = 1

    while first_index + (3*k-1) < len(nums):
        first_sum = first_sum - nums[first_index-1] + nums[first_index+k-1]
        second_sum = second_sum - \
            nums[first_index + k - 1] + nums[first_index + 2*k - 1]
        third_sum = third_sum - nums[first_index +
                                     2 * k - 1] + nums[first_index + 3 * k - 1]

        if first_sum > max_single_sum:
            max_single_sum = first_sum
            single_index = [first_index]

        if max_single_sum + second_sum > max_double_sum:
            max_double_sum = max_single_sum + second_sum
            double_index = single_index + [first_index + k]

        if max_double_sum + third_sum > max_triple_sum:
            max_triple_sum = max_double_sum + third_sum
            triple_index = double_index + [first_index + 2*k]

        first_index += 1

    return triple_index

