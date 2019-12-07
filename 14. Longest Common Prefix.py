class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        tem = strs[0]
        flag = 1
        result = ""
        length = [len(x) for x in strs]
        minl = min(length)
        for i in range(minl):
            for s in strs[1:]:
                if tem[i] != s[i]:
                    flag = 0
                    break
            if flag == 0:
                break
            result+=tem[i]
        return result