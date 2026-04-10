class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        ret = 0

        while l < r:
            if height[l] < height[r]:
                available_volume = max_l - height[l]
                max_l = max(max_l, height[l])
                l += 1
            else:
                available_volume = max_r - height[r]
                max_r = max(max_r, height[r])
                r -= 1

            if available_volume > 0:
                ret += available_volume
        
        return ret