class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        result = 0
        flag = [[0 for _ in range(col)] for _ in range(row)]

        def _dfs(i, j, flag):
            if flag[i][j] == 1:
                return
            if flag[i][j] == 2:
                return

            flag[i][j] = 2

            if i + 1 < row and int(grid[i + 1][j]) == 1:
                _dfs(i + 1, j, flag)
            if j + 1 < col and int(grid[i][j + 1]) == 1:
                _dfs(i, j + 1, flag)
            if i - 1 >= 0 and int(grid[i - 1][j]) == 1:
                _dfs(i - 1, j, flag)
            if j - 1 >= 0 and int(grid[i][j - 1]) == 1:
                _dfs(i, j - 1, flag)

            flag[i][j] = 1
            return

        for i in range(row):
            for j in range(col):
                if int(grid[i][j]) == 1 and flag[i][j] != 1:
                    _dfs(i, j, flag)
                    result += 1
        return result
