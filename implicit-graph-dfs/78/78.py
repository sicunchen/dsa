# https://leetcode.com/problems/subsets/
"""
此题要点：
1. dfs是一种回溯(backtracking)算法
2. python的deep copy如果是一重list可用[:]来进行，再多就不行了
"""


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        combinations = []
        combination = []
        # 用lintcode需sort
        # nums.sort()
        self.dfs1(0, nums, combination, combinations)
        return combinations

    """
    Solution 1: dfs简单递归，对于每个数，考虑是否使用，是append到当前subset再dfs, 否pop再dfs
    此法的答案顺序为：[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    """

    def dfs1(self, index, nums, combination, combinations):
        # 递归出口
        if index == len(nums):
            # deep copy,如果这里不使用 deep copy， 就会导致combinations里的每一项都指向了combination的reference
            combinations.append(combination[:])
            return

        # 递归拆解
        # 选了nums[index]
        combination.append(nums[index])
        self.dfs1(index + 1, nums, combination, combinations)

        # 不选nums[index]
        combination.pop(-1)
        self.dfs1(index + 1, nums, combination, combinations)

    """
    Solution 2: 更通用的，可拓展到全排列问题的dfs
    此法的答案顺序为：[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """

    def dfs2(self, nums, index, combination, combinations):
        combinations.append(combination[:])
        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs2(nums, i + 1, combination, combinations)
            combination.pop(-1)
