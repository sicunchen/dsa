# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])


"""
find the first position i so that nums[i]<=LAST NUMBER
WRONG: nums[i] <= FIRST NUMBER or < FIRST NUMBER
why? consider [1,2,3,4,5], you can't find the minimum using nums[i]<first number
A SORTED ARRAY is a subset of a ROTATED SORTED ARRAY. It's a special rotated sorted array.
"""
