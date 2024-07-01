class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        suma = 0
        x1 = x
        if x == 0:
            return 0
        else:
            while x != 0:
                digit = x % 10
                suma = suma + digit
                x = x // 10
        print(suma)
        return suma if x1 % suma == 0 else -1

solution = Solution()
result = solution.sumOfTheDigitsOfHarshadNumber(0)
print(result)
