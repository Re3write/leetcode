class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result=bin(x^y).replace('0b','')
        count=0
        for i in result:
            if i== '1':
               count+=1
        return count


#
# class Solution {
#     public int hammingDistance(int x, int y) {
#         int ans = 0;
#         while(x != 0 || y != 0){
#             if((x & 1) != (y & 1))
#                 ans++;
#             x>>=1;
#             y>>=1;
#         }
#         return ans;
#     }
# }
#
# python 位运算
# 与运算 &
# 　　　　与运算就是比较a和b的二进制如果位数都为1则算为1，如果不想同或都为0则算为0。然后再把答案的二进制转为10进制。
#
# 　　或运算 |
# 　　　　或运算正好与与运算相反，如果位数都不为0则算为1，否则算为0。
#
# 　　异或操作
# 　　　　异或操作是位数不想同则算为1，否则算为0。
#
# 　　1.左移运算符  <<
# 　　　　方法:X<<N 将一个数字X所对应的二进制数向左移动N位.
# 　　　　举例:
# 　　　　3<<2
# 　　　　解法:11向左移动两位变为1100,即12 .
#
# 　　2.右移动运算符  >>
# 　　　　方法:X>>N 将一个数字X所对应的二进制数向右移动N位.
# 　　　　举例:
# 　　　　3>>2
# 　　　　解法:11向右移动两位变为0.
# 　　　　10>>1
# 　　　　解法:10的二进制是1010,向右边移动一位是101,即5.