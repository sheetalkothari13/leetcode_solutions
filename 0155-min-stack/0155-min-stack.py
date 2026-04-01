class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        return None

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val , val)
        element = [val,self.min_val]
        self.stack.append(element)
        return None

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_val = self.stack[-1][1]
        else:
            self.min_val = float('inf')
        return None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()