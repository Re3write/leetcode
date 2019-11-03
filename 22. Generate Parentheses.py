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