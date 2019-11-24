#自己写的超时，每次抽最底下的
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result = 0
        for he in range(max(height)):
            i, j = 0, 0

            while i < len(height) and j < len(height):
                if height[i] - he < 1:
                    i += 1
                else:
                    j = i + 1
                    while j < len(height) and height[j] - he <= 0:
                        j += 1
                    if j < len(height):
                        tmp = j - i - 1
                        result += tmp
                        i = j
        return result


#https://leetcode-cn.com/problems/trapping-rain-water/solution/zuo-you-liang-bian-de-zui-da-zhi-by-powcai/ 接雨水
#双指针 动态规划


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        # 找位置i左边最大值
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i-1])
        # 找位置i右边最大值
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
        #print(max_left)
        #print(max_right)
        # 求结果
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]
        return res


#双指针求左右最大值
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left = 0
        right = len(height) - 1
        res = 0
        # 记录左右边最大值
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res


