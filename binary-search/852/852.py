# https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1
        # find first index i so that nums[i]>nums[i+1]
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid
        if A[start] > A[end]:
            return start
        else:
            return end
