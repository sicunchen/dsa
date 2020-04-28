class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        ans = 1
        base = a
        while n > 0:
            if n % 2 == 1:
                ans = (ans * base) % b
            base = base * base % b
            n = n // 2
        return ans % b

