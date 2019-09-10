#栈, 可以用于存储一组状态

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        length = len(s)
        result = ''
        mutil = 0
        for i in s:
            if '0' <= i <= '9':
                mutil = 10 * mutil + int(i)
            elif i == '[':
                stack.append((mutil, result))
                result = ''
                mutil = 0
            elif i == ']':
                res = stack.pop()
                result = res[1] + res[0] * result
            else:
                result += i

        return result


#dfs
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)
