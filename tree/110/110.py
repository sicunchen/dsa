# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 平衡二叉树：左子树平衡+右子树平衡+左右子树深度差<=1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.NOT_BALANCED = -1
        return self.maxDepth(root) != self.NOT_BALANCED

    # 平衡返回高度，不平衡则返回不平衡
    def maxDepth(self, node):
        if node is None:
            return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)

        if left == self.NOT_BALANCED or right == self.NOT_BALANCED:
            return self.NOT_BALANCED

        if abs(left - right) > 1:
            return self.NOT_BALANCED

        return max(left, right) + 1


# more compact solution, return both balance and height
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, node):
        if node is None:
            return True, 0
        balanced, leftHeight = self.validate(node.left)
        # if the subtree is not balanced then there's no point in recording its height
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(node.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1


# 此法更容易理解，但时间复杂度是O(NlogN)而不是O(N),因为计算树的高度(get_height)在递归和主函数递归的过程中，同一子树会被重复调用
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        if not root:
            return True

        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False

        return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1

    def get_height(self, root):
        if not root:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1
