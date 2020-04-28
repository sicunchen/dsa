# 使用 Divide Conquer + Traverse 的方法。
class Solution:
    def findSubtree(self, root):
        self.minimum_weight = float("inf")
        self.minimum_subtree_root = None
        self.getTreeSum(root)

        return self.minimum_subtree_root

    # 得到 root 为根的二叉树的所有节点之和
    # 顺便打个擂台求出 minimum subtree
    def getTreeSum(self, root):
        if root is None:
            return 0

        left_weight = self.getTreeSum(root.left)
        right_weight = self.getTreeSum(root.right)
        root_weight = left_weight + right_weight + root.val

        if root_weight < self.minimum_weight:
            self.minimum_weight = root_weight
            self.minimum_subtree_root = root

        return root_weight


# 使用纯 Divide & Conquer 的方法。好处是避免使用全局变量。
class Solution:
    def findSubtree(self, root):
        minimum, subtree, sum = self.helper(root)
        return subtree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)

        sum = left_sum + right_sum + root.val
        if left_minimum == min(left_minimum, right_minimum, sum):
            return left_minimum, left_subtree, sum
        if right_minimum == min(left_minimum, right_minimum, sum):
            return right_minimum, right_subtree, sum

        return sum, root, sum
