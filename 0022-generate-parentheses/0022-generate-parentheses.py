class Solution:
    def generateParenthesis(self, n: int):
        result = []
        current = []

        def backtrack(open_used, close_used):
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            if open_used < n:
                current.append("(")
                backtrack(open_used + 1, close_used)
                current.pop()   

            if close_used < open_used:
                current.append(")")
                backtrack(open_used, close_used + 1)
                current.pop()      

        backtrack(0, 0)
        return result