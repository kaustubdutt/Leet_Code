class Solution:
    def hammingWeight(self, n: int) -> int:
        bin1 = bin(n)
        str_bin = str(bin1)
        ones = 0
        for one in str_bin:
            if one == '1':
                ones += 1
        return ones

solution = Solution()
result = solution.hammingWeight(13)
print(result)