# solution 1
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            result.append(root.val)
            traverse(root.right)

        traverse(root)
        return result


# solution 2
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        curr = root
        while len(stack) != 0 or curr != None:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
