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

##二分法
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size

        cell = [nums[0]]
        for num in nums[1:]:
            if num > cell[-1]:
                cell.append(num)
                continue

            l, r = 0, len(cell) - 1
            while l < r:
                mid = l + (r - l) // 2
                if cell[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num
        return len(cell)
