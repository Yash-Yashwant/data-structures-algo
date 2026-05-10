class MyQueue:

    def __init__(self):
        self.ls = []
        

    def push(self, x: int) -> None:
        self.ls.append(x)

    def pop(self) -> int:
        n = len(self.ls)-1
        self.stack2 = []
        i = 0
        while i < n:
            num = self.ls.pop()
            self.stack2.append(num)
            i+=1
        result = self.ls.pop()
        while self.stack2:
            self.ls.append(self.stack2.pop())
        return result

    def peek(self) -> int:
        return self.ls[0]
        
    def empty(self) -> bool:
        return not self.ls 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()