
# https://www.lintcode.com/problem/flatten-binary-tree-to-linked-list/description?_from=ladder&&fromId=1
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# pre-order traversal, 此解法调用前必须清空last_node
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    last_node = None

    def flatten(self, root):
        # write your code here
        if root is None:
            return

        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root

        self.last_node = root
        # 因为flatten有可能会覆盖掉root.right
        right = root.right

        self.flatten(root.left)
        # 访问存好的right
        self.flatten(right)


# divide and conquer
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, root):
        if root is None:
            return None
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        # 返回第一个非空
        return right_last or left_last or root
