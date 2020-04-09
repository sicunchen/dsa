# 1
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(string):
            result = []
            for ch in string:
                if ch != "#":
                    result.append(ch)
                else:
                    if result:
                        result.pop()

            return "".join(result)

        return build(S) == build(T)


# 2
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def findNonSkippingPoint(string, i):
            skip = 0
            while i >= 0:
                if string[i] == "#":
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break
            return i

        s = len(S) - 1
        t = len(T) - 1

        while s >= 0 or t >= 0:
            s = findNonSkippingPoint(S, s)
            t = findNonSkippingPoint(T, t)

            if s >= 0 and t >= 0 and S[s] != T[t]:
                return False
            if (s >= 0) != (t >= 0):
                return False
            s -= 1
            t -= 1
        return True
