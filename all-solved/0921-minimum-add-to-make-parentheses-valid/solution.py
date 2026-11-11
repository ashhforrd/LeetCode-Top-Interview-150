class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        closeParentheses = 0

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack:
                    closeParentheses += 1
                else:
                    stack.pop()
        
        return len(stack) + closeParentheses
