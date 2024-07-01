from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sol = {}
        for i,num in enumerate(nums):
            if num in sol:
                sol[num] += 1
            else:
                sol[num] = 1
        max_count = -1
        majority_element = None

        for num, count in sol.items():
            if count > max_count:
                max_count = count
                majority_element = num

        return majority_element





solution = Solution()
result = solution.majorityElement([3, 6, 9, 7, 7, 7, 7])
print(result)