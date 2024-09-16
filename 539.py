from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        l = len(timePoints)
        for i in range(l):
            x = timePoints[i]
            x = x.split(':')
            x[0] = int(x[0]) * 60
            x[1] = int(x[1])
            timePoints[i] = x[0] + x[1]
        timePoints.sort()
        diff = []
        for i in range(l):
            if i == l - 1:
                d = abs(timePoints[i] - timePoints[0])
                diff.append(d)
                break
            d = abs(timePoints[i] - timePoints[i+1])
            diff.append(d)
        diff2 = [1440-x for x in diff]
        for i in range(len(diff)):
            if diff[i] > diff2[i]:
                diff[i] = diff2[i]
        result = min(diff)
        return result


solution = Solution()
result = solution.findMinDifference(["00:00","04:00","22:00"])
print(result)