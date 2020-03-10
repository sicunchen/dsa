https://leetcode.com/problems/binary-tree-postorder-traversal/

## Solution 1: recursive approach

Time: O(n)
Space: O(h) (worst case O(n), avg case O(logn), h is the height of the binary tree)

## Solution 2: modified iterative pre-order and then reverse

This time add LEFT child first so we can visit right subtree first. And then reverse the result

Time: O(n)
Space: O(n)

## Solution 3: iterative approach + using a flag to indicate whether the node has been visited
