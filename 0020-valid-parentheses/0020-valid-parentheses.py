# class Solution:
#     def isValid(self, s: str) -> bool:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for char in s:
            
            # if closing bracket
            if char in mapping:
                
                # check stack top
                top = stack.pop() if stack else '#'
                
                if mapping[char] != top:
                    return False
            
            else:
                # opening bracket
                stack.append(char)
        
        return not stack
        