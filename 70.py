class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = n + 1
        if n <= 0:
            result = 0
            return result
        else:
            if n1 <= 0:
                return 0
            elif n1 == 1:
                return 1

            prev1, prev2 = 0, 1
            for _ in range(2, n1 + 1):
                current = prev1 + prev2
                prev1, prev2 = prev2, current

            return prev2


# Example usage:
solution = Solution()
print(solution.climbStairs(0))