class Solution:
    def numSquares(self, n: int) -> int:
        dp = [100 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(2,int(n**0.5)+1):
                if j*j <= dp[i] and i-j*j >=0:
                    dp[i] = min(dp[i-j*j]+1,dp[i])
        return dp[n]

#由于是广度遍历，所以当遍历到0时，肯定是最短路径

class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step

    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value, self.step)


class Solution:

    def numSquares(self, n: int) -> int:

        queue = [node(n)]
        visited = set([node(n).value])

        while queue:

            vertex = queue.pop(0)

            residuals = [vertex.value - n * n for n in range(1, int(vertex.value ** .5) + 1)]

            for i in residuals:

                new_vertex = node(i, vertex.step + 1)

                if i == 0:
                    return new_vertex.step

                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)

        return -1

###我的做法
class Solution:
    def numSquares(self, n: int) -> int:
        queue = []
        queue.append((n, 0))
        visit = set((n, 0))

        while queue:
            node = queue.pop(0)
            for i in range(1, int(node[0] ** 0.5) + 1):
                if node[0] - i * i == 0:
                    return node[1] + 1
                elif (node[0] - i * i, node[1] + 1) not in visit and node[0] > i * i:
                    visit.add((node[0] - i * i, node[1] + 1))
                    queue.append((node[0] - i * i, node[1] + 1))
