
#
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total % 2 != 0:
#             return False
#         half = int(total / 2)
#         count = [0 for _ in range(half + 1)]
#         for i in range(1, len(count)):
#             for num in nums:
#                 if i - num < 0:
#                     continue
#                 else:
#                     count[i] = max(count[i], count[i - num] + 1)
#
#         if count[half] > 0:
#             return True
import numpy as np
nums=[1,2,5]
total = sum(nums)
# if total % 2 != 0:
#     return False
half = int(total / 2)
dp = [[0 for _ in range(half + 1)] for _ in range(len(nums) + 1)]
print((np.array(dp).shape))
print(dp)
for i in range(1, len(nums) + 1):
    for j in range(1, half + 1):
        dp[i][j]=dp[i-1][j]
        if j - nums[i - 1] < 0:
            continue
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - nums[i - 1]] + nums[i-1])

print(dp[len(nums)][half])



####下面是时间通过的0,1背包

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)

        # 特判，如果整个数组的和都不是偶数，就无法平分
        s = sum(nums)
        if s & 1 == 1:
            return False

        # 二维 dp 问题：背包的容量
        target = s // 2
        dp = [[False for _ in range(target + 1)] for _ in range(size)]

        # 先写第 1 行：看看第 1 个数是不是能够刚好填满容量为 target
        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True
        # i 表示物品索引
        for i in range(1, size):
            # j 表示容量
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]
