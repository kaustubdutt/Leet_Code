from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count1 = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                count1 += 1
            else:
                count1 = 0
            if count1 == 3:
                return True
        return False







solution = Solution()
result = solution.threeConsecutiveOdds([3, 6, 9, 7, 4, 7 ,7])
print(result)