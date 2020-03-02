class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        for l in S:
            if stack and stack[-1]==l:
                stack.pop()
            else:
                stack.append(l)
        return "".join(stack)
        