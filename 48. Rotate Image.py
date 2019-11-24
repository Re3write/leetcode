# 图像旋转，实际上是这四个位置上的数对应旋转。
# 因此，需要找到这四个位置索引的相互关系：
# matrix[i][j] \to matrix[j][n-i-1]\to matrix[n-i-1][n-j-1]\to matrix[n-j-1][i]matrix[i][j]→matrix[j][n−i−1]→matrix[n−i−1][n−j−1]→matrix[n−j−1][i]
# 注意两个边界条件
# 行只需遍历一半 ，[0,n//2)[0,n//2)
# 列需要在[i,n-i-1)[i,n−i−1)内

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n - i - 1):
                matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i] = \
                matrix[n-j-1][i], matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1]


#转置再逆序
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
