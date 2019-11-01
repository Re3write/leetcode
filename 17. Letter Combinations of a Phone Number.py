#dfs 自己的方法

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
         result = []
         def recurrsion(s,i):
             if i == len(s):
                 str1 = ''
                 for x in s:
                     str1 += x
                 result.append(str1)

             else:
                 s[i] = 'a'
                 recurrsion(s,i+1)
                 s[i] = 'b'
                 recurrsion(s,i+1)
                 s[i] = 'c'
                 recurrsion(s,i+1)
         recurrsion(list(digits),0)
         return result

#python dfs

class Solution(object):
    m = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    def dfs(self, i, digits, ans, tmp):
        if i == len(digits):
            ans.append(''.join(tmp))
            return
        for ch in self.m[digits[i]]:
            tmp.append(ch)
            self.dfs(i + 1, digits, ans, tmp)
            tmp.pop()

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ans = []
        tmp = []
        self.dfs(0, digits, ans, tmp)
        return ans

