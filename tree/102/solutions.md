https://leetcode.com/problems/binary-tree-level-order-traversal/

## Solution 1: recursive approach

Time: O(n) since each node is processed exactly once\
Space: O(n)

## Solution 2: iterative approach using a queue

1. Initiate queue with a root node and start from level 0
2. While queue is not empty:\
   Start the current level by adding an empty list into the levels output
   Compute how many elements should be on the current level - the current queue length
   Pop all the elements at the front(queue length) and add them to the current level list
   Push every element's childs to the queue (left first, right second)
   Go to the next level\

Time: O(n)
Space: O(n)
