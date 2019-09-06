
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
