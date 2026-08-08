class Solution:
    def climbStairs(self, n: int) -> int:
        c = {}

        def solve(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in c:
                return c[n]

            c[n] = solve(n - 1) + solve(n - 2)
            return c[n]

        return solve(n)