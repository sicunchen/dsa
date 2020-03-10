class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans

    def traverse(self, root, ans):
        if root is None:
            return
        ans.append(root.val)
        self.traverse(root.left, ans)
        self.traverse(root.right, ans)

# solution 2


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return ans
