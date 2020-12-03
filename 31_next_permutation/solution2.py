class Solution:
    def next_permutation(self, nums):
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        if i == 0:
            self.reverse(nums, 0, len(nums)-1)
        else:
            for j in range(len(nums)-1, i-1, -1):
                if nums[j] > nums[i-1]:
                    break

            nums[j], nums[i-1] = nums[i-1], nums[j]
            self.reverse(nums, i+1, len(nums) - 1)

    def reverse(self, nums, i, j):
        """
        reverse the elements in nums[i: j+1]
        """
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


"""
nums = [1, 2, 3]

i = 2
for j in range(2, 1, -1):
    j = 2, nums[2] > nums[1]
nums = [1, 3, 2]

nums = [3, 2, 1]
i = 2,
i = 0, nums = [1, 2, 3]

nums = [1, 1, 5]
i = 2
j = 2
nums = [1, 5, 1]

"""
