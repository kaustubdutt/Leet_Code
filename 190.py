class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = f'{n:032b}'
        n = binary_string[::-1]
        return int(n,2)

solution = Solution()
result = solution.reverseBits(43261596)
print(result)