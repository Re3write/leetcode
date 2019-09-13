#一下通过
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for number in nums:
            dict[number] = dict.get(number,0) + 1
        top_k = sorted(zip(dict.keys(),dict.values()),key = lambda x:x[1], reverse = True)
        i= 0
        result = []
        while i < k:
            result.append(top_k[i][0])
            i+=1
        return result


import heapq
import collections


##堆排序   heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

        #类似sort heapq.nlargest   key可以是lambda，也可以是get生成式， 在外面用是count.get()，这样就不用zip自己了
