# solution 1
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            sum += map[s[i]]
            if i > 0 and map[s[i-1]] < map[s[i]]:
                sum -= 2*map[s[i-1]]
        return sum


# solution 2
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        # will get index out of range error if using range(len(s))
        for i in range(len(s)-1):
            if map[s[i]] < map[s[i+1]]:
                sum -= map[s[i]]
            else:
                sum += map[s[i]]
        return sum+map[s[-1]]
