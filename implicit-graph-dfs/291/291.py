# https://leetcode.com/problems/word-pattern-ii/


class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        return self.is_match(pattern, str, {}, set())

    def is_match(self, pattern, string, mapping, used):
        if not pattern:
            return not string

        char = pattern[0]

        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.is_match(pattern[1:], string[len(word) :], mapping, used)

        for i in range(len(string)):
            word = string[: i + 1]
            if word in used:
                continue

            used.add(word)
            mapping[char] = word

            if self.is_match(pattern[1:], string[i + 1 :], mapping, used):
                return True

            del mapping[char]
            used.remove(word)

        return False
