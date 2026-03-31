class Solution:
    def largestRectangleArea(self,heights): 
        stack = [] 
        max_area = 0 
        n = len(heights)
    
        for i in range(n): 
            while stack and heights[stack[-1]] > heights[i]: 
                element = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                area = heights[element] * (nse - pse -1)
                max_area = max(area,max_area)
            stack.append(i) 
        while stack:
            element = stack.pop()
            nse = n
            pse = stack[-1] if stack else -1
            area = heights[element] * (nse - pse -1)
            max_area = max(area,max_area)            
        return max_area        