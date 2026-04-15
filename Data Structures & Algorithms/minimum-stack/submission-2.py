class MinStack:

    def __init__(self,min_val=2e30 -1):
        self.arr = []
        self.min_val = min_val
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if val < self.min_val:
            self.min_val = val
        self.arr.append(self.min_val)


    def pop(self) -> None:
        self.arr.pop()
        if self.arr.pop() == self.min_val:
            if len(self.arr) != 0:
                self.min_val = self.arr[-1]
            else: 
                self.min_val = 2e30-1
        
        

    def top(self) -> int:
        return self.arr[-2]
        

    def getMin(self) -> int:
        return self.arr[-1]
        

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()