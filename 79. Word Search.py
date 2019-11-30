class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        flag = [[0]*len(board[0]) for _ in range(len(board))]
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(i,j,word):
            if board[i][j] == word[0]:
                if (len(word) == 1):
                    return True
                for d in direction:
                    tempx,tempy = i+d[0],j+d[1]
                    if tempx>=0 and tempx<len(board) and tempy>=0 and tempy<len(board[0]) and flag[tempx][tempy] == 0:
                        flag[tempx][tempy] = 1
                        if dfs(tempx,tempy,word[1:]):
                            return True
                        flag[tempx][tempy] = 0
                return False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                flag[i][j] = 1
                if board[i][j] == word[0] and dfs(i,j,word):
                    return True
                flag[i][j] = 0
        return False