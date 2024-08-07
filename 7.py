class Solution:
    def reverse(self, x: int) -> int:
        maxy = (2 ** 31) - 1
        miny = -2 ** 31
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x < maxy:
                return x
            else:
                return 0
        elif x < 0:
            x = x * -1
            x = str(x)
            x = x[::-1]
            x = '-' + x
            x = int(x)
            if x > miny:
                return x
            else:
                return 0
        else:
            return x

solution = Solution()
result = solution.reverse(1534236469)
print(result)