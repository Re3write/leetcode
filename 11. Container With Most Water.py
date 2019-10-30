class Solution:
    def maxArea(self, height: List[int]) -> int:
        ind1, ind2 = 0, len(height) - 1
        tmp_area = 0
        max_area = 0
        while ind1 != ind2:
            tmp_area = min(height[ind1], height[ind2]) * (ind2 - ind1)
            max_area = max(tmp_area, max_area)
            if height[ind1] < height[ind2]:
                ind1 += 1
            else:
                ind2 -= 1

        return max_area