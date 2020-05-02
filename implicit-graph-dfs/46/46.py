# https://leetcode.com/problems/permutations/


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        output = []
        self.dfs(nums, [], output)
        return output

    def dfs(self, nums, workingSet, output):
        if len(nums) == len(workingSet):
            output.append(list(workingSet))
            return

        for num in nums:
            if num not in workingSet:
                workingSet.append(num)
                self.dfs(nums, workingSet, output)
                workingSet.pop()
