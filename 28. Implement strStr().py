#https://leetcode-cn.com/problems/implement-strstr/solution/kmp-suan-fa-xiang-jie-by-labuladong/
#KMP详解

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        start = 0
        end = start
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                start = i
                end = start + len(needle)
                if haystack[start:end] == needle:
                    return start
        return -1
