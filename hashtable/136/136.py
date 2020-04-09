class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set=set()
        for n in nums:
            if n in num_set:
                num_set.remove(n)
            else:
                num_set.add(n)
        return list(num_set)[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for n in nums:
            a^=n
        return a


