https://leetcode.com/problems/subtree-of-another-tree/

## Solution 1: Comparing pre-order traversal of two trees

If t is a subtree of s, then t's traversal string is a substring of that of s. The reverse is not necessarily true.

Between in-order, pre-order and post-order traversals, only pre-order traversal with leaf nodes being coded as a value(null or X) could represent a tree uniquely.

Time: O(m+n)\
Space: O(m+n) (?)

## Solution 2

Search thru the bigger tree to see if there's matching nodes for smaller tree's root node. Everytime there is a match, call equalTrees method to compare two subtrees.

Time: worst case O(mn). The tighter bound would be O(n+km), where k is the number of smaller tree's root node's occurrences in the bigger tree.

Space: O(log(n)+log(m)) (?)
