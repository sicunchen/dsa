class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root):
            if root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return 1 + max(lh, rh)

        if root is None:
            return 0
        lh = height(root.left)
        rh = height(root.right)
        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)
        return max(lh + rh, max(ld, rd))

    # more compact solution
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.ans = 0

        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        height(root)

        return self.ans

