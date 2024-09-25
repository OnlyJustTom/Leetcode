class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        else:
            reverse = 0
            y = x
            while y != 0:    
                digit = y % 10
                reverse = reverse * 10 + digit
                y //= 10
            return reverse == x