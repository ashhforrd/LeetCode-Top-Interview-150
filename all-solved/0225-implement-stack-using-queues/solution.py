class MyStack:

    def __init__(self):
        self.q = deque()
        self.p = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.p.append(self.q.popleft())
                
        pop = self.q.popleft()

        while self.p:
            self.q.append(self.p.popleft())
        
        return pop
        
    def top(self) -> int:
        for _ in range(len(self.q) - 1):
            self.p.append(self.q.popleft())
                
        top = self.q[0]
        self.p.append(self.q.popleft())

        while self.p:
            self.q.append(self.p.popleft())
        
        return top

    def empty(self) -> bool:
        return len(self.q) == 0 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
