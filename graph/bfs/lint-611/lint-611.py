# https://www.lintcode.com/problem/knight-shortest-path/description?_from=ladder&&fromId=1

DIRECTIONS = [
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
]


class Solution:

    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))
        return -1

    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])

        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        return not grid[x][y]


# https://leetcode.com/problems/minimum-knight-moves/discuss/589594/Python-bfs()-%2B-using-idea-of-Diagonal-Symmetry


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        queue = collections.deque([(0, 0, 0)])
        directions = [
            [-2, 1],
            [-2, -1],
            [-1, 2],
            [-1, -2],
            [1, 2],
            [1, -2],
            [2, 1],
            [2, -1],
        ]
        visited = set()
        visited.add((0, 0))
        while queue:
            cur_r, cur_c, move = queue.popleft()
            for d_r, d_c in directions:
                i_r, i_c = cur_r + d_r, cur_c + d_c
                if (i_r, i_c) not in visited:
                    if i_r == x and i_c == y:
                        return move + 1
                    queue.append((i_r, i_c, move + 1))
                    visited.add((i_r, i_c))

