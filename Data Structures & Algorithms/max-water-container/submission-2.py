class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        n = len(heights)
        j, k = 0, n-1
        while j < k:
            water = max(min(heights[j], heights[k]) * (k-j), water)
            if heights[j] < heights[k]:
                j+=1
            else:
                k-=1

        return water