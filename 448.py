from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]

        return result


solution = Solution()
result = solution.findDisappearedNumbers([1,1,3])
print(result)