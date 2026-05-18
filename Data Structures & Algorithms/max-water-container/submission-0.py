class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        areaMax = 0
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            area = h * w
            areaMax = max(areaMax, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return areaMax