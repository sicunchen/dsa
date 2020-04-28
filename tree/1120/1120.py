#  Traverse + Divide Conquer
class Solution:
    average, node = 0, None

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.helper(root)
        return self.average

    def helper(self, root):
        if root is None:
            return 0, 0
        # 分治法计算左右子树的平均值
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        # 当前subtree的结果是左右两颗子树的和的平均值加上自身
        sum, size = left_sum + right_sum + root.val, left_size + right_size + 1
        # 打擂台比较得到最大平均值的子树
        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size

        return sum, size
