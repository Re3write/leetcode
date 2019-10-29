class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ''
        if length == 1:
            return s

        maxlen = 1
        tmp_len = 1
        start = 0
        for i in range(length):
            left, right = i - 1, i + 1
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    tmp_len += 2
                    left -= 1
                    right += 1
                else:
                    break

            maxlen, start = (tmp_len, left + 1) if tmp_len > maxlen else (maxlen, start)
            tmp_len = 1

        tmp_len = 0
        for i in range(length):
            left, right = i - 1, i
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    tmp_len += 2
                    left -= 1
                    right += 1
                else:
                    break
            maxlen, start = (tmp_len, left + 1) if tmp_len > maxlen else (maxlen, start)
            tmp_len = 0

        return s[start:start + maxlen]
