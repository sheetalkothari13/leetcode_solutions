class Solution:
    c = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.c:
            return self.c[n]
        self.c[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.c[n]
        