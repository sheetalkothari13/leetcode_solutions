class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        
        while l<r:
            length = r-l
            if height[l] < height[r]:
                curr = height[l] * length
                l += 1
            else:
                curr = height[r] * length
                r -= 1
            max_water = max(max_water,curr)
        return max_water
        