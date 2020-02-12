class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqIndex = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[uniqIndex]:
                nums[uniqIndex+1] = nums[i]
                uniqIndex += 1
        return len(nums[:uniqIndex+1])
