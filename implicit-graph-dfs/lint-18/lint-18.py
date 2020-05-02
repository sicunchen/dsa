# https://www.lintcode.com/problem/subsets-ii/description?_from=ladder&&fromId=1

"""
此题是subsets的follow-up
"""


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        combinations = []
        combination = []
        nums.sort()
        self.dfs(nums, 0, combination, combinations)
        # print(combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(combination[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop(-1)

#iterative solution
# class Solution:
#     """
#     @param nums: A set of numbers.
#     @return: A list of lists. All valid subsets.
#     """

#     def subsetsWithDup(self, nums):
#         nums.sort()
#         subsets = [[]]
#         indexes = [-1]

#         for i in range(len(nums)):
#             size = len(subsets)
#             for s in range(size):
#                 if i > 0 and nums[i] == nums[i - 1] and indexes[s] != i - 1:
#                     continue
#                 subsets.append(list(subsets[s]))
#                 subsets[-1].append(nums[i])
#                 indexes.append(i)
#         return subsets
