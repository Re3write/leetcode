#从后往前找
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dp = [0]*len(nums)
        dp[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            for ind in range(1,nums[i]+1):
                if i+ind <= len(nums)-1 and dp[i+ind] == 1:
                    dp[i] = 1
                    break
        if dp[0] == 1:
            return True
        else:
            return False


class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i
