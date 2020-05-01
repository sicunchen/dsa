# https://www.lintcode.com/problem/partition-array/description?_from=ladder&&fromId=1

"""
通过头尾指针跳过小于k的前缀和大于等于k的后缀，可以找到与第一个大于等于k的值和最后一个小于k的值。进行交换后可达到划分数组的目的，直到找到两个指针相遇为止。

伪代码如下：

令left = 0，right = length-1。
当nums[left] < k时，left指针向右移动。
当nums[right] >= k时，right指针向左移动。
如果left <= right，交换两个值。
如果left > right，返回left作为最终结果，否则返回第二步。

Time: O(n)
Space: O(1)
"""


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left
