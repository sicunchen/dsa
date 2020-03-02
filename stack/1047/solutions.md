https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

The idea is to use a stack to keep track of unique letters. If current string letter is equal to the last element of the stack, pop that element off the stack(eliminate duplicates) or else add the current letter on to the stack. Finally return the stack as string.

Time: O(n)
Space: O(n-d), d is a total length for all duplicates
