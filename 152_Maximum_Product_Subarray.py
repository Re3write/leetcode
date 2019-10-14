# 此题与53题类似，不同处是 5353 题的运算是加法，本题是乘法。
# 对于加法，在遍历数组中始终取max(ma + nums[i], nums[i])即可，因为无论nums[i]的正负如何，最大值一定出现在当前最大值 + 当前值 or 当前值 中的一个。
# 对与乘法，在遍历数组中，若nums[i]是负数，那么ma * nums[i]（即当前最大值与nums[i]的乘积）会变成当前最小值（负数），因此不能简单的只记录最大值。
# 本题的解题思路是同时记录当前最大值和最小值ma, mi：
# 当nums[i]是正数时，ma仍然是最大值，mi * nums[i]为最小值；
# 当nums[i]是负数时，ma将变成最小值，mi * nums[i]为最大值；
# 因此，当nums[i] < 0时，我们交换ma, mi。
# 在遍历nums过程中，每次更新res获取全局最大值。



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi = ma = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0: mi, ma = ma, mi
            ma = max(ma * nums[i], nums[i])
            mi = min(mi * nums[i], nums[i])
            res = max(res, ma)
        return res 