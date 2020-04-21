# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    islands += 1

        return islands

    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = "0"
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y):
                    continue
                queue.append((next_x, next_y))
                grid[next_x][next_y] = "0"

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == "1"


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
