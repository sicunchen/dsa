"""
O(NM)解法。思考：这段代码有什么问题？
无论用什么语言，用[:]，或者slice都会生成一个新的字符串，时间和空间上都有浪费。
"""
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0
#         for i in range(len(haystack)):
#             if haystack[i:i+len(needle)]==needle:
#                 return i
#         return -1

# 优化如下：
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # 这里为什么要加一？想象一下haystack和needle相同的情况，如果不加一就不会进入for loop
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1


"""
利用Robin Karp算法，利用哈希函数将O(m)的复杂度优化为O(1)，m为目标串的长度。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  #
        if haystack is None or needle is None:
            return -1
        m, n = len(needle), len(haystack)
        if m == 0:
            return 0
        HASH_SIZE, BASE = 10 ** 6, 31
        # 31^m
        power = 1
        for i in range(m):
            power = (power * BASE) % HASH_SIZE

        target_code = 0
        for i in range(m):
            target_code = (target_code * BASE + ord(needle[i])) % HASH_SIZE

        hash_code = 0
        for i in range(n):
            hash_code = (hash_code * BASE + ord(haystack[i])) % HASH_SIZE
            if i < m - 1:
                continue

            if i >= m:
                hash_code = (hash_code - ord(haystack[i - m]) * power) % HASH_SIZE
                if hash_code < 0:
                    hash_code += HASH_SIZE

            if hash_code == target_code:
                if haystack[i - m + 1 : i + 1] == needle:
                    return i - m + 1
        return -1
