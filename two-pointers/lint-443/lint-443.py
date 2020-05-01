# https://www.lintcode.com/problem/two-sum-greater-than-target/description?_from=ladder&&fromId=1
"""
Time: O(nlogn+n)->O(nlogn)
Space: O(1)
"""


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            value = nums[left] + nums[right]
            if value <= target:
                left += 1
            else:
                count += right - left
                right -= 1
        return count
