# https://leetcode.com/problems/insert-delete-getrandom-o1/
import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.val2index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val2index:
            return False
        self.nums.append(val)
        self.val2index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val2index:
            return False
        index = self.val2index[val]
        last = self.nums[-1]

        # move the last element to index
        self.nums[index] = last
        self.val2index[last] = index

        # remove the last element
        self.nums.pop()
        del self.val2index[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
