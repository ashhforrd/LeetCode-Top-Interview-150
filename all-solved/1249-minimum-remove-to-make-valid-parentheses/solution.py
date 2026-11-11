class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(["(", i])
            elif s[i] == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append([")", i])
        
        numSet = set()
        while stack:
            _, idx = stack.pop()
            numSet.add(idx)
                
        res = ""
        for i in range(len(s)):
            if i not in numSet:    
                res += s[i]
        
        return res
