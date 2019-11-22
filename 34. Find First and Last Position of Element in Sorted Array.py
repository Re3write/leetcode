class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def searchLeft():
            left = 0
            right = len(nums) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid

            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            return -1

        def searchRight():
            left = 0
            right = len(nums) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid
            if nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            return -1

        return [searchLeft(), searchRight()]