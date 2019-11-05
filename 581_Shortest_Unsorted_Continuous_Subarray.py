import numpy as np
# print([True if x != 0 else False for x in result]) 列表生成式
#排序前后相减
import numpy as np


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        new_nums = sorted(nums, key=lambda x: x, reverse=False)
        result = np.array(new_nums) - np.array(nums)
        index1 = (result != 0).argmax(axis=0)
        index2 = len(result) - (result[::-1] != 0).argmax(axis=0)

        if max(result) == 0:
            return 0
        else:
            return index2 - index1



class Solution:  #同时循环简介写法
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1

