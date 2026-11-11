class MyQueue:

    def __init__(self):
        self.s = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()

        while self.s:
            n = self.s.pop()
            self.s2.append(n)
        
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]

        while self.s:
            n = self.s.pop()
            self.s2.append(n)
        
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s) == 0 and len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
