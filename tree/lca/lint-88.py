# https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-tree/description?_from=ladder&&fromId=1


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # 四种情况
        # A,B 都在root为根的二叉树里，return lca(A,B)
        # 如果A,B都不在root为根的二叉树里，return None
        # 如果只有A在，return A
        # 如果只有B在，return B

        # A & 下面有B => A
        # B & 下面有A => B
        # A & 下面啥都没有 => A
        # B & 下面啥都有 => B
        if root is None:
            return None
        if root is A or root is B:
            return root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        if left is not None and right is not None:
            return root
        if left is not None:
            return left

        if right is not None:
            return right
        return None
