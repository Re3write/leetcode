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

#
# 将数组元素对应为索引的位置加n
# 遍历加n后的数组，若数组元素值小于等于n，则说明数组下标值不存在，即消失的数字
# class Solution {
# public:
#     vector<int> findDisappearedNumbers(vector<int>& nums) {
#         vector<int> res;
#         if(nums.empty()) return nums;
#         for(int i=0;i<nums.size();i++)
#         {
#             int index=(nums[i]-1)%nums.size();
#             nums[index]+=nums.size();
#         }
#         for(int i=0;i<nums.size();i++)
#         {
#             if(nums[i]<=nums.size())
#                 res.push_back(i+1);
#         }
#         return res;
#     }
# };

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

    # 稍微解释下，最高赞的 @ 江南花家七公子的答案，遍历一遍nums数组，把每一位上的数组元素绝对值（因为有可能被之前的遍历标记为负数，但其绝对值依旧保留了原始的数组下标信息）当成数组下标，定位到属于这个数值元素的位置，这里注意一下错位对应，因为数组需要从0开始的。定位到属于该数组元素的位置后，利用令该位置上的值为负数进行标记，这里就可以无视重复的元素值带来的影响（不管重复几次，这个位置上还是负值）。最后，
    # 没有出现在[1, n]
    # 范围内的数字，他对应数组下标上的数组元素是不会被标记为负数的，再遍历一次就可以找到答案。 方法好牛逼，学到了。
