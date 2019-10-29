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




class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1
