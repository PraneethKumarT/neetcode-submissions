class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None or val < self.min:
            self.min = val
        self.minStack.append(self.min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
            self.min = self.getMin()

        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None

