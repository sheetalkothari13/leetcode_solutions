class Solution:
    def myPow(self, x, n):
        MOD = 10**9 + 7

        if n == 0:
            return 1

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return (half * half) % MOD
        else:
            return (x * half * half) % MOD

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        even = (n + 1) // 2
        odd = n // 2

        return (self.myPow(5, even) * self.myPow(4, odd)) % MOD