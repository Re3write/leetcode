nums = [2,7,9,3,1]

length = len(nums)
dp = [0 for _ in range(length + 1)]
dp[1] = nums[0]
for i in range(1, length):
    dp[i + 1] = max(nums[i] + dp[i - 1], dp[i])

print(dp[length])