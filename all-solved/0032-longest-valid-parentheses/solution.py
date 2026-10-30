class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        count = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])   
        
        return count
    
    # def countParentesis(self, )
