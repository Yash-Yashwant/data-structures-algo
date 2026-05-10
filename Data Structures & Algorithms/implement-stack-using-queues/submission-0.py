class MyStack:

    def __init__(self):
        self.ls = []
        

    def push(self, x: int) -> None:
        self.ls.append(x)

    def pop(self) -> int:
        n = len(self.ls)
        for i in range(n-1):
            temp = self.ls.pop(0)
            self.ls.append(temp)
        return self.ls.pop(0)

    def top(self) -> int:
        return self.ls[-1]
        

    def empty(self) -> bool:
        return self.ls == []
            
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()