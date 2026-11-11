class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if self.stack and price >= self.stack[-1][0]:
            count = 1

            while self.stack and self.stack[-1][0] <= price:
                stock = self.stack.pop()
                count += stock[1]
            
            self.stack.append([price, count])
            return count

        self.stack.append([price, 1])
        return 1
        
# menit 9 51/101
# menit 9 51/101

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
