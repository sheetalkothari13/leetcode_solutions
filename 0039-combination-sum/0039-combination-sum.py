class Solution:
    def combinationSum(self, candidates, target):
        result = []
        current = []

        def backtrack(start, total):
            if total == target:
                result.append(current[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, total + candidates[i])
                current.pop()

        backtrack(0, 0)
        return result