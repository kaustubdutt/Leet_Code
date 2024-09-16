from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permutations([], nums, result)
        return result

    def permutations(self, current: List[int], remaining: List[int], r: List[List[int]]) -> None:
        if not remaining:
            r.append(current)
            return
        for i in range(len(remaining)):
            new_current = current + [remaining[i]]
            new_remaining = remaining[:i] + remaining[i + 1:]
            self.permutations(new_current, new_remaining, r)


sol = Solution()
answer = sol.permute([1,1,2])
print(answer)