from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        for i in range(k, len(nums)):
            nums[i] = '_'
        print(nums)
        return k

solution = Solution()
result = solution.removeElement([0,1,2,2,3,0,4,2], 2)
print(result)
