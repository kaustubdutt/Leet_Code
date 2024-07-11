class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            if n > 0:
                bin_n = bin(n)
                bin_n = bin_n[3:]
                return int(bin_n,2) == 0


solution = Solution()
result = -2**4
print(solution.isPowerOfTwo(result))