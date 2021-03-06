class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        flag = 1 if divisor > 0 and dividend > 0 or divisor < 0 and dividend < 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        low, upper = 0, dividend

        while low <= upper:
            middle = (low + upper) // 2
            if dividend < middle * divisor:
                upper = middle - 1
            elif (middle + 1) * divisor <= dividend:
                low = middle + 1
            else:
                return min(max(-2 ** 31, flag * middle), 2 ** 31 - 1)


#或者每次让商加倍 亦或

class Solution:
    def divide(self, divd: int, dior: int) -> int:
        res = 0
        sign =  1 if divd ^ dior >= 0 else -1
        #print(sign)
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2**31, res), 2**31-1)
