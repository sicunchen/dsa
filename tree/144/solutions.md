https://leetcode.com/problems/binary-tree-preorder-traversal/

Solution 1: recursive approach
Time: O(n)
Space: O(h) (worst case O(n), avg case O(logn), h is the height of the binary tree)
https://stackoverflow.com/questions/41201908/why-is-the-space-complexity-of-a-recursive-inorder-traversal-oh-and-not-on

Solution 2: iterative approach using a stack
In each iteration, we pop one node from the stack and visit this node. We need to first put the RIGHT child onto the stack so we can visit the left child first since the nature of the stack is LIFO. After that we continue to the next iteration until the stack is empty.
Time: O(n)
Space: O(n)
