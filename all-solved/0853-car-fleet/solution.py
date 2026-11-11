class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        stack.append(((target - position[0]) / speed[0], position[0]))

        for i in range(1, len(position)):
            time = (target - position[i]) / speed[i]
            stack.append((time, position[i]))
        
        stack.sort(key=lambda x: x[1], reverse=True)
        
        newStack = [stack[0][0]]

        for i in range(1, len(position)):
            n = newStack[-1]
            if stack[i][0] <= n:
                continue
            else:
                newStack.append(stack[i][0])
        
        return len(newStack)
