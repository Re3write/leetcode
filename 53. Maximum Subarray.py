#动态规划

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] < 0:
            return nums[0]
        maxs = 0
        temp_max = 0
        max_single = -999
        for num in nums:
            max_single = max(max_single,num)
            if temp_max+num < 0:
                temp_max = 0
            else:
                temp_max += num
                maxs = max(temp_max,maxs)
        if max_single < 0:
            return max_single
        return maxs