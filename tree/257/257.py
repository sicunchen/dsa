# traversal
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append("->".join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()  # 回溯，撤销到原来的状态

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()


# divide and conquer
class Solution:
    def binaryTreePaths(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        paths = []
        for path in leftPaths + rightPaths:
            paths.append(str(root.val) + "->" + path)
        return paths
