class Solution:
    def reverse(self, x: int) -> int:
        y = x
        reverse = 0
        negative = False
        if x < 0:
            y *= -1
            negative = True
        while y != 0:
            digit = y % 10
            reverse = reverse * 10 + digit
            y //= 10
        if reverse > 2**31 - 1 or reverse < -2**31:
                return 0
        elif negative:
            return reverse * -1
        else:
            return reverse

        