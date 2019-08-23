# 动态规划

# 中心扩散法

##判断是否为回文子串方法
def palindromic(s):
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return True
    elif len(s) % 2 == 0:
        middle = len(s) // 2
        left = s[:middle]
        right = s[middle:]
        if left == right[::-1]:
            return True
        else:
            return False
    elif len(s) % 2 == 1:
        middle = len(s) // 2
        left = s[:middle]
        right = s[middle + 1:]
        if left == right[::-1]:
            return True
        else:
            return False

print(palindromic('1221'))

class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count1 = 0
        for i in range(length):
            left = right = i
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    count1 = count1 + 1
                    left = left - 1
                    right = right + 1
                else:
                    break

        count2 = 0
        for i in range(length):
            left = i - 1
            right = i
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    count2 = count2 + 1
                    left = left - 1
                    right = right + 1
                else:
                    break
        return count1 + count2