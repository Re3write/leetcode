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