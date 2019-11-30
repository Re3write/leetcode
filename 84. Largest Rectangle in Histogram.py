# 我们可以基于方法 1 进行一点点修改来优化算法。我们可以用前一对柱子之间的最低高度来求出当前柱子对间的最低高度。
#
# 用数学语言来表达，minheight=\min(minheight, heights(j))minheight=min(minheight,heights(j)) ，其中， heights(j)heights(j) 是第 j 个柱子的高度。
#
# Java
# public class Solution {
#    public int largestRectangleArea(int[] heights) {
#        int maxarea = 0;
#        for (int i = 0; i < heights.length; i++) {
#            int minheight = Integer.MAX_VALUE;
#            for (int j = i; j < heights.length; j++) {
#                minheight = Math.min(minheight, heights[j]);
#                maxarea = Math.max(maxarea, minheight * (j - i + 1));
#            }
#        }
#        return maxarea;
#    }
# }


# 从上可以看出，矩形的面积取决于区间中最小的高度，因此考虑以拥有最小高度的点作为分治中心，将区域分为三份。
# 因此区间中的最大面积为
# max(
# 最小高度 * 区间长度，
# 最小高度左侧的最大面积，
# 最小高度右侧的最大面积
# )


# 分治算法
# class Solution3:
#     def largestRectangleArea(self, heights: [int]) -> int:
#         def divide(left, right):
#             if right < left:
#                 return 0
#
#             min_i = left
#             for i in range(left, right + 1):
#                 if heights[i] < heights[min_i]:
#                     min_i = i
#
#             return max((right - left + 1) * heights[min_i],
#                         divide(left, min_i-1), divide(min_i+1, right))
#         return divide(0, len(heights) - 1)



#单调栈 分治法
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res
