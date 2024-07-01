from typing import List
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        average = []
        while len(nums) != 0:
            maxy = max(nums)
            nums.remove(maxy)
            miny = min(nums)
            nums.remove(miny)
            avg = (maxy + miny)/2
            average.append(avg)
        return min(average)

solution = Solution()
result = solution.minimumAverage([7,8,3,4,15,13,4,1])
print(result)