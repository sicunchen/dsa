# solution 1
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preOrder(node):
            if node is None:
                return "X"
            return '#'+str(node.val)+" "+preOrder(node.left)+" "+preOrder(node.right)
        s1 = preOrder(s)
        s2 = preOrder(t)
        return s2 in s1

# solution 2


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equalTrees(t1, t2):
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            elif t1.val != t2.val:
                return False
            else:
                return equalTrees(t1.left, t2.left) and equalTrees(t1.right, t2.right)

        if s is None:
            return False
        return equalTrees(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
