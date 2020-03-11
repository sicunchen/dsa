#solution 1
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels=[]
        if root is None: return levels
        def helper(node,level):
            if len(levels)==level:levels.append([])
            levels[level].append(node.val)
            if node.left: helper(node.left,level+1)
            if node.right: helper(node.right,level+1)
        helper(root,0)
        return levels

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels=[]
        if root is None: return levels
        queue=collections.deque([root])
        level=0
        while queue:
            levels.append([])
            level_len=len(queue)
            for i in range(level_len):
                node=queue.popleft()
                levels[level].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level+=1
        return levels
                 