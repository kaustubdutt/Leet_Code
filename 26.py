class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = set(nums)
        unique_list = list(unique)
        return unique_list
result = Solution.removeDuplicates([1,2,2])
print(result)