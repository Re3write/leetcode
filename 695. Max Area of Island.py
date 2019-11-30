class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        flag = [[0] * len(grid[0]) for _ in range(len(grid))]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = []

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or flag[i][j] == 1 or grid[i][j] == 0:
                return 0
            else:
                a = 0
                flag[i][j] = 1
                for d in direction:
                    a += dfs(i + d[0], j + d[1])
                return a + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and flag[i][j] == 0:
                    result.append(dfs(i, j))
        if not result:
            return 0
        return max(result)



