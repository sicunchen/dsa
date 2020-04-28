# https://leetcode.com/problems/validate-binary-search-tree/


# solution 1: 根据BST的特性进行in-order traversal
"""
if a binary tree is a bst, then its in-order traverse result would be an array in ascending order. 
However we don't need to store the traverse result, we only need to compare the current node with 
the last node and see if its value is larger than the last node.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        self.isValid = True
        self.lastNode = None
        self.inorderTraverse(root)
        return self.isValid

    def inorderTraverse(self, node):
        if node is None:
            return

        self.inorderTraverse(node.left)

        if self.lastNode is not None and self.lastNode.val >= node.val:
            self.isValid = False
            return

        self.lastNode = node

        self.inorderTraverse(node.right)


# solution 2：divide and conquer
"""
题目对BST的定义：
左子树的所有节点值<根节点值 => 如果左子树的最大值<根节点值，则满足条件
右子树的所有节点值>根节点值 => 如果右子树的最小值>根节点值，则满足条件
分治的返回值：isValid, minNode, maxNode
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        isValid, minVal, maxVal = self.divideConquer(root)
        return isValid

    def divideConquer(self, root):
        if root is None:
            return True, None, None
        leftValid, leftMin, leftMax = self.divideConquer(root.left)
        rightValid, rightMin, rightMax = self.divideConquer(root.right)

        if not leftValid or not rightValid:
            return False, None, None

        if leftMax is not None and leftMax >= root.val:
            return False, None, None

        if rightMin is not None and rightMin <= root.val:
            return False, None, None
        # is BST
        minVal = leftMin if leftMin is not None else root.val
        maxVal = rightMax if rightMax is not None else root.val
        return True, minVal, maxVal

