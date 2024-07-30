from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        print(dict1)
        for key in dict1:
            if dict1[key] == 1:
                return key
            else:
                continue

solution = Solution()
result = solution.singleNumber([0,1,0,1,0,1,99])
print(result)