class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        starStack = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append((c, i))
            elif c == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
            elif c == "*":
                starStack.append((c, i))
                
        while stack:
            if starStack and stack[-1][1] <= starStack[-1][1]:
                stack.pop()
                starStack.pop()
            else:
                return False
        
        return len(stack) == 0
