class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return nums[0]

        maj = {}
        for num in nums:
            maj[num] = maj.get(num, 0) + 1
            if maj[num] > (length / 2):
                return num