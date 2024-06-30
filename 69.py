class Solution:
    def mySqrt(self, x: int) -> int:
        nxt_x = x/2
        x1 = nxt_x
        x2 = 1
        while int(x2) != int(x1):
            if nxt_x == 0:
                nxt_x = 0
                return nxt_x
            x1 = nxt_x
            nxt_x = 0.5 * (nxt_x + x/nxt_x)
            x2 = nxt_x
        return int(nxt_x)
''' Used Newton - Raphson method for given integer x, find its initial nxt_x = x/2, and put in formula nxt_x = 0.5 * (nxt_x + x/nxt_x)  keep iterating till round() of previous 2 nxt_x match'''

solution = Solution()
result = solution.mySqrt(0)
print(result)