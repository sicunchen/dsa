# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        a, b, lca = self.helper(root, p, q)
        if a and b:
            return lca
        else:
            return None

    def helper(self, root, p, q):
        if root is None:
            return False, False, None
        left_a, left_b, left_node = self.helper(root.left, p, q)
        right_a, right_b, right_node = self.helper(root.right, p, q)

        a = left_a or right_a or root == p
        b = left_b or right_b or root == q

        if root == p or root == q:
            return a, b, root
        if left_node is not None and right_node is not None:
            return a, b, root
        if left_node is not None:
            return a, b, left_node
        if right_node is not None:
            return a, b, right_node
        return a, b, None

