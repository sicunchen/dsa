# solution 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
            if count[n] > len(nums)/2:
                return n


# solution 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # double slash is for integer division
        return nums[len(nums)//2]


# solution 3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count = 0

        for n in nums:
            if count == 0:
                maj = n
            count += (1 if n == maj else -1)
        return maj
