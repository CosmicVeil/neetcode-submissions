class MinStack:


    def __init__(self):
        self.stack = []
        self.minElem = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minElem)==0:
            self.minElem.append(val)
        else:
            self.minElem.append(min(val, self.minElem[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minElem.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minElem[-1]

        
