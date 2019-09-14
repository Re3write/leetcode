class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        length = len(nums)
        dp = [1 for _ in range(length)]

        for i in range(1,length):
            for index in range(i):
                if nums[i] > nums[index]:
                    dp[i] = max(dp[i],dp[index]+1)
        return max(dp)
