from collections import deque

from graph.utils import matrix1, matrix2, Point

DIRECTIONS1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRECTIONS2 = [(-2, 1), (-1, 2), (1, 2), (2, 1),
               (-2, -1), (-1, -2), (1, -2), (2, -1)]


# Number of Islands - bfs
class Solution1:
    def __init__(self):
        self.visited = set()

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in self.visited:
                    self.bfs(grid, i, j)
                    islands += 1

        return islands

    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        self.visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS1:
                next_x = x + delta_x
                next_y = y + delta_y
                if self.is_valid(grid, next_x, next_y):
                    queue.append((next_x, next_y))
                    self.visited.add((next_x, next_y))

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in self.visited:
            return False
        return grid[x][y]

    # def dfs(self, grid, x, y):
    #     for delta_x, delta_y in DIRECTIONS:
    #         next_x = x + delta_x
    #         next_y = y + delta_y
    #
    #         if self.is_valid(grid, next_x, next_y):
    #             self.visited.add((next_x, next_y))
    #             self.dfs(grid, next_x, next_y)


# Knight Shortest Path - bfs
class Solution2:
    def __init__(self):
        self.distance = {}

    def shortestPath(self, grid, source, destination):
        queue = deque([(source.x, source.y)])
        self.distance[(source.x, source.y)] = 0
        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return self.distance[(x, y)]
            for delta_x, delta_y in DIRECTIONS2:
                next_x, next_y = x + delta_x, y + delta_y
                if self.is_valid(grid, next_x, next_y):
                    self.distance[(next_x, next_y)] = self.distance[(x, y)] + 1
                    queue.append((next_x, next_y))

        return -1

    def is_valid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in self.distance and not grid[x][y]


# Knight Probability in Chessboard - dp
def knightProbability(N, K, r, c):

    dp = [[0 for i in range(N)] for j in range(N)]
    dp[r][c] = 1

    for step in range(1, K + 1):
        dpTemp = [[0 for i in range(N)] for j in range(N)]    # which step
        for i in range(N):
            for j in range(N):
                if dp[i][j]:     # which knight
                    for direction in DIRECTIONS2:
                        next_i, next_j = i + direction[0], j + direction[1]
                        if 0 <= next_i < N and 0 <= next_j < N:
                            dpTemp[next_i][next_j] += dp[i][j] * 0.125
        dp = dpTemp

    res = 0
    for i in range(N):
        for j in range(N):
            res += dp[i][j]
    return res


if __name__ == '__main__':
    test1 = Solution1()
    print("Number of Islands: %s" % test1.numIslands(matrix1))

    test2 = Solution2()
    print("Shortest Path: %s" % test2.shortestPath(matrix2, Point(2, 0), Point(2, 2)))

    print("Probability Knight Remains on the Board: %s" % knightProbability(3, 2, 0, 0))


