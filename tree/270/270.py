# https://leetcode.com/problems/closest-binary-search-tree-value/


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        upper = root
        lower = root
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val
