class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxw = 0
        n = len(heights)
        for i in range(n):
            for j in range(i+1, n):
                water = min(heights[i], heights[j]) * (j-i)
                if water > maxw:
                    maxw = water
        return maxw