#买卖股票 不会做
#一个方法团灭 6 道股票问题
#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/


# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity
#
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])


prices=[1,2,3,0,2]
if prices :
    dp = [[0 for _ in range(2)] for _ in range(len(prices))]
    for i in range(len(prices)):
        if (i - 1) == -1:
            dp[i][0] = 0
            dp[i][1] = -prices[i]
        else:
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
    print(dp)
    print(dp[len(prices) - 1][0])


else:
    print(00)