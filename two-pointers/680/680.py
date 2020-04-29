# https://leetcode.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = self.two_pointers(s, 0, len(s) - 1)
        if left >= right:
            return True
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(
            s, left, right - 1
        )

    def is_palindrome(self, s, left, right):
        left, right = self.two_pointers(s, left, right)
        # "bddb" is a palindrome and at the end left > right
        return left >= right

    def two_pointers(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right
