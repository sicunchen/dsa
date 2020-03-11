https://leetcode.com/problems/binary-tree-postorder-traversal/

## Solution 1: recursive approach

Time: O(n)\
Space: O(h) (worst case O(n), avg case O(logn), h is the height of the binary tree)

## Solution 2: modified iterative pre-order and then reverse

This time add LEFT child first so we can visit right subtree first. And then reverse the result

Time: O(n)\
Space: O(n)

## Solution 3: iterative approach + using a flag to indicate whether the node has been visited or not

For post order traversal the root node of a subtree is traversed twice but only added to the result the second time. We can use a flag to indicate the root node has been visited and only add root when the flag is true.

Time: O(n)\
Space: O(n)
