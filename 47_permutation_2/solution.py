class Solution:
    def permutation(self, nums):
        if not nums:
            return []
        res = []
        path = []

        self._permutation(nums, path, res)
        return res

    def _permutation(self, nums, path, res):
        if not nums:
            res.append(list(path))
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            else:
                visited.add(nums[i])
                self._permutation(nums[:i] + nums[i+1:], path + [nums[i]], res)
