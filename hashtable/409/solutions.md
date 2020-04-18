https://leetcode.com/problems/longest-palindrome/

## Solution 1

1. Keep track of each letter's frequencies and initialize an odd count holder.

2. Loop thru the count object, if the freq is even, add it to ans, else add (freq-1) to ans and add 1 to the odd count holder.

3. If the final odd count > 0, add 1 to ans

Time: O(N)  
Space: O(N)

## Solution 2

Same idea as solution 1, but using a set instead to keep track of the letters with odd number frequencies. If the final set is not empty it means we have to remove (setSize-1) letters from the original string to build a palidrome.

Time: O(N)  
Space: O(N)
