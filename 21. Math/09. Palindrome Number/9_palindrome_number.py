class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x) 

        def check(left, right):
            if left >= right:
                return True
            
            if s[left] != s[right]:
                return False
            
            return check(left + 1, right - 1)

        return check(0, len(s)-1)