class Solution:
    def isValid(self, s: str) -> bool:
        match = {"{": "}", "}": "{", "[": "]", "]": "[", "(": ")", ")": "("}
        stack = []
        for i, ch in enumerate(s):
            if (not stack) or ch != match[stack[-1]]:
                stack.append(ch)
            else:
                stack.pop()
        return not stack
