from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t_matrix = zip(*matrix)
        result = list(map(list,t_matrix))
        return result

sol = Solution()
result = sol.transpose([[1,2,3],[4,5,6],[7,8,9]])
print(result)