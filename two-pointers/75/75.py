# https://leetcode.com/problems/sort-colors/


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    # one-pass
    def sortColors(self, nums):
        # write your code here
        left, index, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1

    # two-pass
    def sortColors(self, nums):
        # write your code here
        index = self.sort(nums, 0, 0)
        self.sort(nums, 1, index)

    def sort(self, A, flag, index):
        start, end = index, len(A) - 1
        while start <= end:
            while start <= end and A[start] == flag:
                start += 1
            while start <= end and A[end] != flag:
                end -= 1
            if start <= end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        return start
