class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def gen(i, count, pos, tmp):
            if i == 2 * n:
                result.append(''.join(tmp))
                return
            else:
                if pos + 1 <= n:
                    tmp.append('(')
                    gen(i + 1, count + 1, pos + 1, tmp)
                    tmp.pop()
                if count - 1 >= 0:
                    tmp.append(')')
                    gen(i + 1, count - 1, pos, tmp)
                    tmp.pop()
                return

        if n == 0:
            return []

        gen(1, 1, 1, ['('])
        return result



####

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号已经使用的个数
            :param right: 右括号已经使用的个数
            :return:
            """
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res