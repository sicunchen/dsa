# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
首先我们对数组进行排序 （此题已经排好序了）。
用两个指针(L, R)从左右开始：
如果numbers[L] + numbers[R] == target, 说明找到，返回对应的数。
如果numbers[L] + numbers[R] < target, 此时L指针右移，只有这样才可能让和更大。
反之使R左移。
L和R相遇还没有找到就说明没有解。

Time: O(n)
Space: O(1) -> 比hashtable做法更优越的点
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
        return False
