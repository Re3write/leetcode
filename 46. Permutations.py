class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        result = []
        def helper(temp,nums_tmp):
            if len(nums_tmp) == 0:
                result.append(temp[:])
            for i in range(len(nums_tmp)):
                temp.append(nums_tmp[i])
                helper(temp,nums_tmp[:i]+nums_tmp[i+1:])
                temp.pop(-1)
        helper([],nums)
        return result