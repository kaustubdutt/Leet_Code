class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

solution = Solution()
print(solution.singleNumber([1,2,3,3,2]))