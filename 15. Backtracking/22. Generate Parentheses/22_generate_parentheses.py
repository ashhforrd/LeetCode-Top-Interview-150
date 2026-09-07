class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        length = n * 2
        open_count = 0
        close_count = 0
        result = ""
        final = []

        self.summonParenthesis(result, length, n, open_count, close_count, final)

        return final
    
    def summonParenthesis(self, result, length, n, open_count, close_count, final):
        if len(result) == length:
            final.append(result)

        if open_count < n:
            temp = result + "("
            self.summonParenthesis(temp, length, n, open_count+1, close_count, final)
        
        if close_count < open_count:
            temp = result + ")"
            self.summonParenthesis(temp, length, n, open_count, close_count+1, final)
