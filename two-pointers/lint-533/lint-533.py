# https://www.lintcode.com/problem/two-sum-closest-to-target/description?_from=ladder&&fromId=1

"""
Time: O(nlogn+n)->O(nlogn)
Space: O(1)
"""


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        diff = float("Inf")
        while left < right:
            value = nums[left] + nums[right]
            if value < target:
                diff = min(diff, target - value)
                left += 1
            else:
                diff = min(diff, value - target)
                right -= 1
        return diff
