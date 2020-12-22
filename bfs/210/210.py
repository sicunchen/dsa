# https://leetcode.com/problems/course-schedule-ii/


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        node_indegree = {x: 0 for x in range(n)}
        node_neighbors = {x: [] for x in range(n)}
        # init
        for from_node, to_node in prerequisites:
            node_neighbors[to_node].append(from_node)  # []
            node_indegree[from_node] += 1

        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = collections.deque(start_nodes)
        top_sort = []

        while queue:
            node = queue.popleft()
            top_sort.append(node)

            for neighbor in node_neighbors[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(top_sort) == n:
            return top_sort
        else:
            return []
