https://leetcode.com/problems/rotate-array/

## Solution 1: using an extra array

We can use an extra array to place every element at its rotated position. And then copy the elements to the original array.

Time: O(n)
Space: O(n)

## Solution 2: reverse approach

we when rotate the array k times, k elements from the back come to the front and the rest elements shift backwards.

1. reverse the whole array
2. reverse the first k elements
3. reverse the rest n-k elements

Time: O(n)
Space: O(1)
