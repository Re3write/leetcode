#DFS解法，超时
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(word):
            if not word:
                return True
            for w in wordDict:
                length = len(w)
                if word[:length] == w:
                    if helper(word[length:]):
                        return True
            return False
        return helper(s)

#动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]
