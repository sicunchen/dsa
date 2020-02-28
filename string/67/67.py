# solution 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        carry = 0

        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        for i in range(n-1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 0:
                answer.append("0")
            else:
                answer.append("1")

            carry //= 2

        if carry == 1:
            answer.append("1")
        answer.reverse()
        return "".join(answer)


# solution 2

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
