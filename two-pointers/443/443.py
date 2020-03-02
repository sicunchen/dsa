class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        while read < len(chars):
            currChar, currCount = chars[read], 0
            while read < len(chars) and chars[read] == currChar:
                currCount += 1
                read += 1
            chars[write] = currChar
            write += 1
            if currCount > 1:
                for d in str(currCount):
                    chars[write] = d
                    write += 1
        return write
