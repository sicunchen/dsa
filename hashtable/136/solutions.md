https://leetcode.com/problems/single-number/

## Solution 1: hashtable solution

Initialize a set, add a number if it's not already in it, otherwise delete from the set. The number left will be the answer.

Time: O(n)\
Space: O(n)

## Solution 2: bitwise manipulation

XOR operation returns 0 if two inputs are the same.
a^b^a=(a^a)^b=0^b=b
XOR all bits together to find the unique number/

Time: O(n)
Space: O(1)
