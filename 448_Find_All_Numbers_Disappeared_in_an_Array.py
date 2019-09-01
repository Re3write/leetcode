class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=[1 for _ in range(len(nums))]
        for number in nums:
            if x[number-1] ==1:
               x[number-1] =0
        y=[]
        for index,value in enumerate(x):
            if value == 1:
                y.append(index+1)
        return y

def findDisappearedNumbers(nums):
    # 使用set
    return list(set(range(1, len(nums) + 1)) - set(nums))

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums=[0]+nums
        n=len(nums)
        for i in range(1,n):
            while nums[i]!=i:
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
                if nums[nums[i]]==nums[i]:
                    break
        return [i for i in range(1,n) if nums[i]!=i]

    # 扫描位置（i），交换次数，原数组
    # 0
    # 0[0, 4, 3, 2, 7, 8, 2, 3, 1]
    # 1
    # 1[0, 7, 3, 2, 4, 8, 2, 3, 1]
    # 1
    # 2[0, 3, 3, 2, 4, 8, 2, 7, 1]
    # 1
    # 3[0, 2, 3, 3, 4, 8, 2, 7, 1]
    # 1
    # 4[0, 3, 2, 3, 4, 8, 2, 7, 1]
    # 5
    # 5[0, 3, 2, 3, 4, 1, 2, 7, 8]
    # 5
    # 6[0, 1, 2, 3, 4, 3, 2, 7, 8]
    # 在位置1的时候，4
    # 次交换把2 - 4
    # 都换对了，所以直接跳到5，然后再换两次就有序了。
    # 因为每个数字一开始都不在正确的位置上，所以交换次数很高，6
    # 次是正确次数，实际上还会有第7次一个无用交换


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
        # 举个例子：
        # 原始数组：[4,3,2,7,8,2,3,1]
        # 重置后为：[-4,-3,-2,-7,8,2,-3,-1]
        # 结论：[8,2] 分别对应的index为[5,6]（消失的数字）
        for num in nums:
            index = abs(num) - 1
            # 始终保持nums[index]为负数
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
