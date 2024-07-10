from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        print(matrix)


sol = Solution()
result = sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
print(result)