class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for ast in asteroids:
            isCollision = True

            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) > abs(stack[-1]):
                    stack.pop()
                    isCollision = True

                elif abs(ast) == abs(stack[-1]):
                    stack.pop()
                    isCollision = False
                    break

                else:
                    isCollision = False
                    break
            
            if isCollision:
                stack.append(ast)
                    
        return stack
