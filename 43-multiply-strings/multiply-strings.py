class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        accNum1 = eval(num1)
        accNum2 = eval(num2)
        return str(accNum1*accNum2)