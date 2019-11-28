class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return nums
        start = 0
        count = 0
        for i in nums:
            if i == 0:
               nums[start] = 0
               start += 1
            elif i ==1:
                count += 1
        nums[start:start+count] = [1]*count
        nums[start+count:] = [2]*(length-start-count)

# 初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.
#
# 初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.
#
# 初始化当前考虑的元素序号 ：curr = 0.
#
# While curr <= p2 :
# 若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。
# 若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。
# 若 nums[curr] = 1 ：将指针curr右移。


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''
        荷兰三色旗问题解
        '''
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1