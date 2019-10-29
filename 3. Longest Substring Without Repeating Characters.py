class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return 1
        dict = {}
        start, tail = 0,0
        result = 0
        length_tmp = 0
        while tail <= length - 1:
            if s[tail] not in dict:
                dict[s[tail]] = 1
                length_tmp += 1
                result = max(result,length_tmp)
                tail += 1
            else:
                while(s[start] != s[tail]):
                     dict.pop(s[start])
                     start += 1
                     length_tmp -= 1
                start += 1
                tail += 1
        return result