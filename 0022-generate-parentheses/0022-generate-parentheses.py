class Solution:
    def generateParenthesis(self, n: int):
        result = []
        current = []

        def backtrack(open_used, close_used):

            # Base case: we have used all parentheses
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Option 1: Add '(' if we still have some left
            if open_used < n:
                current.append("(")
                backtrack(open_used + 1, close_used)
                current.pop()      # Backtrack

            # Option 2: Add ')' only if it won't make the string invalid
            if close_used < open_used:
                current.append(")")
                backtrack(open_used, close_used + 1)
                current.pop()      # Backtrack

        backtrack(0, 0)
        return result