class Solution:
    def permute(self, nums):
        res = []
        self.back_tack(nums, res, [])
        return res

    def back_tack(self, candidates, res, track):
        if not candidates:
            res.append(list(track))
            return
        for i in range(len(candidates)):
            self.back_tack(candidates[:i] + candidates[i+1:],
                           res, track + [candidates[i]])


"""
nums = [1, 2]

bt([1, 2], [], [])
    i = 0
    bt([2], [], [1])
        i = 0
        bt([], [], [1, 2])
        res = [[1, 2]]
        done []
    done [2]
    i = 1
    bt([1], [[1,2]], [2])
        i = 0
        bt([], [[1, 2]], [2, 1])
        res = [[1,2], [2,1]]
        done []
    done [1, 2]

"""

