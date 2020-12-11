import random


class RandomizedSet:
    def __init__(self):
        self._nums = []
        self._index_map = dict()

    def insert(self, val):
        if val not in self._index_map:
            self._nums.append(val)
            self._index_map[val] = len(self._nums) - 1
            return True

        return False

    def remove(self, val):
        if val in self._index_map:
            r_index = self._index_map[val]
            self._nums[-1], self._nums[r_index] = self._nums[r_index], self._nums[-1]
            self._index_map[self._nums[r_index]] = r_index
            self._nums.pop()
            del self._index_map[val]
            return True
        return False

    def getRandom(self):
        return self._nums[random.randint(0, len(self._nums)-1)]

