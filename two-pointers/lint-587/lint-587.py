# https://www.lintcode.com/problem/two-sum-unique-pairs/description?_from=ladder&&fromId=1


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        if not nums or len(nums) == 1:
            return 0
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        last_pair = (None, None)
        while left < right:
            if nums[left] + nums[right] == target:
                # 每次都和上一次找到的 pair 去比，如果重复了，就不记录
                if (nums[left], nums[right]) != last_pair:
                    count += 1
                last_pair = (nums[left], nums[right])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return count
