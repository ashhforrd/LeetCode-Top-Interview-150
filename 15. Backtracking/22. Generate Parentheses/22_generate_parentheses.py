class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        length = n * 2
        openCount, closeCount = 0, 0

        curr = ""
        res = []

        def generate(curr, openCount, closeCount):
            if len(curr) == length:
                res.append(curr)
            
            if openCount < n:
                generate(curr + "(", openCount + 1, closeCount)
            if closeCount < openCount:
                generate(curr + ")", openCount, closeCount + 1)

        generate(curr, openCount, closeCount)

        return res