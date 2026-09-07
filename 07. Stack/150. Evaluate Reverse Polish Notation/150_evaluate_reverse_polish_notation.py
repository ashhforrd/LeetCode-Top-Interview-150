class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        numStack = []
        result = 0

        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i].startswith('-') and len(tokens[i]) > 1 and tokens[i][1:].isdigit():
                numStack.append(tokens[i])

            elif tokens[i] in ops:
                operator = tokens[i]
                first = int(numStack.pop())
                second = int(numStack.pop())

                if operator == "+":
                    result = second + first
                elif operator == "-":
                    result = second - first
                elif operator == "*":
                    result = second * first
                elif operator == "/":
                    result = int(second / first)

                numStack.append(str(result))
        
        return int(numStack[0])