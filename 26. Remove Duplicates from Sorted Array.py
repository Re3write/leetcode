class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[start] = nums[i]
                start += 1
        nums[start] = nums[-1]
        return start + 1
