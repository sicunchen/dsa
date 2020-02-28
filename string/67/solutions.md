https://leetcode.com/problems/add-binary/

## Solution 1: bit-by-bit computation

Treat binary addition just like regular addition.

Time: O(max(n,m))
Space: O(max(n,m))

## Solution 2: bit manipulation

https://www.youtube.com/watch?v=qq64FrA2UXQ

while carry is not zero:

1. use & to find positions that need carries
2. use ^ to simulate additions
3. left shift carries and repeat first two steps
