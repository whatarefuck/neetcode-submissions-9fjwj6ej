class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0
        l, r = 0, len(heights) - 1
        while l < r:
            amount = (r - l) * min(heights[l], heights[r])
            if amount > ret:
                ret = amount
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return ret