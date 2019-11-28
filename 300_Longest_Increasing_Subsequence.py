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

#
# 1、设置一个有序数组 tail，初始时为空；
#
# 数组命名为 tail 即 PPT 中各个行表示的数组（是一个“上升子序列”）的结尾，注意：有序数组 tail 虽然有“上升”的性质，但它不是每时每刻都表示问题中的“最长上升子序列”（下文还会强调），不能命名为 LIS，有序数组 tail 是用于求解 LIS 问题的辅助数组。
#
# 2、在遍历数组 nums 的过程中，每来一个新数 num，如果这个数严格大于有序数组 tail 的最后一个元素，就把 num 放在有序数组 tail 的后面，否则进入第 3 点；
#
# 注意：这里的大于是“严格”大于，不包括等于的情况。
#
# 3、在有序数组 tail 中查找第 1 个等于大于 num 的那个数，试图让它变小；
#
# 如果有序数组 tail 中存在等于 num 的元素，什么都不做，因为以 num 结尾的最短的“上升子序列”已经存在；
# 如果有序数组 tail 中存在大于 num 的元素，找到第 1 个，让它变小，这样我们就找到了一个“结尾更小”的“相同长度”的上升子序列。
# 这一步可以使用“二分查找法”。
#
# 4、遍历新的数 num ，先尝试上述第 2 点，第 2 点行不通则执行第 3 点，直到遍历完整个数组 nums，最终有序数组 tail 的长度，就是所求的“最长上升子序列”的长度。
#
