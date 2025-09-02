class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        open = 0
        for i in s:
            if i == '(' and open>0 :
                res.append(i)
            elif i == ')' and open>1 :
                res.append(i)
            if i == '(' :
                open += 1
            else:
                open -=1
        return "".join(res)
            
        