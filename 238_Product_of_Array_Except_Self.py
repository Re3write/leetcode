class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0:
            return [0]
        front = [1 for _ in range(length)]
        back = [1 for _ in range(length)]
        for i in range(1, length):
            front[i] = front[i - 1] * nums[i - 1]
        for i in range(length - 2, -1, -1):
            back[i] = back[i + 1] * nums[i + 1]
        result = []
        for i in range(length):
            result.append(front[i] * back[i])
        return result



#O(N)双指针双向遍历
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], l = res[i] * l, l * nums[i]
            res[j], r = res[j] * r, r * nums[j]
        return res


