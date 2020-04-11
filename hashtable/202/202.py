class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            sum = 0
            while n > 0:
                n, remainder = divmod(n, 10)
                sum += remainder * remainder
            return sum

        hashset = set()
        while n != 1 and n not in hashset:
            hashset.add(n)
            n = getNext(n)
        return n == 1

