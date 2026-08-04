class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        result = []
        current = []

        def backtrack(start, total):
            if total == n and len(current) == k:
                result.append(current[:])
                return

            if total > n or len(current) == k:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                current.pop()

        backtrack(0, 0)
        return result        