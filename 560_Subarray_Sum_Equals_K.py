# len_nums=[0 for _ in nums]

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0
count = 0
if max(nums) == 0 and min(nums) == 0:
    for i in range(1, len(nums) + 1):
        count = count + i
    return count
for index, number in enumerate(nums):
    # if index == 0 or len_nums[index - 1] == 0:
    total = number
    index2 = index
    if total == k:
        count = count + 1
    while total != k and index2 + 1 < len(nums):
        if total + nums[index2 + 1] != k:
            total = total + nums[index2 + 1]
            index2 = index2 + 1
        elif total + nums[index2 + 1] == k:
            # len_nums[index] = index2 + 1 - index
            print(index)
            count = count + 1
            break
# elif len_nums[index-1]!=0:
print(count)


#借助累计数组sum 0-i的累加和
#解析网址https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode/

## the right 解法
_dict = {}
count = 0

# (1)使用dp[i]记录序号从0到i的数字之和
dp = [_ for _ in nums]
for t in range(1, len(nums)):
    dp[t] = dp[t - 1] + nums[t]
dp = [0] + dp

for i in range(len(dp)):

    # (2)通过搜索dp[i],确定是否存在i，从i到j对应的数字和为k。
    if _dict.get(dp[i] - k):
        count += _dict[dp[i] - k]

    # (3)dict[dp[i]]统计dp[i]出现的次数
    if _dict.get(dp[i]):
        _dict[dp[i]] += 1
    else:
        _dict[dp[i]] = 1

return count

