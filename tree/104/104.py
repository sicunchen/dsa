# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# solution 1: traversal, 类似于在数组里找最大值打擂台
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        self.depth = 0
        self.traverse(root, 1)
        return self.depth

    def traverse(self, node, curr_depth):
        if node is None:
            return
        self.depth = max(self.depth, curr_depth)
        self.traverse(node.left, curr_depth + 1)
        self.traverse(node.right, curr_depth + 1)

# solution 2: divide and conquer, 整棵树的最大深度=1+max(左子树最大深度，右子树最大深度)
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        return max(leftMax, rightMax) + 1


# solution 3: bfs
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        if root is None:
            return 0
        queue = collections.deque([root])
        level = 0
        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level
