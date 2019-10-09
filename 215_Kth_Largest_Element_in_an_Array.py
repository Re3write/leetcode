class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = sorted(nums, key = lambda x : x ,reverse = True)
        return result[k-1]



#堆
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
