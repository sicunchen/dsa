# https://leetcode.com/problems/clone-graph/

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        root = node
        if node is None:
            return node
        # 1. Find all the points
        nodes = self.getNodes(node)

        # 2. Copy all the points, store the old->new mapping in a hashmap
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # 3. Copy all the edges
        for node in nodes:
            new_node = mapping[node]
            for n in node.neighbors:
                new_neighbor = mapping[n]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node):
        queue = collections.deque([node])
        visited = set([node])

        while queue:
            head = queue.popleft()
            for n in head.neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
        return visited


"""
1. 代码逻辑分开，不要想着一次性完成多个任务
2. In BFS pay attention to where to add node to the visited set. It must be after the queue append instead of the queue popleft because.
3. The time complexity of BFS is O(M+N),M is number of edges and N number of points.

https://discuss.codechef.com/t/time-complexity-of-bfs-and-dfs/2464
"""
