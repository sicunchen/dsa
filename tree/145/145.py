# solution 1
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root is None:
            return
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)


# solution 2
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result[::-1]

#solution 3
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        if root: stack.append((root,False))
        while stack:
            curr,visited=stack.pop()
            if visited:
                result.append(curr.val)
            else:
                stack.append((curr,True))
                if curr.right: stack.append((curr.right,False))
                if curr.left: stack.append((curr.left,False))
        return result
