class Solution:
    def maxDepth(self, s: str) -> int:
        g,r = 0,0
        for ch in s:
            if ch == "(" :
                r+=1
                g = max(g,r)
            elif ch == ")":
                r-=1
        return(g)