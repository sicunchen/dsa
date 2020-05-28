# solution 1: brute force. Basically check every substring to see it's a palindrome. O(N^3). TLE
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s is None:
#             return None

#         for length in range(len(s), 0, -1):  # O(N)
#             for i in range(len(s) - length + 1):  # O(N)
#                 if self.is_palindrome(s, i, i + length - 1):  # O(N)
#                     return s[i : i + length]

#         return ""

#     def is_palindrome(self, s, left, right):
#         while left < right and s[left] == s[right]:
#             left += 1
#             right -= 1

#         return left >= right

"""
基于中心点的枚举。由回文串正序和反序的性质相同，可以得出一个性质，如果一个字符串，其中心不是回文串，那么它一定不是个回文串。所以我们每次从中心开始，向两边延展首尾，判断是否是回文串。
枚举回文中心，一个string有n个奇数长度的回文串中心点，有n-1个偶数长度的回文串中心点，所以一共有(2n-1)个中心点，时间复杂度O(N)。
向两边延展检查两字符是否相等，时间复杂度O(N)。
总体复杂度O(N^2)。
"""


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s is None:
#             return None
#         start, longest = 0, 0
#         for middle in range(len(s)):
#             # odd
#             left, right = middle, middle
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             if longest < right - left - 1:
#                 longest = right - left - 1
#                 start = left + 1

#             # even
#             left, right = middle, middle + 1
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             if longest < right - left - 1:
#                 longest = right - left - 1
#                 start = left + 1
#         return s[start : start + longest]

"""
以上代码重复问题严重，优化如下：
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None

        answer = (0, 0)
        for middle in range(len(s)):
            # odd
            answer = max(answer, self.get_palindrome_len_and_start(s, middle, middle))
            # even
            answer = max(
                answer, self.get_palindrome_len_and_start(s, middle, middle + 1)
            )

        length, start = answer
        return s[start : start + length]

    def get_palindrome_len_and_start(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1


"""
x[...]y是回文串的条件：x==y&&中间...这一段是回文串
isPalindrome[i][j]表示i到j这一段子串是不是回文串
isPalindrome[i][j]=isPalindrome[i+1][j-1]&&s[i]==s[j]
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None

        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True

        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j

        return s[start : end + 1]

