from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        max_op = {0:0,1:0,2:0,3:0}
        for i in range(len(nums)):
            diff = nums[i] % 3
            max_op[diff] += 1
        sum = max_op[1] + max_op[2]
        return sum

solution = Solution()
result = solution.minimumOperations([3,6,9])
print(result)

