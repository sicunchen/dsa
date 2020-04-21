# https://leetcode.com/problems/number-of-islands/


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1

        return islands

    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        # 圆括号传的是tuple,value copy
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            # 坐标变换数组
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]


"""
这道题能用DFS吗？
能，但可能会造成stack overflow
考虑如下情况：m*n/2, 即大约有一半的点都连接到，栈空间stack memory会占到O(MN)
11111
00001
11111
10000
11111
00001
11111
...
"""
