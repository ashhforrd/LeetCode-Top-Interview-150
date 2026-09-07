class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x) 

        return self.checkPalindrome(string, 0, len(string)-1)

    def checkPalindrome(self, s, left, right):
        if left >= right:
            return True
        
        if s[left] != s[right]:
            return False
        
        return self.checkPalindrome(s, left+1, right-1)