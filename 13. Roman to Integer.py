class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num = 0
        for i in range(len(s)-1):
            if roma_nums[s[i]]>=roma_nums[s[i+1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = s[len(s)-1]
        num = num + roma_nums[last_num]
        return num
