class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return []
        def helper(nums, temp ,pos):
            result.append(temp[:])
            if not nums:
                return
            for i in range(pos,len(nums)):
                 temp.append(nums[i])
                 helper(nums[:i]+nums[i+1:],temp,i)
                 temp.pop()
        helper(nums,[],0)
        return result



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return []
        def helper(nums, temp ,pos):
            result.append(temp[:])
            if pos == len(nums):
                return
            for i in range(pos,len(nums)):
                 temp.append(nums[i])
                 helper(nums,temp,i+1)
                 temp.pop()
        helper(nums,[],0)
        return result