# https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/description?_from=ladder&&fromId=1
"""
排序后双zhizhen
"""


class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        count = 0
        nums.sort()
        while left < right:
            value = nums[left] + nums[right]
            if value > target:
                right -= 1
            else:
                count += right - left
                left += 1
        return count
