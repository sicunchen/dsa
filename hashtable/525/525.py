class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash = {}
        sum = 0
        ans = 0
        for i in range(len(nums)):
            sum += -1 if nums[i] == 0 else 1
            if sum == 0:
                ans = i + 1
            if sum not in hash:
                hash[sum] = i
            else:
                ans = max(ans, i - hash[sum])
        return ans
