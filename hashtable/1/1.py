class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToIndex = {}
        for (i, num) in enumerate(nums):
            if target-num in numsToIndex:
                return [i, numsToIndex[target-num]]
            else:
                numsToIndex[num] = i
