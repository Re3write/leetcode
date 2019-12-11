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





##KMP
# https://blog.csdn.net/CSDNwzl/article/details/88085359
def gen_next(s2):
    k = -1
    n = len(s2)
    j = 0
    next_list = [0 for i in range(n)]
    next_list[0] = -1                           #next数组初始值为-1
    while j < n-1:
        if k == -1 or s2[k] == s2[j]:
            k += 1
            j += 1
            next_list[j] = k                    #如果相等 则next[j+1] = k
        else:
            k = next_list[k]                    #如果不等，则将next[k]的值给k
    return next_list


def match(s1, s2, next_list):
    ans = -1
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] == s2[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next_list[j]
        if j == len(s2):
            ans = i - len(s2)
            break
    return ans


if __name__ == '__main__':
    s1 = 'ababaacc'
    s2 = 'abaa'
    next_list = gen_next(s2)
    print(next_list)
    print(match(s1, s2, next_list))
