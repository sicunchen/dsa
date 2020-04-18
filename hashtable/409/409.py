class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        odd_count = 0
        for freq in collections.Counter(s).values():
            if freq % 2 == 0:
                ans += freq
            else:
                ans += freq - 1
                odd_count += 1
        return ans if odd_count == 0 else ans + 1


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_set = set()
        for l in s:
            if l not in odd_set:
                odd_set.add(l)
            else:
                odd_set.remove(l)
        return len(s) if len(odd_set) == 0 else len(s) - len(odd_set) + 1
