#或者访问过的原矩阵赋值为0
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



class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count