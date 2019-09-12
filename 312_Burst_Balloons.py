# 我分别使用了三种方法来解决这道题目，并做了一些思考。回溯法、记忆化递归、自底向上的动态规划，欢迎学习交流，视频地址：https://www.bilibili.com/video/av45180542


nums = [3,1,5,8]
length = len(nums)
dp = [[0 for _ in range(length + 2)] for _ in range(length + 2)]
nums.insert(0, 1)
nums.append(1)
print(nums)
print(dp)
for l in range(1, length + 1):
    # print(l)
    for i in range(1, length - l + 2):
        j = i + l -1
        print(i,j)
        for k in range(i, j + 1):
            print(k)
            dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[k] * nums[i - 1] * nums[j + 1])
print(dp[1][length])
