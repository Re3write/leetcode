#range逆序了解一下

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for index in range(length-1,-1,-1):
            if nums[index] == 0:
                while index<length-1:
                      nums[index],nums[index+1] = nums[index+1] , nums[index]
                      index+=1



nums = [0,1,0,3,12]
count = nums.count(0)
for x in range(count):
    nums.remove(0)
    nums.append(0)
print(nums)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums[:]:   ####遍历原数组的副本
            if i==0:
                nums.append(0)
                nums.remove(0)



# 我的思路是这样的，所谓要把0移动到数组后面，其实就是把非0数给移动到数组前面，
# 而每个非0数需要移动的步数其实就是这个非0数前面0的个数。
#
# 例如题目中的case：
#
# [0, 1, 0, 3, 2]
# 按我的思路，那就是1需要移动1步，3和2需要移动两步。在完成这三个数的移动后，将后面补0即可。
#
# 这里其实就是维护了一个计数变量count，请看代码，然后画个图就能懂了。
#
# class Solution {
#     public void moveZeroes(int[] nums) {
#         int count = 0;
#         for(int i = 0; i < nums.length; i++) {
#             if(nums[i] == 0) {
#                 count++;
#             }else {
#                 nums[i - count] = nums[i];
#             }
#         }
#         for(int i = nums.length - count; i < nums.length; i++) {
#             nums[i] = 0;
#         }
#     }
# }




#
#
# 思路：可以先把所有非0的元素移到前面，然后将后面的位置补0。
# 使用指针i，指向需要插入的下标，使用指针j指向遍历的下标。遍历一遍，如果j指向的位置为0，则i不变，j++后移；如果j指向的位置不为0，则将j位置的元素值赋值到i位置，然后i++。
#
# class Solution {
#     public void moveZeroes(int[] nums) {
#         //i:插入位置下标 ; j:查找位置下标
#         int i = 0;
#         for(int j = 0; j < nums.length; j++){
#             if(nums[j] != 0){
#                 nums[i] = nums[j];
#                 i++;
#             }
#         }
#         //将后面的位置补0
#         for(int p = i; p < nums.length; p++){
#             nums[p] = 0;
#         }
#     }
# }