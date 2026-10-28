class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        
        string = str(x)
        string = string[::-1]

        new_int = int(string)

        if new_int < -2*31 or new_int > 2**31-1:
            return 0

        if negative == True:
            return -1 * new_int 
        else:
            return new_int
