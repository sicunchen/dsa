# https://leetcode.com/problems/two-sum-iii-data-structure-design/


class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.counter[number] = self.counter.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.counter:
            if num * 2 == value and self.counter[num] > 1:
                return True
            if num * 2 != value and value - num in self.counter:
                return True
        return False

