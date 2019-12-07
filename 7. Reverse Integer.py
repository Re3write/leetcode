##虽然可能用不到，但我在解题过程中了解到一些关于不同语言之间取模规则的知识，在此分享一下

# 需要注意的一点就是，python的取模是根据向下取整法的，而c/c++/java是基于向零取整的。
# 例如：
# 在python中 ：-53除以10=-6 …7 所以python中 -53%10=7
# 在c语言中，-53除以10=-5 … -3 所以c语言中 -53%10=-3
# （python3中， /是精确除法，//是向下取整除法，%是求模，四舍五入取整round, 向零取整int, 向下和向上取整函数math.floor, math.ceil）

class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        result = 0
        flag = 1 if x > 0 else 0
        x = x if x > 0 else -x

        while x >= 1:
            mod = x % 10
            result = result * 10 + mod
            x = x // 10

        if flag != 1:
            result = -result
        if result > 2 ** 31 - 1 or result < -(2 ** 31):
            return 0
        return result